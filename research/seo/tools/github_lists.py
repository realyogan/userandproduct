"""Pull GitHub "awesome" lists and build the Useful links inventory.

Usage: python -I research/seo/tools/github_lists.py [fetch|parse|all]   (run from the project root)

fetch  downloads each list's README into research/seo/competitors/github-lists/raw/<owner>__<repo>.md
       and its license into github-lists/licenses.json (one-second delay between requests).
parse  reads the raw files and writes inventory-links-github.csv, inventory-links-github-sections.csv
       and inventory-links-github-summary.md under research/seo/competitors/.
Standard library only.
"""
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
COMP = os.path.join(ROOT, "research", "seo", "competitors")
LISTS_DIR = os.path.join(COMP, "github-lists")
RAW_DIR = os.path.join(LISTS_DIR, "raw")
LICENSES = os.path.join(LISTS_DIR, "licenses.json")
OUT_CSV = os.path.join(COMP, "inventory-links-github.csv")
OUT_SECTIONS = os.path.join(COMP, "inventory-links-github-sections.csv")
OUT_SUMMARY = os.path.join(COMP, "inventory-links-github-summary.md")

# (owner/repo, branch, readme file name)
LISTS = [
    ("dend/awesome-product-management", "master", "README.md"),
    ("ProductHired/open-product-management", "master", "README.md"),
    ("bradtraversy/design-resources-for-developers", "master", "readme.md"),
    ("gztchan/awesome-design", "master", "README.md"),
    ("LisaDziuba/Awesome-Design-Tools", "master", "README.md"),
    ("ttt30ga/awesome-product-design", "main", "README.md"),
    ("batoreh/awesome-ux", "master", "README.md"),
    ("alexpate/awesome-design-systems", "master", "README.md"),
    ("lorabv/awesome-agile", "master", "README.md"),
    ("bekatom/awesome-growth-hacking", "master", "README.md"),
    ("samber/awesome-user-research", "main", "README.md"),
    ("domenicosolazzo/awesome-okr", "master", "README.md"),
]

UA = {"User-Agent": "userandproduct-research/1.0"}
LINK_SEEDS = ["bookmarks.design", "uxtools.co", "toools.design", "uxdatabase.io", "designresourc.es"]

# Navigation and boilerplate sections that never hold entries.
SKIP_SECTIONS = re.compile(
    r"^(contents|table of contents?|toc|index|contribut\w*|how to contribute|license|licence|credits?|thanks|"
    r"acknowledg\w*|support|sponsors?|backers?|footnotes?|about|code of conduct|authors?|maintainers?|"
    r"related lists?|other awesome lists?|to create a better knowledge space.*)$",
    re.I,
)
SKIP_HOSTS = {
    "img.shields.io", "badgen.net", "awesome.re", "travis-ci.org", "travis-ci.com", "creativecommons.org",
    "opensource.org", "i.imgur.com", "user-images.githubusercontent.com", "raw.githubusercontent.com",
    "camo.githubusercontent.com", "gitter.im", "forthebadge.com", "badge.fury.io", "github.githubassets.com",
}
# Hosting platforms: a link to them is a page on the platform, not the platform as a tool.
PLATFORM_HOSTS = {"youtube.com", "youtu.be", "medium.com", "amazon.com", "twitter.com", "x.com", "linkedin.com",
                  "quora.com", "slideshare.net", "vimeo.com", "speakerdeck.com", "docs.google.com", "bit.ly",
                  "goo.gl", "amzn.to", "soundcloud.com", "podcasts.apple.com", "itunes.apple.com", "ted.com"}
