"""Screenshots and layout checks for the home page mockup.

Run: python shots_home.py   (from option-1/build/; the page must be served at
http://localhost/user-and-product/research/mockups/option-1/)
Writes option-1/shots/home-<width>-<light|dark>.png (full page) for 375 and 1280, then prints:
horizontal overflow at each width from 375 to 1440, the ad units in each viewport-sized slice of the page,
and the mobile ad density (ad heights over page height at 375).
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "http://localhost/user-and-product/research/mockups/option-1/"
OUT = Path(__file__).resolve().parent.parent / "shots"   # option-1/shots/
OUT.mkdir(exist_ok=True)

ADS = """() => [...document.querySelectorAll('.ad')].filter(a => a.offsetParent)
  .map(a => { const r = a.getBoundingClientRect(); return [r.top + scrollY, r.height, r.width, a.dataset.ad]; })"""

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")  # the installed Chrome, headless
    for w in (375, 1280):
        for scheme in ("light", "dark"):
            pg = b.new_page(viewport={"width": w, "height": 800}, color_scheme=scheme)
            pg.goto(URL, wait_until="networkidle")
            # lazy images below the fold load only when near the viewport: load them all before the full-page shot
            pg.evaluate("() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
            pg.wait_for_function("() => [...document.images].every(i => i.complete)")
            pg.screenshot(path=str(OUT / f"home-{w}-{scheme}.png"), full_page=True)
            pg.close()
    print("overflow (scrollWidth - innerWidth):")
    for w in (375, 390, 414, 480, 600, 680, 768, 900, 1024, 1100, 1280, 1440):
        pg = b.new_page(viewport={"width": w, "height": 800})
        pg.goto(URL, wait_until="networkidle")
        over = pg.evaluate("() => document.documentElement.scrollWidth - innerWidth")
        cols = pg.evaluate("() => getComputedStyle(document.querySelector('.feed')).gridTemplateColumns.split(' ').length")
        cell = pg.evaluate("() => Math.round(document.querySelector('.feed .card').getBoundingClientRect().width)")
        ads = pg.evaluate(ADS)
        hgt = pg.evaluate("() => document.documentElement.scrollHeight")
        vh = 667 if w < 768 else 800
        worst = max(sum(1 for t, h, *_ in ads if t < y + vh and t + h > y) for y in range(0, hgt, 50))
        print(f"  {w}: overflow {over}px, feed {cols} col(s) of {cell}px, ads {[(a[3], round(a[2]), round(a[1])) for a in ads]},"
              f" most ads in one view {worst}")
        if w == 375:
            print(f"  mobile ad density: {sum(a[1] for a in ads):.0f} / {hgt} px = {100 * sum(a[1] for a in ads) / hgt:.1f}%")
        pg.close()
    b.close()
