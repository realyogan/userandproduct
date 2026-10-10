"""Screenshots and checks for the Books section mockup.

Run: python shots_books.py   (from option-1/build/; pages served at http://localhost/user-and-product/research/mockups/option-1/)
Writes option-1/shots/books-<page>-<width>-<light|dark>.png (full page) for 375 and 1280, then prints for each page:
horizontal overflow at 375, 768, 1280 and 1440, the h1 count, images without alt, requests to other hosts, internal
links that do not resolve, and sponsored links without the disclosure beside them.
"""
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

BASE = "http://localhost/user-and-product/research/mockups/option-1/"
PAGES = [("shelf", "sections/books.html"), ("topic", "books/product-management.html"), ("placeholder", "books/topic.html")]
OUT = Path(__file__).resolve().parent.parent / "shots"
OUT.mkdir(exist_ok=True)

CHECKS = """() => ({
  h1: document.querySelectorAll('h1').length,
  noAlt: [...document.images].filter(i => !i.hasAttribute('alt')).map(i => i.src),
  svgImg: [...document.querySelectorAll('svg[role=img]')].filter(s => !s.querySelector('title')).length,
  links: [...document.querySelectorAll('a[href]')].map(a => a.href),
  sponsored: [...document.querySelectorAll('a[rel~=sponsored]')].map(a => !!a.closest('.buy') && /commission/.test(a.closest('.buy').textContent)),
  tabStops: [...document.querySelectorAll('a[href],button,summary')].filter(e => e.offsetParent || e.getClientRects().length).length
})"""

with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome")
    for name, path in PAGES[:2]:
        for w in (375, 1280):
            for scheme in ("light", "dark"):
                pg = b.new_page(viewport={"width": w, "height": 800}, color_scheme=scheme)
                pg.goto(BASE + path, wait_until="networkidle")
                pg.evaluate("() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager')")
                pg.wait_for_function("() => [...document.images].every(i => i.complete)")
                pg.screenshot(path=str(OUT / f"books-{name}-{w}-{scheme}.png"), full_page=True)
                pg.close()
    ctx = b.new_context()
    for name, path in PAGES:
        print(f"== {name}: {path}")
        for w in (375, 768, 1280, 1440):
            pg = ctx.new_page()
            pg.set_viewport_size({"width": w, "height": 800})
            ext = []
            pg.on("request", lambda r: ext.append(r.url) if urlparse(r.url).hostname not in ("localhost",) and not r.url.startswith("data:") else None)
            resp = pg.goto(BASE + path, wait_until="networkidle")
            over = pg.evaluate("() => document.documentElement.scrollWidth - innerWidth")
            if w == 375:
                c = pg.evaluate(CHECKS)
                bad = []
                for href in sorted(set(c["links"])):
                    u = urlparse(href)
                    if u.hostname != "localhost":
                        continue
                    r = ctx.request.get(href.split("#")[0])
                    if r.status != 200:
                        bad.append((href, r.status))
                    frag = u.fragment
                    if frag and href.split("#")[0] == pg.url.split("#")[0] and not pg.evaluate(f"() => !!document.getElementById({frag!r})"):
                        bad.append((href, "no anchor"))
                print(f"  status {resp.status}; h1 {c['h1']}; img without alt {c['noAlt']}; svg img without title {c['svgImg']}; "
                      f"tab stops {c['tabStops']}; broken links {bad}; sponsored with disclosure {c['sponsored']}")
            print(f"  {w}: overflow {over}px; external requests {ext}")
            pg.close()
    b.close()
