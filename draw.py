"""Paint the Tuesday 24 November 2026 world-news page into entry.png.

Pillow only. Everything is laid out on a 1024 x 1024 grid, drawn at 2x and
scaled down once at the end so small type stays crisp. No randomness, no clock,
no network: the same stories.py always gives the same bytes.
"""
from PIL import Image, ImageDraw, ImageFont

from stories import LEADS, REGIONS, TIMELINE, TIMELINE_NOTE, DATE_CHECK, NUMBERS

S = 2                      # supersample factor
W = H = 1024
FONT_DIR = "/usr/share/fonts/truetype/noto/"

PAPER = (247, 244, 237)
INK = (22, 24, 29)
GREY = (104, 109, 118)
SOFT = (226, 222, 212)
CARD = (255, 255, 255)
GOLD = (242, 193, 78)
RED = (179, 38, 30)

REGION_COLOUR = {
    "ASIA": (205, 64, 80),
    "EUROPE": (40, 104, 180),
    "MIDDLE EAST": (214, 132, 22),
    "AFRICA": (52, 145, 84),
    "OCEANIA": (16, 150, 156),
    "NORTH AMERICA": (118, 76, 176),
    "LATIN AMERICA": (140, 92, 60),
}
LABEL_COLOUR = {
    "CONFIRMED": (30, 125, 78),
    "OFFICIAL": (36, 87, 166),
    "REPORTED": (98, 102, 112),
    "SCHEDULED": (181, 101, 29),
}

_fonts = {}


def F(style, size):
    key = (style, size)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(FONT_DIR + f"NotoSans-{style}.ttf", round(size * S))
    return _fonts[key]


img = Image.new("RGB", (W * S, H * S), PAPER)
d = ImageDraw.Draw(img)


def P(*v):
    return [round(x * S) for x in v]


def width(s, font):
    return d.textlength(s, font=font) / S


def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x * S, y * S), s, font=font, fill=fill, anchor=anchor)


def box(x0, y0, x1, y1, fill=None, outline=None, w=1, r=0):
    if r:
        d.rounded_rectangle(P(x0, y0, x1, y1), radius=r * S, fill=fill, outline=outline, width=round(w * S))
    else:
        d.rectangle(P(x0, y0, x1, y1), fill=fill, outline=outline, width=round(w * S))


