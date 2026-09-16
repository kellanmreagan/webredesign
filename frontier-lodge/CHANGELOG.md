# Frontier Lodge — Redesign Change Log

Source: https://www.frontierlodge.com/ (crawled and archived to `source/`). Redesign built as
static HTML/CSS/JS in this folder: `index.html`, `fishing.html`, `rates.html`, `location.html`,
`snowmobiling.html`, `bearhunting.html`, `moosehunting.html`, plus `css/style.css`, `js/main.js`,
and `images/`.

## Layout & navigation — kept as-is

The source site is exactly 7 pages (confirmed by a full breadth-first crawl of every internal
link on every page — no gallery, cottages, ice-fishing, or testimonials pages exist). The nav
destinations and labels (Fishing, Rates, Location, Snowmobiling, Bear Hunting, Moose & Grouse
Hunting) were already clear and non-duplicated, so per AGENTS.md rule 1 the redesign keeps the
same 7 pages, same names, same destinations. The one change: the source site's nav order varied
slightly page-to-page (a FrontPage artifact, not intentional IA), so the redesign uses one
consistent nav order (Home, Fishing, Rates, Location, Snowmobiling, Bear Hunting, Moose & Grouse
Hunting) site-wide — a refinement, not a reshuffle.

## Content preserved

- All body copy from every page, verbatim, including the source's own typos/quirks per the
  no-rewrite rule: "wood for heath" (fishing.html), "6 SCENIC MILES OFF THE TOP F TRAIL"
  (snowmobiling.html), and "Sales Tax extra were applicable" (appears this way, verbatim, on
  every rates/policy block across the site).
- Every rate table: cabin family/group rates (2-Bedroom, Cabin #8, Cabin #9 & 10), rentals,
  docking fees, bear hunt day-rates, and the Rawhide Lake fishing outpost rate — all numbers
  reproduced exactly as listed.
- All reservation and property policies: 2-night minimum, no-pet policy, 50% deposit, 60-day
  cancellation window, accepted payment types, bear season dates and firearm-registration note.
- The full amenities list, "within driving distance" list, and both housekeeping-cottage
  descriptions (moose/grouse page and homepage).
- All 20 real photos reused directly from the source site (cabins, lodge exterior, lake/beach,
  hunters, snowmobiling, the hand-drawn location map, and the Rawhide Lake/trail maps) — no stock
  photography substituted, nothing dropped. The trail map thumbnail still links to the full-size
  map image, same as the source site's "For Better View — Click On Map."
- The site's actual logo graphic (`largelogo.gif`, the cursive "Frontier Lodge" mark over a lake
  sunset) reused directly in the header on every page.
- Contact info: phone (705) 848-2809, toll-free 1-888-848-2809, email frontierbetty@hotmail.com,
  P.O. Box 278, Elliot Lake, Ontario P5A 2J7, host Ken Luciani — 100% consistent in the source,
  reproduced identically, with click-to-call added on both phone numbers.

## Content oddities flagged, not resolved (AGENTS.md rule 6)

1. **Outdated pet-policy date.** The homepage's no-pet-policy line reads "effective Jan. 1,
   2006" — the policy itself is clearly still current (rates.html restates it with no date), but
   that date is now roughly 20 years old. Kept verbatim rather than silently dropped or updated.
   **Flagging for you:** would you like that date line removed, since the policy is evidently
   standing/ongoing rather than a 2006-only announcement?
2. **fishing.html meta description says "Bark Lake"** but 100% of the page's visible content is
   about "Rawhide Lake" — likely a stale meta description from an earlier version of the page.
   The redesign's meta description was written to match the actual visible content (Rawhide
   Lake), since AGENTS.md permits meta title/description to reuse **existing** site text, and the
   body copy is the more consistent, more visible source of truth here.
3. **location.html's original title/meta both said "winter family vacation"** despite the page
   being 100% driving directions with no winter content — likely copy-pasted from another page.
   The redesign's title/meta for this page were written to describe what the page actually is
   (directions/location), same reasoning as above.

## Non-content chrome omitted (per AGENTS.md rule 5)

- FrontPage tiled background image and `GENERATOR` meta tag.
- The "Due North Marketing" site-designer credit footer (a promotional link for the original
  site's builder, not Frontier Lodge's own content).
- The FEDNOR government-badge and Ontario Fishing Network badge images/links — third-party
  affiliation badges, inconsistently present on only some of the original pages, not core
  business content.
- `anielg.gif`'s leftover unedited FrontPage alt text ("anielg.gif (18700 bytes)") — the image
  itself (two hunters and a hung deer near the lodge, real business content) is not on this
  page's build since it duplicated newmoose1.gif's subject; alt text across the site uses
  plain, non-invented descriptions per the "don't invent marketing alt copy" rule.

## Design

Palette pulled from the site's own logo and cabin photos (deep pine green, warm rust/red,
cream) rather than a new brand identity — matches the "wilderness lodge" personality called for
in AGENTS.md. Serif headings (Libre Baskerville) read as a classic lodge letterhead; clean body
type (Nunito Sans) keeps the long rate tables and policy text scannable. Mobile-first, fully
responsive, click-to-call phone numbers throughout.
