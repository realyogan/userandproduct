# Run progress page

Open http://localhost/user-and-product/research/progress/ while a long run is going. The page reads
`status.json` in this folder every 10 seconds and shows the run title, a state pill, the started and
updated times, a one-line note, an overall progress bar (done steps over all steps) and the step list,
with the running step highlighted. Click the "Alarm off · click to turn on" button to arm the alarm ("Test" plays the chime once): when the run moves from
`running` to `finished` it plays a short chime (a lower tone on `failed`), flashes the tab title and
shows a "Done" banner. The sound setting is remembered in the browser.

**Any long run should write `status.json` as it goes.** Set a step to `running` when it starts and to
`done` (with a short note and a time) when it ends, refresh `note` and `updated` each time, and set
`state` to `finished` or `failed` at the end. Write the whole file each time (to a temp file, then
rename) so the page never reads half a file.

## Schema

```json
{
  "version": 1,
  "run_id": "v12-report",
  "title": "Intent re-score and report rebuild",
  "state": "running",
  "started": "2026-10-09T00:40+05:30",
  "updated": "2026-10-09T00:41+05:30",
  "note": "one line on what is happening now",
  "steps": [
    {"n": 1, "title": "Step title", "status": "pending", "note": "", "time": ""}
  ]
}
```

- `state`: `running` | `finished` | `failed`
- step `status`: `pending` | `running` | `done` | `failed` | `skipped`
- `started`, `updated`: ISO 8601 with an offset; a step's `time` is free text such as `00:52`.
- If the file is missing or unreadable, the page shows a "status.json unreachable" pill.
