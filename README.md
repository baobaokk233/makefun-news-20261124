# World News — Tuesday 24 November 2026, One Page

A single square image summing up the world news of **Tuesday 24 November 2026**,
laid out as a newspaper front page: masthead with the date, one big lead story
with an AI-generated illustration, three columns of numbered stories with a
source on every item, a briefs line and a "day in numbers" markets strip.

## The stories (16 + 3 briefs)

Lead — **Huang is back as Nvidia chief; shares soar 31%** (Reuters, 23 Nov).
Nvidia's board unanimously reinstates its co-founder 11 days after he resigned,
under pressure from President Trump. Nasdaq +6.5% in its best day since April;
Nvidia shares recover nearly $1 trillion in value.

World

1. **Korea scrambles jets as Russian planes enter air zone** (AP, 24 Nov).
   Fighters chase off Russian aircraft near Ulleung island; a shelter alert is
   lifted after 3 minutes. No airspace violation.
2. **COP31 collapses without a deal** (CNN, 22–23 Nov). Longest climate summit
   on record ends in failure as oil states block any mention of fossil fuels.
3. **Moscow warns Estonia of 'open war'** (Reuters, 23 Nov). Russia accuses
   Tallinn of hostile acts after Estonia says it will shut border crossings
   from 1 December.
4. **Allies: Russia may launch nuclear space weapon** (WDR / NDR / SZ, 23 Nov).
   Western intelligence cited in German reports; a satellite could fly in
   December. Moscow denies the claim.
5. **Leaked data puts Russian war dead near 500,000** (Bloomberg, 23 Nov).
   Analysis of Rosstat records counts at least 470,000; a Guardian count of
   the same leak tops 460,000.

Business

6. **Markets roar back on Nvidia news** (Reuters, 24 Nov). S&P 500 +4.7% and
   Nasdaq +6.5% in the best day since April; Asia follows with Kospi +7.5%.
7. **Two US states sue Musk over Grok deepfakes** (AP, 23 Nov). Virginia and
   Oregon say the chatbot made sexualised images of children; about 3 million
   in 11 days.
8. **Anthropic launches Claude Ship** (Anthropic, 23 Nov). New tools to help
   developers review code changes and fix bugs faster.
9. **Honda recalls 810,000 vehicles in US** (AP, 24 Nov). Takata airbag
   inflators could rupture and send sharp metal fragments flying.
10. **Aviation groups seek $30bn for FAA overhaul** (The Times of India,
    24 Nov). Call for modernisation funding follows nationwide flight
    disruption.

Nations & Life

11. **Indonesia factory fire kills 24** (Reuters, 23 Nov). Blaze at a candy
    factory in Cikande; about 30 people still missing after the Saturday fire.
12. **Trump orders faster federal executions** (AP, 23 Nov). Memo directs the
    death penalty for murders of children and for killings during sex crimes.
13. **Injured children from Gaza arrive in UK** (AP, 24 Nov). Young patients
    flown in for medical treatment.
14. **Denmark to ban school phones to 10th grade** (AP, 24 Nov). Move follows
    poor PISA results and concern over classroom focus.
15. **2031 Women's World Cup hosts named** (AP, 24 Nov). US, Mexico, Costa
    Rica and Jamaica to host in 2031; the UK gets the 2035 edition.

Briefly — Zanzibar hotel fire evacuates 180 tourists; Amtrak derails in
Louisiana, 5 hurt; quake of 4.1 strikes Pakistan (The Times of India, 24 Nov).

Day in numbers — S&P 500 +4.7% (7,237) · Nasdaq +6.5% (24,090) · Nikkei +3.9%
(58,654) · Kospi +7.5% (5,014) · Nvidia +31.5% (best day in 23 years).
US closes are Monday 23 Nov; Asian closes are Tuesday 24 Nov (Reuters,
Moneycontrol).

## Verification note

- The image is `entry.png`: 1024 x 1024 pixels, 331,522 bytes (under 1 MiB).
- Every headline, figure and source above was checked against reporting dated
  23–24 November 2026 before this note was written; per-story sources are in
  `news24_sources.md`.
- No faces appear on war/death items: the lead illustration is a generated
  computer chip with a rising chart, no people.
- The program is deterministic: `main.py` only copies `entry.png` into the
  output directory, so running it twice produces byte-identical files.
  `build_page.py` re-renders the page from the fixed copy and the generated
  hero image in `assets/lead_chip.png`; two runs give the same SHA-256
  (`387c1bd203ebac273b9e73215ef26dcec5aca57620feb9ccec8d6e03dc00a437`).
- Kit check (24 Nov kit, run 2026-11-24 ~14:43 CST): 13 passed, 1 failed,
  5 at-submission. The one failure is `thinking_reproduces` against the
  morning transcript bundle, which predates this rebuild — the bundle must be
  rebuilt from the sessions that wrote this version before submission. The
  kit itself is kept outside this repo at
  `~/workspace/makefun_news_20261124-kit/` (its files would count as
  unwritten lines against the entry). The v1 entry it replaces is backed up
  at `~/workspace/makefun_news_20261124-backup-v1/`.

## How to run

```sh
python3 main.py
```

The image is written to the directory in `MAKEFUN_OUTPUT_DIR`, or to `/output`
when that variable is not set. The directory is created if it does not exist.

To re-render the page from scratch (needs Pillow and the fonts the script
names, plus `assets/lead_chip.png`):

```sh
python3 build_page.py
```
