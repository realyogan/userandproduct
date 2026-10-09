#!/usr/bin/env python3
"""Small DataForSEO REST client for the userandproduct.com research store.

Standard library only. Credentials come from an env file (never printed, logged or saved):
    .local/dataforseo.env with DATAFORSEO_LOGIN=... and DATAFORSEO_PASSWORD=...
The path can be overridden with the environment variable DATAFORSEO_ENV.

What it does on every call
- Cache check (paid calls only): before sending, cache/index.csv is searched for a row with the
  same subject and endpoint younger than the reuse window (30 days volumes/SERPs/domains, 60 days
  ideas, suggestions and ranked keywords, 90 days sitemaps). A fresh hit means the call is skipped
  and None is returned.
- Budget guard: the client is created with a per-run cap in dollars. It sums the "cost" field of
  every response and refuses the next request when running total + last observed cost per request
  would exceed the cap. It prints what the request would have cost and raises BudgetExceeded.
- Raw save first: every response is written to cache/raw/<id>.json before anything else, where
  id is YYMMDD-NNN continuing after the highest NNN already in cache/index.csv for that day.
- Dry run: prints the request (method, URL, body) without sending it.

Usage (from the project root)

    import sys; sys.path.insert(0, "research/seo/tools")
    from dataforseo_client import Client

    c = Client(cap=2.00)                 # dry_run=True to print requests only
    c.balance()                          # free; prints only the balance
    res = c.post("dataforseo_labs/google/keyword_ideas/live",
                 [{"keywords": ["ux research"], "location_code": 2840, "language_code": "en"}],
                 subject="ux research")  # subject enables the cache check; None = skipped
    if res:
        c.index_row(res["_id"], "dataforseo", "dataforseo_labs/google/keyword_ideas/live",
                    "ux research", "2840", res["_file"], "note")
    print(c.spent)

    python research/seo/tools/dataforseo_client.py balance     # command-line balance check

post() and get() return the parsed JSON response with two extra keys added after saving:
"_id" (the raw id) and "_file" (path relative to research/seo, for the index row).
"""
import base64
import csv
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SEO = os.path.dirname(HERE)                       # research/seo
ROOT = os.path.dirname(os.path.dirname(SEO))      # project root
INDEX = os.path.join(SEO, "cache", "index.csv")
RAW = os.path.join(SEO, "cache", "raw")
API = "https://api.dataforseo.com/v3/"
DEFAULT_ENV = os.path.join(ROOT, ".local", "dataforseo.env")
FREE_PATHS = ("appendix/user_data",)


class BudgetExceeded(RuntimeError):
    pass


def reuse_days(endpoint):
    e = endpoint.lower()
    if "sitemap" in e:
        return 90
    if any(k in e for k in ("keyword_ideas", "keyword_suggestions", "related_keywords", "ranked_keywords")):
        return 60
    return 30


def load_env(path=None):
    path = path or os.environ.get("DATAFORSEO_ENV") or DEFAULT_ENV
    vals = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    if not vals.get("DATAFORSEO_LOGIN") or not vals.get("DATAFORSEO_PASSWORD"):
        raise RuntimeError("env file is missing DATAFORSEO_LOGIN or DATAFORSEO_PASSWORD")
    return vals


