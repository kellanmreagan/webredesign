# Pleasant Valley Log Cabins — Redesign Change Log

Source: http://www.pvlc.com/ (crawled and archived to `source/`). Redesign built as static
HTML/CSS/JS in this folder: `index.html`, `cabins.html`, `rates.html`, `activities.html`,
`directions.html`, `family.html`, plus `css/style.css`, `js/main.js`, and `images/`.

## Layout & navigation

The original site's nav/IA was thin, duplicated, and partly broken: two separate photo-gallery
pages for the Deer Meadow cabin (byte-identical, one linked as "Large Cabin" from the rates page
and the other as "Deer Meadow" from the facilities page), two "Return to Home" links on the
Bird's Nest and Bear's Den gallery pages pointing at dead `file:///C:/...` paths from the original
author's PC, and cabin descriptions/photos split across three separate pages per cabin
(facilities page, rates page, standalone gallery page) with no way to get from one to another.

Per AGENTS.md rule 2 ("if nav/IA is confusing, thin, duplicated, or broken: modernize
structure... while still placing all content and media on the appropriate pages"), the site was
restructured into 6 pages with a single persistent nav:

- **Home** (`index.html`) — was `index.html`
- **Cabins** (`cabins.html`) — merges `cabinfacilities.html` with all four per-cabin photo
  gallery pages (`photo gallery Moose Lodge.html`, `photo gallery dear meadow cabin.html` /
  `photo gallery large cabin.html` [duplicate, treated as one], `photo_gallery_for_the_bird.html`,
  `photo_gallery_for_the_bears_den.html`) into one scannable page with a lightbox
- **Rates & Policies** (`rates.html`) — was `CabinRentalRates.html`
- **Activities** (`activities.html`) — merges `cabrental.html`'s Nearby Activities and Family
  Activity Suggestions sections with `winter_at_pleasant_valley.html`, its picture gallery
  (`pleasant_valley_is_a_winter_wond.html`), and `Ski Package Special.htm` into one activities page
- **Directions** (`directions.html`) — was `localmap.html`
- **Our Family** (`family.html`) — was `Our Family.html`

All body copy, headings, prices, specs, and captions were copied verbatim from the source pages
(see `source/content-notes.md` for the verbatim reference used while building). Nothing was
paraphrased or rewritten.

## Content preserved

- Every cabin description, spec, and rate table (Moose Lodge, Deer Meadow, Bird's Nest, Bear's
  Den) — copied verbatim from both `cabinfacilities.html` (on the Cabins page) and
  `CabinRentalRates.html` (on the Rates page), since the two source pages used slightly different
  phrasing for the same cabins; both original texts are kept on their respective new pages rather
  than merged/rewritten into one.
- All policies, nearby activities, family activity suggestions, winter activities, ski package
  details, directions, and the Fisher family photo/page.
- All 41 real business photos (cabin exteriors, interiors, galleries, family photo, winter
  photos, maps, activity icons) — reused from the source site, resized/compressed for web
  performance only (no content change), original filenames preserved in `source/images/`.
- Contact info verified consistent across every source page: phone (608) 633-0029, email
  info@pvlc.com. Two distinct addresses (mailing: S480 24th Ct.; cabin location: S453 24th Ct.)
  are both real and both preserved everywhere they appeared.

## Non-content chrome omitted (per AGENTS.md rule 5)

- FrontPage `<marquee>` scrolling banner on the homepage — its text was kept as static body copy
  in the hero section, just not as a scrolling animation.
- Animated falling-snow JavaScript effect on the winter page.
- Tiny 1pt-font SEO keyword-stuffing blocks at the bottom of the homepage and ski package page.
- A stray `<p>60</p>` FrontPage artifact on the rates page.
- Dead `file:///C:/PVLC Web Files/...` links on two gallery pages — replaced with working links
  back to the site (no content lost, since the link text "Return to Pleasant Valley Home Page"
  is preserved and now actually works).
- FrontPage generator meta tags and `FP_swapImg`/`FP_preloadImgs` button-hover JS boilerplate,
  replaced with plain CSS/HTML nav.
- The old small "Log Cabin Rentals" / "Our Family" GIF nav buttons — replaced with a modern text
  nav bar linking to the same (and additional, previously unlinked-from-home) destinations.

## Design

Restrained palette pulled from the log-cabin photos themselves (forest green, warm bark brown,
cream, amber accent) instead of introducing a new brand identity. Serif display type for
headings (rustic-but-classy, not generic SaaS) paired with a clean sans body face. Mobile-first,
fully responsive, click-to-call phone numbers, and a lightweight photo lightbox for the cabin
galleries (no framework, ~35 lines of vanilla JS).