def wrap(s, font, maxw):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if width(trial, font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(x, y, s, font, maxw, lh, fill=INK, max_lines=9):
    lines = wrap(s, font, maxw)
    if len(lines) > max_lines:
        print("WARN overflow:", s[:50])
        lines = lines[:max_lines]
    for i, ln in enumerate(lines):
        text(x, y + i * lh, ln, font, fill)
    return y + len(lines) * lh


def pin(cx, cy, n, colour, r=7.0):
    d.ellipse(P(cx - r, cy - r, cx + r, cy + r), fill=colour, outline=CARD, width=round(1.2 * S))
    text(cx, cy + 0.3, str(n), F("Bold", 7.5 if n < 10 else 7), CARD, anchor="mm")


def chip(x, y, label, src):
    f = F("CondensedBold", 8)
    tw = width(label, f)
    box(x, y, x + tw + 8, y + 11, fill=LABEL_COLOUR[label], r=2)
    text(x + 4, y + 5.6, label, f, CARD, anchor="lm")
    text(x + tw + 12, y + 5.6, src, F("Condensed", 8.5), GREY, anchor="lm")


# ---------------------------------------------------------------- header
box(0, 0, W, 92, fill=INK)
text(16, 9, "TUESDAY", F("Bold", 17), GOLD)
text(13, 26, "24 NOVEMBER 2026", F("Black", 50), CARD)
text(1008, 12, "THE WORLD IN ONE DAY", F("Bold", 21), CARD, anchor="ra")
text(1008, 42, "30 stories from 7 regions, every one dated 24 Nov", F("Regular", 13.5), (205, 209, 216), anchor="ra")
text(1008, 63, "Numbered pins on the map  ·  times in UTC  ·  certainty label on each story",
     F("Regular", 11), (170, 175, 184), anchor="ra")

# ---------------------------------------------------------------- lead cards
CW, GAP, LY0, LY1 = 245, 8.67, 98, 246
for i, s in enumerate(LEADS):
    x = 10 + i * (CW + GAP)
    col = REGION_COLOUR[s["region"]]
    box(x, LY0, x + CW, LY1, fill=CARD, outline=SOFT)
    box(x, LY0, x + 5, LY1, fill=col)
    pin(x + 20, LY0 + 16, s["n"], col, 8)
    big_f = F("Black", 30)
    text(x + 33, LY0 + 0, s["big"], big_f, col)
    text(x + 37 + width(s["big"], big_f), LY0 + 12, s["unit"], F("Bold", 9.5), GREY)
    text(x + CW - 6, LY0 + 6, s["region"], F("Bold", 8), col, anchor="ra")
    y = para(x + 12, LY0 + 44, s["head"], F("Bold", 13.5), CW - 20, 16.5, max_lines=2)
    para(x + 12, y + 2, s["detail"], F("Regular", 10), CW - 20, 12.5, (55, 58, 66), max_lines=4)
    chip(x + 12, LY1 - 16, s["label"], s["src"])

# ---------------------------------------------------------------- map
MX0, MY0, MX1, MY1 = 10, 252, 610, 480
LON0, LON1, LAT0, LAT1 = -175.0, 180.0, 72.0, -63.0


def proj(lon, lat):
    return (MX0 + (lon - LON0) / (LON1 - LON0) * (MX1 - MX0),
            MY0 + (LAT0 - lat) / (LAT0 - LAT1) * (MY1 - MY0))


LAND = [
    # North America
    [(-165, 65), (-140, 70), (-100, 71), (-80, 64), (-62, 58), (-55, 50), (-67, 45), (-76, 36),
     (-81, 26), (-82, 30), (-90, 29), (-97, 26), (-97, 20), (-90, 16), (-83, 9), (-78, 8),
     (-86, 14), (-105, 20), (-112, 29), (-117, 33), (-124, 40), (-124, 48), (-135, 58),
     (-150, 60), (-165, 62)],
    # Greenland (clipped at the top edge)
    [(-55, 60), (-42, 60), (-22, 70), (-20, 76), (-60, 76), (-68, 72)],
    # South America
    [(-78, 8), (-72, 12), (-60, 10), (-50, 0), (-35, -6), (-39, -14), (-41, -22), (-48, -26),
     (-58, -35), (-62, -40), (-68, -52), (-74, -50), (-72, -35), (-71, -18), (-76, -14),
     (-81, -5), (-80, 0)],
    # Eurasia
    [(-10, 36), (-9, 43), (-1, 46), (-5, 48), (2, 51), (8, 54), (10, 57), (5, 62), (12, 66),
     (20, 70), (30, 70), (40, 67), (60, 70), (80, 73), (105, 76), (140, 72), (170, 70),
     (180, 66), (165, 60), (155, 55), (142, 47), (135, 43), (129, 35), (121, 31), (122, 25),
     (109, 21), (106, 10), (100, 13), (103, 1), (98, 8), (98, 16), (92, 22), (88, 22), (80, 15),
     (77, 8), (72, 20), (67, 25), (57, 25), (56, 27), (50, 30), (48, 29), (56, 24), (59, 22),
     (52, 16), (43, 12), (35, 28), (35, 33), (36, 37), (28, 41), (23, 38), (20, 40), (15, 38),
     (12, 44), (8, 44), (3, 43), (-1, 37)],
    # Africa
    [(-17, 21), (-6, 36), (10, 37), (20, 32), (32, 31), (34, 28), (43, 12), (51, 12), (40, -2),
     (39, -15), (35, -24), (32, -29), (20, -35), (18, -30), (12, -17), (13, -6), (9, 4),
     (-8, 4), (-17, 14)],
    # Australia
    [(114, -22), (122, -18), (130, -12), (137, -12), (142, -11), (146, -19), (153, -26),
     (150, -37), (141, -38), (131, -31), (115, -34)],
    # Britain and Ireland, Japan, Madagascar, New Zealand, islands of Southeast Asia
    [(-5, 50), (1, 51), (0, 54), (-3, 58), (-6, 56)],
    [(-10, 52), (-6, 52), (-6, 55), (-10, 54)],
    [(130, 31), (135, 34), (140, 35), (142, 40), (141, 45), (140, 42), (137, 37), (132, 34)],
    [(44, -25), (47, -25), (50, -15), (49, -12), (44, -17)],
    [(172, -41), (174, -37), (178, -38), (174, -42), (168, -46), (167, -45)],
    [(95, 5), (104, -4), (106, -6), (101, -2)],
    [(109, 1), (117, 7), (119, 1), (116, -4), (110, -3)],
    [(105, -7), (114, -7), (114, -9), (106, -8)],
    [(131, -1), (141, -3), (150, -10), (141, -9), (137, -5)],
    [(119, 0), (125, 1), (121, -5)],
    [(120, 18), (122, 18), (126, 7), (122, 7)],
]
box(MX0, MY0, MX1, MY1, fill=(220, 231, 239))
for lat in (60, 30, 0, -30):
    y = proj(0, lat)[1]
    d.line(P(MX0, y, MX1, y), fill=(205, 218, 228), width=S)
for poly in LAND:
    d.polygon([tuple(round(c * S) for c in proj(lo, la)) for lo, la in poly], fill=(200, 203, 192))
y_eq = proj(0, 0)[1]
text(MX1 - 4, y_eq - 10, "EQUATOR", F("Regular", 6.5), (150, 165, 178), anchor="ra")
box(MX0, MY0, MX1, MY1, outline=SOFT)
box(MX0, MY0, MX0 + 132, MY0 + 15, fill=INK)
text(MX0 + 5, MY0 + 7.5, "WHERE IT HAPPENED", F("Bold", 8.5), CARD, anchor="lm")

pins = []
for s in LEADS:
    pins.append([s["n"], REGION_COLOUR[s["region"]], *proj(s["lon"], s["lat"])])
for region, items in REGIONS:
    for s in items:
        pins.append([s["n"], REGION_COLOUR[region], *proj(s["lon"], s["lat"])])
spots = [(p[2], p[3]) for p in pins]
pos = [[p[2], p[3]] for p in pins]
for _ in range(120):                       # push overlapping pins apart, deterministically
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            dx, dy = pos[j][0] - pos[i][0], pos[j][1] - pos[i][1]
            dist = (dx * dx + dy * dy) ** 0.5
            if dist < 15.5:
                if dist < 0.01:
                    dx, dy, dist = 1.0, 0.0, 1.0
                push = (15.5 - dist) / 2
                ux, uy = dx / dist, dy / dist
                pos[i][0] -= ux * push; pos[i][1] -= uy * push
                pos[j][0] += ux * push; pos[j][1] += uy * push
    for p in pos:
        p[0] = min(max(p[0], MX0 + 8), MX1 - 8)
        p[1] = min(max(p[1], MY0 + 22), MY1 - 8)
for (sx, sy), (px, py) in zip(spots, pos):
    if abs(sx - px) + abs(sy - py) > 2:
        d.line(P(sx, sy, px, py), fill=(90, 94, 100), width=S)
    d.ellipse(P(sx - 1.6, sy - 1.6, sx + 1.6, sy + 1.6), fill=INK)
for (n, col, _, _), (px, py) in zip(pins, pos):
    pin(px, py, n, col)

# region key under the map title
kx = MX0 + 6
ky = MY1 - 14
for name, col in REGION_COLOUR.items():
    label = name.title()
    box(kx, ky + 2, kx + 7, ky + 9, fill=col)
    text(kx + 10, ky + 5.5, label, F("Condensed", 8), INK, anchor="lm")
    kx += 16 + width(label, F("Condensed", 8))

# ---------------------------------------------------------------- date check
RX0, RX1 = 618, 1014
box(RX0, 252, RX1, 388, fill=CARD, outline=RED, w=1.6)
box(RX0, 252, RX1, 270, fill=RED)
text(RX0 + 7, 261, "DATE CHECK", F("Black", 10.5), CARD, anchor="lm")
text(RX1 - 7, 261, "true stories, wrong day: kept OFF this page", F("Regular", 9), CARD, anchor="rm")
for i, (story, when) in enumerate(DATE_CHECK):
    y = 275 + i * 15.6
    f = F("Condensed", 10.5)
    text(RX0 + 8, y, story, f, (80, 84, 92))
    sw = width(story, f)
    d.line(P(RX0 + 8, y + 8, RX0 + 8 + sw, y + 8), fill=(150, 60, 55), width=S)
    text(RX1 - 8, y, when, F("CondensedBold", 10.5), RED, anchor="ra")

# ---------------------------------------------------------------- numbers + label key
text(RX0, 394, "BY THE NUMBERS, 24 NOV", F("Bold", 8.5), GREY)
tw = (RX1 - RX0 - 3 * 6) / 4
for i, (num, cap) in enumerate(NUMBERS):
    x = RX0 + i * (tw + 6)
    box(x, 406, x + tw, 446, fill=CARD, outline=SOFT)
    text(x + 6, 405, num, F("Black", 17), INK)
    para(x + 6, 428, cap, F("Condensed", 8), tw - 10, 9, GREY, max_lines=2)
text(RX0, 451, "HOW SURE", F("Bold", 8.5), GREY)
key = [("CONFIRMED", "several sources agree"), ("OFFICIAL", "government or agency"),
       ("REPORTED", "one wire or outlet"), ("SCHEDULED", "set for 24 Nov, result later")]
for i, (lab, meaning) in enumerate(key):
    x = RX0 + (i % 2) * 200
    y = 462 + (i // 2) * 10
    f = F("CondensedBold", 7.5)
    lw = width(lab, f)
    box(x, y, x + lw + 6, y + 9, fill=LABEL_COLOUR[lab], r=1.5)
    text(x + 3, y + 4.6, lab, f, CARD, anchor="lm")
    text(x + lw + 10, y + 4.6, meaning, F("Condensed", 8.5), INK, anchor="lm")

# ---------------------------------------------------------------- timeline
TY = 488
text(10, TY, "24 NOVEMBER, HOUR BY HOUR (UTC)", F("Black", 11), INK)
text(1014, TY + 1, TIMELINE_NOTE, F("Regular", 8.5), GREY, anchor="ra")
axis_y = TY + 39
d.line(P(14, axis_y, 1010, axis_y), fill=INK, width=round(1.6 * S))
colour_of = {s["n"]: REGION_COLOUR[s["region"]] for s in LEADS}
for region, items in REGIONS:
    for s in items:
        colour_of[s["n"]] = REGION_COLOUR[region]
step = (972 - 52) / (len(TIMELINE) - 1)
for i, (t, what, n) in enumerate(TIMELINE):
    x = 52 + i * step
    col = colour_of[n]
    text(x, axis_y - 7, t, F("Bold", 11), INK, anchor="ms")
    d.ellipse(P(x - 3.5, axis_y - 3.5, x + 3.5, axis_y + 3.5), fill=col)
    text(x, axis_y + 6, what, F("CondensedSemiBold", 9.5), INK, anchor="ma")
    pin(x, axis_y + 27, n, col, 6.5)

# ---------------------------------------------------------------- region blocks
COLS = [["ASIA"], ["EUROPE", "MIDDLE EAST"], ["AFRICA", "NORTH AMERICA"], ["OCEANIA", "LATIN AMERICA"]]
by_name = dict(REGIONS)
BY0, BY1 = 572, 1004
for c, names in enumerate(COLS):
    x = 10 + c * (CW + GAP)
    y = BY0
    for name in names:
        col = REGION_COLOUR[name]
        items = by_name[name]
        box(x, y, x + CW, y + 17, fill=col)
        text(x + 6, y + 8.5, name, F("Black", 10), CARD, anchor="lm")
        text(x + CW - 6, y + 8.5, f"{len(items)} {'story' if len(items) == 1 else 'stories'}",
             F("Bold", 8.5), CARD, anchor="rm")
        y += 21
        for s in items:
            pin(x + 8, y + 7, s["n"], col, 7)
            y = para(x + 20, y - 1, s["head"], F("CondensedBold", 12), CW - 22, 14, max_lines=2)
            y = para(x + 20, y, s["detail"], F("Condensed", 10.5), CW - 22, 12, (60, 63, 70), max_lines=2)
            chip(x + 20, y + 1.5, s["label"], s["src"])
            y += 17
        y += 3
    if y > BY1:
        print("WARN column", c, "ends at", round(y))

text(512, 1012, "Sources: Reuters, AP, CMSA, EMSC/USGS, UEFA, White House, PINA, Africa CDC, Google and others  ·  "
     "drawn shapes, no photos  ·  page made 24 Nov 2026", F("Regular", 8), GREY, anchor="mm")

out = img.resize((W, H), Image.LANCZOS)
out.save("entry.png", optimize=True)
print("entry.png written")
