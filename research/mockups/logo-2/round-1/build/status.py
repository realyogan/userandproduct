"""Write research/progress/status.json for the logo-2 round-1 run. Usage: status.py <step n> <status> <note>."""
import json, os, sys, datetime
P = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'progress', 'status.json')
TITLES = ['Brief', 'Ideas', 'Draw', 'Board', 'Sizes', 'Checks']
def now():
    return datetime.datetime.now().astimezone().strftime('%Y-%m-%dT%H:%M%z')[:-2] + ':' + datetime.datetime.now().astimezone().strftime('%z')[-2:]
def main(n, status, note):
    try:
        d = json.load(open(P, encoding='utf8'))
        if d.get('run_id') != 'logo-2-round-1':
            raise ValueError
    except Exception:
        d = {'version': 1, 'run_id': 'logo-2-round-1', 'title': 'Logo exploration 2, round 1: twelve marks with mass and a fold',
             'state': 'running', 'started': now(), 'steps': [{'n': i + 1, 'title': t, 'status': 'pending', 'note': '', 'time': ''} for i, t in enumerate(TITLES)]}
    if n == 'finished':
        d['state'] = 'finished'; d['note'] = note
    else:
        s = d['steps'][int(n) - 1]; s['status'] = status; s['note'] = note; s['time'] = datetime.datetime.now().strftime('%H:%M')
        d['note'] = note; d['state'] = 'running'
    d['updated'] = now()
    tmp = P + '.tmp'
    json.dump(d, open(tmp, 'w', encoding='utf8'), indent=2); os.replace(tmp, P)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
