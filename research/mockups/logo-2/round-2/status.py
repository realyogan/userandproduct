"""Write research/progress/status.json for run logo-2-round-2.  usage: python status.py <step n> <status> "<note>" [finished]"""
import json, sys, os, datetime
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'progress', 'status.json')
TITLES = ["Brief", "Letter studies", "Draw", "Board", "Sizes", "Checks"]
now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M+05:30')
try:
    d = json.load(open(P, encoding='utf-8'))
    assert d.get('run_id') == 'logo-2-round-2'
except Exception:
    d = {"version": 1, "run_id": "logo-2-round-2", "title": "Logo exploration 2, round 2: ten letterform marks from U, D and P",
         "state": "running", "started": now,
         "steps": [{"n": i + 1, "title": t, "status": "pending", "note": "", "time": ""} for i, t in enumerate(TITLES)]}
n, st, note = int(sys.argv[1]), sys.argv[2], sys.argv[3]
s = d['steps'][n - 1]; s['status'] = st; s['note'] = note; s['time'] = now[11:16]
d['updated'] = now; d['note'] = note
d['state'] = 'finished' if len(sys.argv) > 4 else 'running'
tmp = P + '.tmp'; json.dump(d, open(tmp, 'w', encoding='utf-8'), indent=2); os.replace(tmp, P)
