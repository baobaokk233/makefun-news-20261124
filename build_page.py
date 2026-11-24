"""Render the 24 Nov 2026 world-news front page (1024x1024 PNG).

Deterministic: fixed copy, fonts, layout and PNG encoding. Running this
script twice produces byte-identical entry.png. The entry program main.py
only copies entry.png into the output directory (stdlib only), so the
submitted program stays deterministic too.
"""

import hashlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ASSETS = HERE / "assets"

W, H = 1024, 1024
PAPER = (253, 248, 238)      # warm newsprint cream
INK = (26, 26, 26)
RED = (179, 39, 30)          # classic newspaper red
GREY = (110, 104, 90)
RULE = (201, 194, 178)
DARK = (26, 26, 26)

SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
SERIF_BLK = "/usr/share/fonts/truetype/noto/NotoSerif-Black.ttf"
SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_center(draw, cx, y, text, fnt, fill):
    draw.text((cx - fnt.getlength(text) / 2, y), text, font=fnt, fill=fill)


def letterspaced(text):
    return " ".join(list(text))


# ---------------------------------------------------------------- stories
LEAD = {
    "kicker": "BUSINESS  ·  LEAD STORY",
    "headline": "HUANG IS BACK AS NVIDIA CHIEF; SHARES SOAR 31%",
    "deck": ("Nvidia's board unanimously reinstates its co-founder 11 days after "
             "he resigned. The Nasdaq jumps 6.5% in its best day since April."),
    "source": "REUTERS  ·  23 NOV 2026",
}

COLUMNS = [
    ("WORLD", [
        ("Korea scrambles jets as Russian planes enter air zone",
         "Fighters chase off Russian aircraft near Ulleung island; a shelter "
         "alert is lifted after 3 minutes.",
         "AP"),
        ("COP31 collapses without a deal",
         "Longest climate summit on record ends in failure as oil states block "
         "any mention of fossil fuels.",
         "CNN"),
        ("Moscow warns Estonia of \u2018open war\u2019",
         "Russia accuses Tallinn of hostile acts after Estonia says it will shut "
         "its border crossings from 1 Dec.",
         "REUTERS"),
        ("Allies: Russia may launch nuclear space weapon",
         "German reports cite Western intelligence; a satellite could fly in "
         "December. Moscow denies it.",
         "WDR / NDR / SZ"),
        ("Leaked data puts Russian war dead near 500,000",
         "Bloomberg analysis of Rosstat records counts at least 470,000; a "
         "Guardian count tops 460,000.",
         "BLOOMBERG"),
    ]),
    ("BUSINESS", [
        ("Markets roar back on Nvidia news",
         "S&P 500 +4.7% and Nasdaq +6.5% in the best day since April; Asia "
         "follows with Kospi +7.5%.",
         "REUTERS"),
        ("Two US states sue Musk over Grok deepfakes",
         "Virginia and Oregon say the chatbot made sexualised images of "
         "children; about 3 million in 11 days.",
         "AP"),
        ("Anthropic launches Claude Ship",
         "New tools to help developers review code changes and fix bugs faster.",
         "ANTHROPIC"),
        ("Honda recalls 810,000 vehicles in US",
         "Takata airbag inflators could rupture and send sharp metal fragments "
         "flying.",
         "AP"),
        ("Aviation groups seek $30bn for FAA overhaul",
         "Call for modernisation funding follows nationwide flight disruption.",
         "THE TIMES OF INDIA"),
    ]),
    ("NATIONS & LIFE", [
        ("Indonesia factory fire kills 24",
         "Blaze at a candy factory in Cikande; about 30 people still missing "
         "after the Saturday fire.",
         "REUTERS"),
        ("Trump orders faster federal executions",
         "Memo directs the death penalty for murders of children and for "
         "killings during sex crimes.",
         "AP"),
        ("Injured children from Gaza arrive in UK",
         "Young patients flown in for medical treatment as the war's toll on "
         "children keeps rising.",
         "AP"),
        ("Denmark to ban school phones to 10th grade",
         "Move follows poor PISA results and concern over classroom focus.",
         "AP"),
        ("2031 Women\u2019s World Cup hosts named",
         "US, Mexico, Costa Rica and Jamaica to host in 2031; the UK gets the "
         "2035 edition.",
         "AP"),
    ]),
]

