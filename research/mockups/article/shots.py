"""Screenshots and layout checks for article variant A.

Run: python shots.py   (the page must be served at http://localhost/user-and-product/research/mockups/article/)
Writes shots/a-<width>x<height>-<light|dark>.png (the top 1200px of the page) for each viewport below and
prints, per viewport: horizontal overflow, the three column widths, the running-text measure, the lines of the
longest title in the compact list, the most ad units in one view, whether the sticky rails stop at the body end,
and the mobile ad density (ad heights over page height at 375).
"""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "http://localhost/user-and-product/research/mockups/article/article-a.html"
OUT = Path(__file__).resolve().parent / "shots"
OUT.mkdir(exist_ok=True)
VIEWPORTS = [(375, 812), (768, 1024), (1024, 768), (1280, 720), (1280, 800), (1366, 768),
             (1440, 900), (1536, 864), (1680, 1050), (1920, 1080)]

MEASURE = """() => {
  const w = el => el && el.offsetParent !== null ? Math.round(el.getBoundingClientRect().width) : 0;
  const titles = [...document.querySelectorAll('.rail-t')].filter(t => t.offsetParent);
  const lines = titles.map(t => Math.round(t.getBoundingClientRect().height / parseFloat(getComputedStyle(t).lineHeight)));
  const p = document.querySelector('.prose > p');
  // in-page units; the fixed anchor (phones only) is counted on its own as always in view
  const ads = [...document.querySelectorAll('.ad')].filter(a => a.offsetParent)
    .map(a => { const r = a.getBoundingClientRect(); return [r.top + scrollY, r.height, a.dataset.ad]; });
  return {over: document.documentElement.scrollWidth - innerWidth,
          left: w(document.querySelector('.side')), main: w(document.querySelector('.main')),
          rail: w(document.querySelector('.rail')), railTop: document.querySelector('.rail') && document.querySelector('.rail').offsetParent
            ? Math.round(document.querySelector('.rail').getBoundingClientRect().top - document.querySelector('.main').getBoundingClientRect().bottom) : null,
          text: w(p), ch: p ? Math.round(p.getBoundingClientRect().width / (parseFloat(getComputedStyle(p).fontSize) * 0.5)) : 0,
          lines, ads, h: document.documentElement.scrollHeight,
          anchor: getComputedStyle(document.querySelector('.anchor')).display !== 'none' ? 84 : 0,
          railInList: titles.length ? Math.round(titles[0].closest('.rail-list').getBoundingClientRect().width) : 0};
}"""

# scroll so the body's end sits mid-screen, then check the sticky blocks have not passed it
STICKY = """() => {
  const main = document.querySelector('.main'), side = document.querySelector('.side'), ad = document.querySelector('.rail__sticky');
  scrollTo({top: main.getBoundingClientRect().bottom + scrollY - innerHeight / 2, behavior: 'instant'});
  const mb = main.getBoundingClientRect().bottom, out = {};
  if (side && side.offsetParent) out.side = Math.round(side.getBoundingClientRect().bottom - mb);
  if (ad && ad.offsetParent && getComputedStyle(ad).position === 'sticky') out.ad = Math.round(ad.getBoundingClientRect().bottom - mb);
  return out;
}"""

rows = []
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")  # the installed Chrome, headless
    for vw, vh in VIEWPORTS:
        for scheme in ("light", "dark"):
            pg = b.new_page(viewport={"width": vw, "height": vh}, color_scheme=scheme)
            pg.goto(URL, wait_until="networkidle")
            pg.evaluate("() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
            pg.wait_for_function("() => [...document.images].every(i => i.complete)")
            pg.screenshot(path=str(OUT / f"a-{vw}x{vh}-{scheme}.png"), full_page=True,
                          clip={"x": 0, "y": 0, "width": vw, "height": 1200})
            if scheme == "light":
                m = pg.evaluate(MEASURE)
                m["sticky"] = pg.evaluate(STICKY)
                worst = max(sum(1 for t, h, _ in m["ads"] if t < y + vh and t + h > y) for y in range(0, m["h"], 50)) + (1 if m["anchor"] else 0)
                m["worst"] = worst
                m["vp"] = f"{vw}x{vh}"
                if vw == 375:
                    # the anchor is on screen the whole time it shows: count its share of the screen, not of the page
                    m["density"] = round(100 * sum(a[1] for a in m["ads"]) / m["h"], 1)
                    m["anchor_share"] = round(100 * m["anchor"] / vh, 1)
                del m["ads"]
                rows.append(m)
                print(json.dumps(m))
            pg.close()
    b.close()
