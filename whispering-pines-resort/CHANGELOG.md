# Whispering Pines Resort — Redesign Change Log

Source: https://whisperingresort.com/ (crawled and archived to `source/`). Redesign built as
static HTML/CSS/JS in this folder: `index.html`, `availability.html`, `prices.html`,
`canoes.html`, `trails.html`, `directions.html`, `history.html`, plus `css/style.css`,
`js/main.js`, and `images/`.

## Layout & navigation — kept as-is

The source site's information architecture (Home, Availability, Prices/Rules, Canoe Liveries,
Trail Maps, Map/Directions, WPR History) was already a clear, non-duplicated set of 7 pages,
cross-linked from a text link list at the bottom of every page. Per AGENTS.md rule 1, the
redesign keeps the same 7 pages, same names, same content groupings — just as a persistent top
nav (with a mobile hamburger menu) instead of repeated bottom-of-page text links.

## Content preserved

- All body copy from every page, verbatim, including the homepage's full "You'll love it up
  here" / seasons-on-the-river / location copy, the full prices/rules text (cabin specs, campsite
  pricing, discounts, cancellation policy, and every guest rule), the full history page, all four
  driving-direction routes, the canoe/kayak trip-time table, and all trail-map links.
- The entire live cabin availability calendar (see `source/content-notes.md` for the full
  breakdown) — every reserved cabin number, every day, for the closed months and the three months
  of live data present at crawl time.
- All 19 photos and the hand-drawn directions map, reused directly from the source site — no
  stock photography, nothing dropped. Renamed from cryptic source filenames to descriptive ones
  (see `source/crawl-log.md`).
- The site's own wordmark/logo graphic (`logo.gif`), used in the header and footer rather than
  replaced with new brand styling.
- Contact info: phone (989) 348-2044, email info@whisperingresort.com, address 11763 W. County
  Rd. 612, Frederic, MI 49733. Click-to-call added on every phone number.

## Content oddities resolved (AGENTS.md rule 6)

- `trails1.htm`'s footer listed the phone number with a 517 area code, while all 6 other pages
  use 989 (989 covers the Frederic/Grayling area; 517 is Lansing, ~150 miles away). Used 989
  throughout, matching the consistent value.
- The mailing address appeared in three different abbreviation styles across pages
  ("W.Co.Rd.612" / "W. County Rd. 612" / "W. 612") — not a factual conflict, just inconsistent
  formatting. Standardized on "11763 W. County Rd. 612, Frederic, MI 49733" everywhere.

## Non-content chrome omitted (per AGENTS.md rule 5)

- Dead HTML comments from past seasonal copy (SUMMER/FALL/WINTER promotional blurbs, a defunct
  "we accept Mastercard and Visa" notice that directly contradicts the live "checks, cash or
  money orders only" policy) — confirmed not rendered on the live site before omitting.
- A stray, unmatched `-->` that renders as literal garbage text on the live homepage (leftover
  from a broken HTML comment edit) — the real heading next to it was kept.
- The "\*\*\*\* Double click photos for a better view \*\*\*\*" instruction, tied to the old
  thumbnail-then-full-size click pattern; full-size photos are shown directly now.
- `mc.gif` / `visa.gif` payment-logo images, referenced only inside the dead comment above.

## Flagged for the business owner, not resolved

The availability calendar (`availability.html`) is a faithful re-presentation of the same
manually-maintained data entry the old site used — it is **not** a live booking system. It will
need the same month-by-month manual updates going forward. See `source/content-notes.md` for
exactly what was live at crawl time.

## Design

Palette pulled directly from the resort's own office sign photo (deep navy background, gold
wordmark, pine-green and sky-blue sunrise icon) rather than a new brand identity — matches the
"rustic river lodge" personality called for in AGENTS.md. Bitter (a slab serif with cabin-sign
character) for headings, Karla for body copy. Mobile-first, fully responsive, click-to-call
phone numbers throughout, and a hand-built CSS Grid calendar in place of the source's nested
HTML tables for the availability page.
