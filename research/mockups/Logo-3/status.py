"""Write research/progress/status.json for run logo-3.  usage: python status.py <step n> <status> "<note>" [finished]"""
import datetime
import json
import os
import sys

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'progress', 'status.json')
TITLES = ["Source", "Clean master", "Color options", "Gradients", "Lockups", "Previews", "Board", "Checks"]
RUN = 'logo-3'
now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M+05:30')
try:
    d = json.load(open(P, encoding='utf-8'))
    assert d.get('run_id') == RUN
except Exception:
    d = {"version": 1, "run_id": RUN, "title": "Logo 3: color options and previews for the owner's mark",
         "state": "running", "started": now,
         "steps": [{"n": i + 1, "title": t, "status": "pending", "note": "", "time": ""} for i, t in enumerate(TITLES)]}
n, st, note = int(sys.argv[1]), sys.argv[2], sys.argv[3]
s = d['steps'][n - 1]
s['status'], s['note'], s['time'] = st, note, now[11:16]
d['updated'] = now
d['note'] = note
d['state'] = 'finished' if len(sys.argv) > 4 else 'running'
tmp = P + '.tmp'
json.dump(d, open(tmp, 'w', encoding='utf-8'), indent=2)
os.replace(tmp, P)
