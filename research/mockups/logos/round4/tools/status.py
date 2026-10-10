"""Update research/progress/status.json for the logos-round4 run.

Usage: python status.py init
       python status.py <step> <pending|running|done> "<note>" [finished]
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'progress', 'status.json'))
TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
STEPS = ["Read the three boards and the brief", "Nameplates and monograms (P1 to P4)", "Abstract symbols (P5 to P7)",
         "Negative-space marks and the tenth (P8 to P10)", "Originality checks", "Board, in-context strips, screenshots"]


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
        data = {"version": 1, "run_id": "logos-round4",
                "title": "Logo concepts, round 4: mark plus name, institution not startup",
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