def read_index():
    if not os.path.exists(INDEX):
        return []
    with open(INDEX, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def next_id(today=None):
    today = today or dt.date.today()
    prefix = today.strftime("%y%m%d")
    pat = re.compile(r"^%s-(\d{3,})$" % prefix)
    high = 0
    for row in read_index():
        m = pat.match(row.get("id", ""))
        if m:
            high = max(high, int(m.group(1)))
    # also respect raw files written but not yet indexed
    if os.path.isdir(RAW):
        for name in os.listdir(RAW):
            m = pat.match(name[:-5]) if name.endswith(".json") else None
            if m:
                high = max(high, int(m.group(1)))
    return "%s-%03d" % (prefix, high + 1)


def index_row(id, source, endpoint, subject, location, file, note, date=None):
    """Append one row to cache/index.csv (id,date,source,endpoint,subject,location,file,note)."""
    date = date or dt.date.today().isoformat()
    with open(INDEX, "a", encoding="utf-8", newline="") as fh:
        csv.writer(fh, lineterminator="\r\n").writerow(
            [id, date, source, endpoint, subject, location, file, note])


def cached(subject, endpoint, today=None):
    """Return the freshest index row for subject + endpoint inside the reuse window, else None."""
    today = today or dt.date.today()
    window = reuse_days(endpoint)
    ep = endpoint.strip("/").lower()
    best = None
    for row in read_index():
        if row.get("subject", "").strip().lower() != subject.strip().lower():
            continue
        if ep not in row.get("endpoint", "").lower():
            continue
        if "; status " in row.get("note", ""):
            continue  # a failed call (error status recorded in the note) is not cached data
        try:
            d = dt.date.fromisoformat(row["date"])
        except (KeyError, ValueError):
            continue
        if (today - d).days < window and (best is None or row["date"] > best["date"]):
            best = row
    return best


class Client:
    def __init__(self, cap, dry_run=False, env_path=None, verbose=True):
        self.cap = float(cap)
        self.dry_run = dry_run
        self.verbose = verbose
        self.spent = 0.0
        self.last_cost = 0.0
        self.requests = 0
        self._env_path = env_path

    def _auth(self):
        e = load_env(self._env_path)
        token = base64.b64encode(("%s:%s" % (e["DATAFORSEO_LOGIN"], e["DATAFORSEO_PASSWORD"])).encode()).decode()
        return "Basic " + token

    def _send(self, method, path, body=None, save=True):
        path = path.strip("/")
        if path.startswith("v3/"):
            path = path[3:]
        url = API + path
        data = json.dumps(body).encode("utf-8") if body is not None else None
        paid = path not in FREE_PATHS
        if self.dry_run:
            print("DRY RUN %s %s" % (method, url))
            if body is not None:
                print(json.dumps(body, indent=1))
            return None
        if paid and self.spent + self.last_cost > self.cap:
            msg = ("budget guard: next request would cost about $%.4f; spent $%.4f of $%.2f cap; not sent"
                   % (self.last_cost, self.spent, self.cap))
            print(msg)
            raise BudgetExceeded(msg)
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", self._auth())
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                raw = resp.read()
        except urllib.error.HTTPError as err:
            raw = err.read()
        text = raw.decode("utf-8", errors="replace")
        rid = rel = None
        if save:
            rid = next_id()
            os.makedirs(RAW, exist_ok=True)
            with open(os.path.join(RAW, rid + ".json"), "w", encoding="utf-8") as fh:
                fh.write(text)
            rel = "cache/raw/%s.json" % rid
        res = json.loads(text)
        cost = float(res.get("cost") or 0)
        self.requests += 1
        if paid:
            self.spent += cost
            self.last_cost = cost
        if isinstance(res, dict):
            res["_id"] = rid
            res["_file"] = rel
        return res

    def post(self, path, tasks, subject=None):
        """POST a task list. With subject, skip (return None) on a fresh cache hit."""
        if subject:
            hit = cached(subject, path)
            if hit:
                if self.verbose:
                    print("cache hit: %s %s -> %s (%s); skipped" % (subject, path, hit["file"], hit["date"]))
                return None
        return self._send("POST", path, tasks)

    def get(self, path, subject=None, save=True):
        if subject:
            hit = cached(subject, path)
            if hit:
                if self.verbose:
                    print("cache hit: %s %s -> %s (%s); skipped" % (subject, path, hit["file"], hit["date"]))
                return None
        return self._send("GET", path, save=save)

    def balance(self):
        """Free call; prints and returns only the account balance (not saved to the cache)."""
        res = self._send("GET", "appendix/user_data", save=False)
        if res is None:
            return None
        try:
            bal = res["tasks"][0]["result"][0]["money"]["balance"]
        except (KeyError, IndexError, TypeError):
            print("balance: unavailable (status %s)" % res.get("status_code"))
            return None
        print("balance: $%.2f" % bal)
        return bal


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "balance":
        Client(cap=0).balance()
    else:
        print(__doc__)
