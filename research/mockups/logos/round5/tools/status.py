"""Update research/progress/status.json for the logos-round5 run.

Usage: python status.py init
       python status.py <step> <pending|running|done> "<note>" [finished]
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'progress', 'status.json'))
TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
STEPS = ["Read boards and inspiration", "Tripod derivatives Q1 to Q3", "Tripod derivatives Q4 to Q6",
         "Weighted ring Q7 to Q10", "Originality checks and reductions", "Board, strips, screenshots"]


def now():
    return datetime.datetime.now(TZ)


def write(data):
    tmp = PATH + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    os.replace(tmp, PATH)


def main(argv):
    t = now()
    if argv[0] == 'init':
        data = {"version": 1, "run_id": "logos-round5",
                "title": "Logo concepts, round 5: tripod derivatives and the weighted ring",
                "state": "running", "started": t.strftime('%Y-%m-%dT%H:%M+05:30'),
                "updated": t.strftime('%Y-%m-%dT%H:%M+05:30'), "note": "Starting",
                "steps": [{"n": i + 1, "title": s, "status": "pending", "note": "", "time": ""}
                          for i, s in enumerate(STEPS)]}
        write(data)
        return
    with open(PATH, encoding='utf-8') as f:
        data = json.load(f)
    n, status, note = int(argv[0]), argv[1], argv[2]
    step = data['steps'][n - 1]
    step['status'] = status
    step['note'] = note
    step['time'] = t.strftime('%H:%M')
    data['note'] = note
    data['updated'] = t.strftime('%Y-%m-%dT%H:%M+05:30')
    if len(argv) > 3 and argv[3] == 'finished':
        data['state'] = 'finished'
    write(data)


if __name__ == '__main__':
    main(sys.argv[1:])
