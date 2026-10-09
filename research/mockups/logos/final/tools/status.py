"""Update research/progress/status.json for the logo-final-colours run.

Usage: python status.py init
       python status.py <step> <pending|running|done> "<note>" [finished]
"""
import json, os, sys, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'progress', 'status.json'))
TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
STEPS = ["Lockup from S5 and the fixed wordmark", "Ten themes and contrast", "Asset packs per theme",
         "Board, hub wiring, screenshots"]


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
        global STEPS
        run_id, title = "logo-final-colours", "Final logo: ten colour themes for S5"
        if len(argv) > 3:          # init <run_id> "<title>" "step 1|step 2|..."
            run_id, title, STEPS = argv[1], argv[2], argv[3].split('|')
        data = {"version": 1, "run_id": run_id,
                "title": title,
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
