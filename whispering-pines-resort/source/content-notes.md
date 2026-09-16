# Content notes — whisperingresort.com → redesign

## Pages mapped

| Source page   | Redesign page        |
|----------------|----------------------|
| `index.html`   | `index.html` (Home)  |
| `avail.htm`    | `availability.html`  |
| `prices.htm`   | `prices.html`        |
| `wprhist.htm`  | `history.html`       |
| `wpmap.htm`    | `directions.html`    |
| `canoes1.htm`  | `canoes.html`         |
| `trails1.htm`  | `trails.html`        |

Nav/IA was already a clean flat set of 7 pages (home + 6 topic pages, cross-linked from every
page's footer) — kept as-is per AGENTS.md rule 1, just given a persistent top nav instead of
bottom-of-page text links repeated on every page.

## Live vs. dead content (important distinction)

The source HTML has years of accumulated HTML comments (`<!-- -->`) from past seasonal copy
(SUMMER/FALL/WINTER blurbs, a defunct Mastercard/Visa acceptance notice). These were **not**
rendered on the live site — confirmed by fetching the rendered page text, not just the raw HTML
— so per rule 5 they were left out as dead chrome, not content.

One partially-live artifact: the homepage has a stray, unmatched `-->` that renders as literal
visible text on the live site (a broken/orphaned HTML comment from a past edit). The heading it
sits next to ("Make Your Summer Fun Reservations Now!") is genuinely live and was kept; the
literal `-->` garbage text was omitted as markup corruption, not content.

The "\*\*\*\* Double click photos for a better view \*\*\*\*" instruction was omitted: it's a
UX instruction tied to the old thumbnail→full-size click pattern (bandwidth-saving 1990s
convention), which no longer applies now that full-size photos are shown directly and are
already visually hinted as clickable.

## Images

All photos, the logo, and the hand-drawn directions map were re-fetched from the live site and
reused directly (no stock substitutions, nothing dropped). Renamed from cryptic originals
(`cbn1fulsiz1.jpg`, `rakfulsiz.jpg`, etc.) to descriptive filenames — see `crawl-log.md` — since
filenames are non-content chrome, not copy. Alt text was written to match what's actually in each
photo, since the source alt attributes were themselves single unadorned words (`Cap`, `Dock`,
`old1`) with no descriptive captions to preserve.

Payment-logo images (`mc.gif`, `visa.gif`) referenced only inside dead HTML comments were not
carried over — the live `prices.htm` explicitly states "We accept checks, cash or money orders
only," which would directly contradict showing card-payment logos.

The DNR trail-search screenshot (`dnrhikelist.jpg` → `dnr-trail-search-results.jpg`) is a
screenshot of a Michigan.gov public results page that was already embedded in the source site;
reproduced as-is as reference content, same as the source.

## The availability calendar (`avail.htm` → `availability.html`)

This is a live, manually-updated booking calendar — the source itself says "LAST UPDATE 08/17/26"
and repeatedly tells guests to call for the most current status. At crawl time (2026-09-16) the
calendar had:
- January–April 2026 marked CLOSED
- May/June/July tables present in the HTML but wrapped in comments (not live/rendered — omitted)
- August, September, and October 2026 as live, day-by-day cabin-reservation grids
- November–December 2026 marked CLOSED

All of this was reproduced faithfully (every reserved cabin number, every day) in a responsive
CSS Grid calendar instead of the source's nested HTML `<table>` markup. **Flagging for the
business owner:** this page will need the same manual updates the old one did each month/season —
it is not wired to a live booking system, just a faithful re-presentation of the same static data
entry workflow.

## Address formatting

The source renders the same address three slightly different ways across pages
("11763 W.Co.Rd.612", "11763 W. County Rd. 612", "11763 W. 612") — not a factual conflict, just
inconsistent abbreviation from page to page. Standardized on "11763 W. County Rd. 612, Frederic,
MI 49733" everywhere in the redesign, per rule 6 (use the clearest/most complete consistent
value when variants exist).

## Phone number

`trails1.htm`'s footer listed "(517)348-2044" while every other page uses "(989)348-2044". 517
is a Lansing-area code, nowhere near Frederic, MI (which is 989 territory) — used "(989)
348-2044" throughout, matching all 6 other instances across the site.