# Headings that are not categories in a given list, mapped to the category they stand for.
SECTION_OVERRIDES = {("alexpate/awesome-design-systems", "Tags"): "Design Systems"}
# Key-value table rows used by some lists to describe one tool (the tool is the heading above).
KV_LABELS = {"property", "developer", "cost", "platform", "platforms", "price", "pricing", "license"}
BARE_URL = re.compile(r"https?://[^\s|)>\]]+")
GENERIC_NAMES = {"link", "here", "website", "source", "demo", "github", "back to top", "top", "read more",
                 "more", "pdf", "video", "article", "repo"}


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def api_license(repo):
    """Repo license via the public GitHub API (None when the repo has no license file)."""
    try:
        data = json.loads(get("https://api.github.com/repos/%s/license" % repo))
        spdx = (data.get("license") or {}).get("spdx_id")
        if spdx == "NOASSERTION":
            return "other (see repo LICENSE)"
        return spdx
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        return "unknown (API error %s)" % e.code
    except Exception as e:  # network trouble
        return "unknown (%s)" % e


def readme_license(text):
    t = text.lower()
    for pat, name in [
        (r"publicdomain/zero|\bcc0\b", "CC0-1.0"),
        (r"licenses/by-sa/4\.0|cc by-sa 4|cc-by-sa-4", "CC-BY-SA-4.0"),
        (r"licenses/by/4\.0|cc by 4|cc-by-4", "CC-BY-4.0"),
        (r"\bunlicense\b", "Unlicense"),
        (r"mit license", "MIT"),
    ]:
        if re.search(pat, t):
            return name + " (stated in README)"
    return None


def fetch():
    os.makedirs(RAW_DIR, exist_ok=True)
    licenses = {}
    for repo, branch, fname in LISTS:
        out = os.path.join(RAW_DIR, repo.replace("/", "__") + ".md")
        url = "https://raw.githubusercontent.com/%s/%s/%s" % (repo, branch, fname)
        try:
            text = get(url)
        except Exception as e:
            print("FAILED", repo, e)
            licenses[repo] = "not fetched (%s)" % e
            time.sleep(1)
            continue
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print("ok", repo, len(text))
        time.sleep(1)
        lic = api_license(repo)
        if not lic or lic.startswith("other") or lic.startswith("unknown"):
            lic = readme_license(text) or lic or "none stated"
        licenses[repo] = lic
        time.sleep(1)
    with open(LICENSES, "w", encoding="utf-8") as f:
        json.dump(licenses, f, indent=2)


HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_HEADING = re.compile(r"^\s*<h([1-6])[^>]*>(.*?)</h[1-6]>", re.I)
BOLD_HEADING = re.compile(r"^\s*\*\*([^*]{2,60})\*\*\s*:?\s*$")
MD_LINK = re.compile(r"(!?)\[((?:[^\[\]]|\[[^\]]*\])*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_LINK = re.compile(r"<a\s[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", re.I | re.S)
TAG = re.compile(r"<[^>]+>")


def clean(s):
    s = TAG.sub("", s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"[*_`]+", "", s)
    s = re.sub(r":[a-z0-9_+-]+:", "", s)  # emoji shortcodes
    s = s.replace("&amp;", "&").replace("&nbsp;", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip(" -–—:|•·\t")


def clean_heading(s):
    s = clean(s)
    s = re.sub(r"^[^\w(]+", "", s, flags=re.U)  # leading emoji or symbols
    s = re.sub(r"[^\w)?!.]+$", "", s, flags=re.U)
    return s.strip()


def domain_of(url):
    host = urllib.parse.urlsplit(url).netloc.lower().split("@")[-1].split(":")[0]
    return host[4:] if host.startswith("www.") else host


def keep_link(url, name):
    if not re.match(r"https?://", url, re.I):
        return False
    host = domain_of(url)
    if not host or host in SKIP_HOSTS or host.endswith("shields.io"):
        return False
    if re.search(r"\.(png|jpe?g|gif|svg|webp)(\?|$)", url, re.I):
        return False
    if host == "github.com":
        parts = [p for p in urllib.parse.urlsplit(url).path.split("/") if p]
        if len(parts) < 2:  # profiles (contributors)
            return False
        if len(parts) > 2 and parts[2] in ("graphs", "pulls", "issues", "contributors", "stargazers",
                                            "network", "compare", "fork"):
            return False
    if not name or name.lower().strip(" .!") in GENERIC_NAMES:
        return False
    return True


def parse_file(path, repo):
    rows = []
    stack = []  # (level, title)
    in_code = False
    own = "github.com/" + repo.lower()
    para = ""  # first paragraph under the current heading (description for key-value tool tables)
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        level = None
        m = HEADING.match(line)
        if m:
            level, title = len(m.group(1)), m.group(2)
        else:
            m = HTML_HEADING.match(line)
            if m:
                level, title = int(m.group(1)), m.group(2)
            else:
                b = BOLD_HEADING.match(line)
                if b:
                    level, title = 7, b.group(1)
        if level is not None:
            title = clean_heading(title)
            if title:
                title = SECTION_OVERRIDES.get((repo, title), title)
                stack = [(l, t) for l, t in stack if l < level]
                stack.append((level, title))
                para = ""
            continue
        st = line.strip()
        if st and not para and not st.startswith(("|", "!", "<", "-", "*")):
            para = clean(st)
        # Skip navigation and boilerplate sections; a wrapper heading such as "Table of Content" above
        # real categories is dropped from the path instead.
        if stack and SKIP_SECTIONS.match(stack[-1][1]):
            continue
        titles = [t for _, t in stack if not SKIP_SECTIONS.match(t)]
        # The single top-level heading is the list title, not a category.
        if stack and stack[0][0] == 1 and sum(1 for l, _ in stack if l == 1) == 1 and titles:
            section_titles = titles[1:]
        else:
            section_titles = titles
        if not section_titles:
            continue
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            label = clean(cells[0]).lower() if cells else ""
            if label in KV_LABELS:
                continue
            if label == "url" and len(cells) > 1 and len(section_titles) > 1:
                bu = BARE_URL.search(cells[1])
                if bu:
                    url = bu.group(0)
                    rows.append({
                        "name": section_titles[-1],
                        "url": url,
                        "domain": domain_of(url),
                        "source_list": repo,
                        "source_section": " > ".join(section_titles[:-1]),
                        "description": para[:300],
                    })
                continue
        links = []
        for mm in MD_LINK.finditer(line):
            if not mm.group(1):
                links.append((mm.start(), mm.end(), clean(mm.group(2)), mm.group(3)))
        for mm in HTML_LINK.finditer(line):
            links.append((mm.start(), mm.end(), clean(mm.group(2)), mm.group(1)))
        if not links:
            continue
        links.sort()
        stripped = line.strip()
        is_table = stripped.startswith("|")
        first_kept = False
        for i, (s, e, name, url) in enumerate(links):
            # In list items and paragraphs, only the first link is the entry; later links are usually
            # authors or sources. In tables each linked cell can be an entry.
            if first_kept and not is_table:
                break
            if not keep_link(url, name):
                continue
            if (own + "/") in url.lower() or url.lower().rstrip("/").endswith(own):
                continue  # the list's own files and anchors
            if not is_table and s > 0 and not re.match(r"^\s*([-*+]|\d+\.)?\s*$", TAG.sub("", line[:s])):
                # Link sits mid-sentence: only keep it when the line is a short list item.
                if not re.match(r"^([-*+]|\d+\.)\s", stripped):
                    continue
            first_kept = True
            if is_table:
                cell_end = line.find("|", e)
                desc = clean(line[e:cell_end if cell_end > 0 else len(line)])
                if not desc:
                    nxt = line.find("|", cell_end + 1) if cell_end > 0 else -1
                    desc = clean(line[cell_end + 1:nxt]) if nxt > 0 else ""
            else:
                desc = clean(line[e:])
            desc = desc.strip(" -–—:|,.")
            if not re.search(r"[A-Za-z]{2}", desc):
                desc = ""
            rows.append({
                "name": name[:150],
                "url": url.strip(),
                "domain": domain_of(url),
                "source_list": repo,
                "source_section": " > ".join(section_titles),
                "description": desc[:300],
            })
    return rows


def norm_name(n):
    return re.sub(r"[^a-z0-9]+", "", n.lower())


def tool_key(row):
    dom = row["domain"]
    if dom == "github.com":
        parts = [p for p in urllib.parse.urlsplit(row["url"]).path.split("/") if p][:2]
        dom = "github.com/" + "/".join(parts).lower()
    return dom


def parse():
    with open(LICENSES, encoding="utf-8") as f:
        licenses = json.load(f)
    all_rows = []
    parsed = []
    for repo, _, _ in LISTS:
        path = os.path.join(RAW_DIR, repo.replace("/", "__") + ".md")
        if not os.path.exists(path):
            continue
        rows = parse_file(path, repo)
        for r in rows:
            r["license"] = licenses.get(repo, "")
        parsed.append((repo, len(rows)))
        all_rows.extend(rows)

    # Dedupe on domain plus name (GitHub entries use the repo path as their domain key).
    merged = {}
    order = []
    for r in all_rows:
        key = (tool_key(r), norm_name(r["name"]))
        if key not in merged:
            merged[key] = dict(r, also_in=[], lists={r["source_list"]})
            order.append(key)
        else:
            m = merged[key]
            if r["source_list"] not in m["lists"]:
                m["lists"].add(r["source_list"])
                m["also_in"].append(r["source_list"])
            if not m["description"] and r["description"]:
                m["description"] = r["description"]
    entries = []
    for k in order:
        m = merged[k]
        m["list_count"] = len(m["lists"])
        entries.append(m)
    entries.sort(key=lambda m: (-m["list_count"], m["domain"], m["name"].lower()))

    fields = ["name", "url", "domain", "source_list", "source_section", "description", "license",
              "also_in", "list_count"]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for m in entries:
            w.writerow(dict(m, also_in=";".join(m["also_in"])))

    # Section frequencies by leaf heading.
    sec_lists = defaultdict(set)
    sec_entries = Counter()
    sec_display = {}
    for r in all_rows:
        leaf = r["source_section"].split(" > ")[-1]
        k = leaf.lower()
        sec_display.setdefault(k, leaf)
        sec_lists[k].add(r["source_list"])
        sec_entries[k] += 1
    sections = sorted(sec_entries, key=lambda k: (-len(sec_lists[k]), -sec_entries[k], k))
    with open(OUT_SECTIONS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["heading", "list_count", "entry_count"])
        for k in sections:
            w.writerow([sec_display[k], len(sec_lists[k]), sec_entries[k]])

    # Most-listed tools: group home-page links by domain, so one tool under several names counts once.
    by_tool = defaultdict(lambda: {"lists": set(), "names": Counter()})
    for r in all_rows:
        dom = tool_key(r)
        path = urllib.parse.urlsplit(r["url"]).path.strip("/")
        if dom in PLATFORM_HOSTS:
            continue
        if dom.startswith("github.com/") or "/" not in path:
            by_tool[dom]["lists"].add(r["source_list"])
            by_tool[dom]["names"][r["name"]] += 1
    top_tools = sorted(by_tool.items(), key=lambda kv: (-len(kv[1]["lists"]), kv[0]))[:30]

    seed_hits = {}
    for s in LINK_SEEDS:
        hits = [r for r in all_rows if r["domain"] == s or r["domain"].endswith("." + s)]
        seed_hits[s] = sorted({r["source_list"] for r in hits})

    out = []
    out.append("# GitHub awesome lists: Useful links inventory")
    out.append("")
    out.append("Pulled 2026-10-08 from raw.githubusercontent.com. Rerun with "
               "`python -I research/seo/tools/github_lists.py all` from the project root.")
    out.append("")
    out.append("- Lists parsed: %d" % len(parsed))
    out.append("- Link rows before dedupe: %d" % len(all_rows))
    out.append("- Unique entries (domain plus name): %d" % len(entries))
    out.append("- Entries in two or more lists: %d" % sum(1 for m in entries if m["list_count"] > 1))
    out.append("")
    out.append("Files: `inventory-links-github.csv` (entries), `inventory-links-github-sections.csv` "
               "(heading frequencies), `github-lists/raw/` (the READMEs as pulled), "
               "`github-lists/licenses.json`.")
    out.append("")
    out.append("## Lists")
    out.append("")
    out.append("| List | License | Link rows |")
    out.append("|---|---|---|")
    done = dict(parsed)
    for repo, n in parsed:
        out.append("| [%s](https://github.com/%s) | %s | %d |" % (repo, repo, licenses.get(repo, ""), n))
    for repo, lic in licenses.items():
        if repo not in done:
            out.append("| %s | %s | 0 |" % (repo, lic))
    out.append("")
    out.append("## The 30 most-listed tools")
    out.append("")
    out.append("Grouped by domain over home-page links only, so one tool listed under different names counts once.")
    out.append("")
    out.append("| # | Tool | Domain | Lists |")
    out.append("|---|---|---|---|")
    for i, (dom, v) in enumerate(top_tools, 1):
        out.append("| %d | %s | %s | %d |" % (i, v["names"].most_common(1)[0][0], dom, len(v["lists"])))
    out.append("")
    out.append("## The 40 most common section headings")
    out.append("")
    out.append("Leaf heading of each link, case-folded; sorted by the number of lists that use it, then by "
               "entries. Full table in `inventory-links-github-sections.csv`.")
    out.append("")
    out.append("| # | Heading | Lists | Entries |")
    out.append("|---|---|---|---|")
    for i, k in enumerate(sections[:40], 1):
        out.append("| %d | %s | %d | %d |" % (i, sec_display[k], len(sec_lists[k]), sec_entries[k]))
    out.append("")
    out.append("## Seed Links directories listed as entries")
    out.append("")
    for s in LINK_SEEDS:
        out.append("- %s: %s" % (s, ", ".join(seed_hits[s]) if seed_hits[s] else "not listed"))
    out.append("")
    out.append("## Notes")
    out.append("")
    out.append("- goabstract/Awesome-Design-Tools serves a README identical to LisaDziuba/Awesome-Design-Tools, "
               "so only the latter is parsed.")
    out.append("- Aghoreshwar/Awesome-Customer-Analytics came up in the analytics search but is a churn-model "
               "project, not a list; domenicosolazzo/awesome-okr replaced it. ElizaLo/Product-Management-and-Leadership "
               "was looked at and left out (interview preparation, few tools).")
    out.append("- Not found (404 on main and master): BrunoLopes/awesome-ux, kfischer-okarin/awesome-ux-research, "
               "chrisdiana/awesome-ux, tipoqueno/UX-Collection. batoreh/awesome-ux stands in as the UX collection.")
    out.append("- GitHub repository search hit the unauthenticated rate limit after eight queries; the list set "
               "was chosen from those results (agile, growth, user research, customer analytics, design systems, "
               "product design).")
    out.append("- In a list item only the first link counts as the entry; later links in the same item (authors, "
               "sources) are dropped. In tables each linked cell counts. Contents, contributing, license and "
               "similar sections are skipped, as are badges, images, profiles and links into the list's own repo.")
    out.append("- Many rows are articles, books and talks rather than tools (the product management lists are "
               "mostly reading lists). The most-listed table counts home-page links only for that reason.")
    out.append("- Licenses come from the GitHub license API, or the README when the repo has no license file. "
               "\"none stated\" means no license was found: use those entries as facts (name and URL) only and "
               "write our own descriptions. Descriptions from CC0 and Unlicense lists can be reused freely; "
               "CC-BY and MIT need attribution.")
    out.append("")
    with open(OUT_SUMMARY, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print("lists", len(parsed), "rows", len(all_rows), "unique", len(entries))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("fetch", "all"):
        fetch()
    if cmd in ("parse", "all"):
        parse()
