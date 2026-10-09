"""The ten colour themes for the S5 lockup, with WCAG contrast checks.

Each theme: light mode (large tiles, small tiles, wordmark, page background) and dark mode (the same
roles on a near-black), plus one link accent per mode. 'odd' optionally recolours one small tile
(T08: the single coloured tile). Ratios are WCAG 2 relative-luminance contrast.
"""


def lum(hexc):
    h = hexc.lstrip('#')
    out = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = out
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


WHITE, CREAM = '#FFFFFF', '#F4EFE3'
T = []


def theme(key, slug, name, L, D, feel, rec=None, odd=None):
    T.append(dict(key=key, slug=slug, name=name, L=L, D=D, feel=feel, rec=rec, odd=odd))


# L / D: big = large tiles, small = small tiles (one colour now: no two-tone marks), word = wordmark,
# bg = page, link = accent. Order: press red first, then the blues from darkest to brightest (light shade).
BLACK, OFF, NEAR = '#0B0B0C', '#F1EEE7', '#0F1115'


def blue(key, slug, name, light, dark, feel, rec=None):
    theme(key, slug, name,
          dict(big=light, small=light, word=BLACK, bg=WHITE, link=light),
          dict(big=dark, small=dark, word=OFF, bg=NEAR, link=dark), feel, rec)


theme('T01', 't01-press-red', 'Press red',
      dict(big='#B3141C', small='#B3141C', word='#141414', bg=WHITE, link='#B3141C'),
      dict(big='#F0676C', small='#F0676C', word='#F1EEE7', bg='#121111', link='#F38A8E'),
      'Warm and editorial. A printing red with a black name: loud and newsy, close to the Financial Times '
      'or a design annual. Kept exactly as it was; also the natural secondary accent for any of the blues.')
blue('T02', 't02-midnight', 'Midnight', '#151C36', '#9EABD6',
     'Cool and editorial. A near-black blue that reads as black at a glance and blue up close: the quietest '
     'scheme, close to a law firm or a private bank. Next to red: red takes over completely, so red would have '
     'to stay tiny.')
blue('T03', 't03-prussian', 'Prussian blue', '#0B3150', '#7DB0D8',
     'Cool and historic. The old pigment blue, deep with a green undertone: scholarly, like an atlas or a '
     'museum. Next to red: a classic print pairing, calm and serious.')
blue('T04', 't04-navy', 'Navy', '#1B2C66', '#98ABE6',
     'Cool and institutional. A true navy, a touch of violet: established, trustworthy, close to a business '
     'school or a long-running journal. Next to red: the oldest editorial pairing there is; red works as a '
     'small accent without fighting.',
     rec='The safest authority. Navy is dark enough to feel as heavy as black (13.1:1 on white), still clearly '
         'blue, and its dark tint (#98ABE6) stays crisp on near-black. It sits naturally beside the black name, '
         'and it takes press red as a later secondary accent better than any other blue here.')
blue('T05', 't05-sapphire', 'Sapphire', '#0F3B8C', '#7C9CF5',
     'Cool and rich. A saturated jewel blue, deeper than cobalt: confident and premium, close to a financial '
     'brand. Next to red: strong, slightly patriotic; keep red small.')
blue('T06', 't06-petrol', 'Petrol blue', '#0D4D5E', '#6CBCCB',
     'Cool and technical, with a teal lean: the deep petrol blue of a Mercedes paint chip. Precise and '
     'engineered, the rarest hue in UX and business media. Next to red: near-complementary, so the pair is '
     'lively but refined.',
     rec='The most ownable blue. No UX or product title uses this teal-leaning petrol, so it becomes ours fast, '
         'and it still reads as blue, heavy and precise (9.4:1 on white). The dark tint (#6CBCCB) is the '
         'clearest of all on near-black. Red beside it is almost complementary: a refined accent, never a clash.')
blue('T07', 't07-cobalt', 'Cobalt', '#0047AB', '#5FA8FF',
     'Cool and vivid. A pure, saturated pigment blue with no violet: clear and modern, close to a tech '
     'publisher. Next to red: very loud; the two primaries compete.')
blue('T08', 't08-signal-blue', 'Signal blue', '#2B46A0', '#8EA2FF',
     'Cool and technical. The signal blue re-tuned: the light shade is deeper and less saturated than the old '
     '#1F3FBF (tested against #2A45B0, #2D4AA6, #2F4D9C and #34509A; #2B46A0 held the 16px favicon best), the '
     'dark shade is the one the owner liked. Next to red: balanced, but use red sparingly.')
blue('T09', 't09-steel', 'Steel blue', '#3B5D7E', '#A0BAD4',
     'Cool and understated. A grey blue: calm, technical, close to an engineering consultancy. The least '
     'saturated; it can read as grey at small sizes. Next to red: red pops hard against it.')
blue('T10', 't10-royal', 'Royal blue', '#3A5BD9', '#A9BCFF',
     'Cool and bright. The lightest, most energetic blue: friendly and product-like, close to a SaaS brand. '
     'Mark contrast is 5.7:1, fine for a mark but the lightest of the ten. Next to red: very loud.')


def mark_colors(t, mode):
    """Distinct mark colours for one mode (for the contrast check)."""
    c = t[mode]
    cols = [c['big'], c['small']]
    if t['odd']:
        cols.append(t['odd'][mode])
    out = []
    for x in cols:
        if x not in out:
            out.append(x)
    return out


def checks(t):
    res = {}
    for mode in ('L', 'D'):
        c = t[mode]
        res[mode] = dict(word=ratio(c['word'], c['bg']),
                         marks=[(x, ratio(x, c['bg'])) for x in mark_colors(t, mode)],
                         link=ratio(c['link'], c['bg']))
    return res


def ok(t):
    r = checks(t)
    good = True
    for mode in ('L', 'D'):
        good &= r[mode]['word'] >= 7 and all(v >= 3 for _, v in r[mode]['marks']) and r[mode]['link'] >= 4.5
    return good


if __name__ == '__main__':
    for t in T:
        r = checks(t)
        line = f"{t['key']} {t['name']:<26}"
        for mode in ('L', 'D'):
            m = ' '.join(f'{x}:{v:.1f}' for x, v in r[mode]['marks'])
            line += f" | {mode} word {r[mode]['word']:.1f} mark {m} link {r[mode]['link']:.1f}"
        print(line, 'OK' if ok(t) else 'FAIL')