BRIEFS = ("BRIEFLY  \u2014  Zanzibar hotel fire evacuates 180 tourists  \u00b7  Amtrak "
          "derails in Louisiana, 5 hurt  \u00b7  Quake of 4.1 strikes Pakistan")

NUMBERS = [
    ("S&P 500", "+4.7%", "7,237"),
    ("NASDAQ", "+6.5%", "24,090"),
    ("NIKKEI", "+3.9%", "58,654"),
    ("KOSPI", "+7.5%", "5,014"),
    ("NVIDIA", "+31.5%", "23-yr best"),
]

FOOTER = ("Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 CNN \u00b7 Bloomberg \u00b7 The Guardian \u00b7 "
          "The Japan Times \u00b7 Moneycontrol \u00b7 The Times of India \u2014 All stories "
          "published 23\u201324 Nov 2026. Lead illustration: AI-generated.")


# ---------------------------------------------------------------- render
def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36                      # side margin
    cw = W - 2 * mx              # content width = 952

    # ---- top line: volume / motto
    f_small = font(SANS_B, 11)
    d.line([(mx, 10), (W - mx, 10)], fill=INK, width=2)
    d.text((mx, 16), "VOL. I  \u2014  NO. 328", font=f_small, fill=INK)
    draw_center(d, W // 2, 16, "ONE DAY. ONE PAGE. THE WORLD.", f_small, INK)
    d.text((W - mx - f_small.getlength("TUESDAY EDITION"), 16),
           "TUESDAY EDITION", font=f_small, fill=INK)

    # ---- masthead
    f_mast = font(SERIF_BLK, 70)
    draw_center(d, W // 2, 20, "WORLD NEWS", f_mast, INK)
    d.line([(mx, 100), (W - mx, 100)], fill=INK, width=3)
    d.line([(mx, 104), (W - mx, 104)], fill=INK, width=1)

    # ---- dateline bar
    f_date = font(SERIF_B, 17)
    d.text((mx, 112), "TUESDAY, 24 NOVEMBER 2026", font=f_date, fill=RED)
    draw_center(d, W // 2, 114, letterspaced("THE WORLD IN ONE PAGE"),
                font(SANS_B, 12), GREY)
    right = "24 NOV 2026  \u00b7  16 STORIES"
    d.text((W - mx - f_date.getlength(right), 112), right, font=f_date, fill=INK)
    d.line([(mx, 136), (W - mx, 136)], fill=INK, width=1)

    # ---- lead story
    lx, ly = mx, 146
    lw = 560                    # lead text width
    f_kick = font(SANS_B, 12)
    d.text((lx, ly), letterspaced(LEAD["kicker"]), font=f_kick, fill=RED)
    f_head = font(SERIF_BLK, 36)
    y = ly + 20
    for line in wrap(LEAD["headline"], f_head, lw):
        d.text((lx, y), line, font=f_head, fill=INK)
        y += 44
    f_deck = font(SERIF, 16)
    y += 2
    for line in wrap(LEAD["deck"], f_deck, lw):
        d.text((lx, y), line, font=f_deck, fill=INK)
        y += 21
    y += 8
    d.text((lx, y), LEAD["source"], font=font(SANS_B, 11), fill=GREY)
    lead_text_bottom = y + 14

    # hero image, right of lead
    hero = Image.open(ASSETS / "lead_chip.png").convert("RGB")
    hw, hh = 372, 220
    src_ratio = hero.width / hero.height
    tgt_ratio = hw / hh
    if src_ratio > tgt_ratio:
        nw = int(hero.height * tgt_ratio)
        x0 = (hero.width - nw) // 2
        hero = hero.crop((x0, 0, x0 + nw, hero.height))
    else:
        nh = int(hero.width / tgt_ratio)
        y0 = (hero.height - nh) // 2
        hero = hero.crop((0, y0, hero.width, y0 + nh))
    hero = hero.resize((hw, hh), Image.LANCZOS)
    hx = W - mx - hw
    hy = ly + 2
    img.paste(hero, (hx, hy))
    d.rectangle([hx, hy, hx + hw - 1, hy + hh - 1], outline=INK, width=2)
    d.text((hx, hy + hh + 7), "AI CHIP STOCKS LEAD THE REBOUND  \u2014  ILLUSTRATION",
           font=font(SANS_B, 10), fill=GREY)
    lead_bottom = max(lead_text_bottom, hy + hh + 7 + 12)
    assert lead_bottom <= 392, f"lead overflows: {lead_bottom}"

    # ---- rule above columns
    d.line([(mx, 400), (W - mx, 400)], fill=INK, width=2)

    # ---- three columns
    col_w = 304
    gap = 20
    top = 412
    f_colh = font(SANS_B, 14)
    f_hl = font(SERIF_B, 15)
    f_sum = font(SANS, 12)
    f_num = font(SERIF_BLK, 15)
    f_lab = font(SANS_B, 10)
    n = 0
    col_bottoms = []
    for ci, (title, items) in enumerate(COLUMNS):
        x = mx + ci * (col_w + gap)
        d.text((x, top), letterspaced(title), font=f_colh, fill=RED)
        d.line([(x, top + 22), (x + col_w, top + 22)], fill=INK, width=1)
        y = top + 32
        for headline, summary, source in items:
            n += 1
            num = f"{n}."
            num_w = f_num.getlength(num) + 6
            hl_lines = wrap(headline, f_hl, col_w - num_w)[:2]
            d.text((x, y), num, font=f_num, fill=RED)
            yy = y
            for line in hl_lines:
                d.text((x + num_w, yy), line, font=f_hl, fill=INK)
                yy += 19
            y = yy + 2
            for line in wrap(summary, f_sum, col_w)[:2]:
                d.text((x, y), line, font=f_sum, fill=(60, 60, 60))
                y += 15
            y += 2
            d.text((x, y), "SOURCE: " + source, font=f_lab, fill=GREY)
            y += 12 + 8
        col_bottoms.append(y - 8)
        if ci < 2:
            vx = x + col_w + gap // 2
            d.line([(vx, top), (vx, 880)], fill=RULE, width=1)
    assert max(col_bottoms) <= 880, f"columns overflow: {col_bottoms}"

    # ---- briefly strip
    d.line([(mx, 890), (W - mx, 890)], fill=INK, width=1)
    d.text((mx, 898), BRIEFS, font=font(SANS_B, 12), fill=INK)

    # ---- day in numbers band
    band_y, band_h = 920, 56
    d.rectangle([mx, band_y, W - mx, band_y + band_h], fill=DARK)
    f_nlab = font(SANS_B, 11)
    f_nval = font(SERIF_BLK, 19)
    f_nnum = font(SANS, 12)
    d.text((mx + 10, band_y + 8), "THE DAY", font=f_nlab, fill=(253, 248, 238))
    d.text((mx + 10, band_y + 23), "IN NUMBERS", font=f_nlab, fill=(253, 248, 238))
    d.text((mx + 10, band_y + 38), "24 NOV", font=f_nlab, fill=(180, 175, 160))
    seg_x0 = mx + 118
    seg_w = (cw - 118) / len(NUMBERS)
    for i, (label, change, value) in enumerate(NUMBERS):
        cx = seg_x0 + seg_w * i + 8
        d.text((cx, band_y + 7), label, font=f_nlab, fill=(180, 175, 160))
        d.text((cx, band_y + 24), change, font=f_nval, fill=(120, 220, 140))
        vw = f_nval.getlength(change)
        d.text((cx + vw + 6, band_y + 29), value, font=f_nnum,
               fill=(253, 248, 238))

    # ---- footer
    f_foot = font(SANS, 10)
    y = 986
    for line in wrap(FOOTER, f_foot, cw):
        d.text((mx, y), line, font=f_foot, fill=GREY)
        y += 13
    assert y <= 1020, f"footer overflow: {y}"

    print(f"lead_bottom={lead_bottom} col_bottoms={col_bottoms} "
          f"footer_end={y}")
    return img


def main():
    out = render()
    target = HERE / "entry.png"
    out.save(target, format="PNG", optimize=True)
    data = target.read_bytes()
    print(f"entry.png: {out.size[0]}x{out.size[1]}, {len(data)} bytes, "
          f"sha256 {hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
