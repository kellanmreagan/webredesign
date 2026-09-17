# Barefoot On The Beach — Redesign Change Log

Source: http://www.barefootonthebeach.com/ (crawled and archived to `source/`). Redesign built
as static HTML/CSS/JS in this folder: `index.html`, `rental-info.html`, `amenities.html`,
`activities.html`, `bargains.html`, plus `css/style.css`, `js/main.js`, and `images/`.

## Layout & navigation — kept, with two broken links fixed

The source site's nav (Home / Rental Info / Amenities / Activities / Map to Resort / Bargains /
Contact Us) covers five distinct real pages plus one external map link and one mailto — a
sensible, non-duplicated structure. Per AGENTS.md rule 1, the redesign keeps the same pages,
names, and order.

Two things were fixed because they are outright bugs, not content:

1. **The source's own primary nav 404s on itself.** The homepage's horizontal nav links to
   `Pages/RentalInfo/index.htm` and `Pages/Bargains/index.htm` (capitalized), which both 404 on
   the live (case-sensitive) server — only the lowercase `Pages/rentalinfo/` and
   `Pages/bargains/` paths actually resolve. Confirmed by curling every path/case variant
   directly; see `source/crawl-log.md` for the full list of what 200s vs 404s. The redesign's
   nav links to working pages, obviously — this is a link-plumbing fix, not a content change.
2. **The "Home" nav link points to the wrong business.** On every page, "Home" links to
   `barefootartdesigns/index.htm`, which loads — but it's the homepage of an unrelated business,
   "Barefoot Art Designs" (a painting/mural/illustration portfolio site), not this vacation
   rental. This is a FrontPage-era mislinked-template leftover. The redesign's "Home" links go
   to the actual home page; none of the unrelated Barefoot Art Designs content was pulled in,
   since it isn't this business's content to preserve.

## Content preserved

- The full unit description, "One Bedroom Efficiency / NO SMOKING, NO PETS" notice, and the
  Dr. Beach ranking claims for Barefoot Beach and Delnor Wiggins State Park (Home page).
- The complete seasonal rate table — all 12 rows (Peak/High/Low/Mid season windows from January
  2019 through April 2021) — reproduced verbatim on the Rental Info page, including the exact
  dates and weekly rates. These dates are now in the past; they were **not** updated, extended,
  or removed, per the no-invented-content rule. **Flagging for the business owner:** this table
  is years out of date and should be refreshed with current rates before the site goes live for
  real bookings.
- All rental terms verbatim: one night/25% deposit policy, payment-in-full timing, the 10%
  4+-week discount, "rates are for two people, cleaning included, taxes not included, $300
  security deposit, one week minimum," and the "ask for the Internet Special" line.
- The full Amenities list (Beach, Tennis, Swimming, Bocci Ball, Basketball, Golf, Barbecue
  Grills, Schuffleboard, Horseshoes) verbatim, including the source's own spelling
  "Schuffleboard" and the 239-992-2345 tennis info number.
- The full Nearby Attractions and Activities list (13 entries: Bonita Beach, Barefoot Beach
  Preserve, Lovers Key/Carl Johnson State Park, Delnor-Wiggins Pass, Koreshan State Historical
  Site, Kayak/Canoe Rentals, Boating, Miniature Golf, Naples Pier, Ft. Myers Beach, Sanibel and
  Captiva Islands, Corkscrew Swamp Sanctuary, Naples Zoo) verbatim, including the "HIGHLY
  RECOMMENDED" call-outs (now shown as a small tag next to the heading rather than inline
  shouted text, same information).
- The Bargains page's current state verbatim: "None at this time" for last-minute specials
  (an honest empty state, not invented content) and the Internet Special reminder.
- Contact info exactly as used on each source page (see `source/content-notes.md` for the
  page-by-page mapping): phones 239-287-2603 and 239-947-9728 (click-to-call added throughout,
  in whichever order each source page listed them), and all three real email addresses in the
  same roles they had on the source — `barefoot@barefootonthebeach.com` (nav "Contact Us"),
  `bill@barefootonthebeach.com` (footer/topbar), and `info@barefootonthebeach.com` (Rental
  Info / Bargains reservation link) — none merged or replaced with a guess, matching the
  precedent set for a similar multi-address situation on the Dave Illg's Collision Repair
  Center redesign.
- 11 real, non-stock photos of the actual unit and resort (living room, kitchen, dining area,
  bedroom, Bonita Beach, Gulf sunset, tennis courts, Beach & Tennis Club aerial, Barefoot Beach
  Preserve, Lovers Key, Delnor-Wiggins Pass) and the site's own "Barefoot On The Beach" logo
  banner graphic — all reused directly from the source. See "Recovering the Flash photo
  galleries" below for how these were found.
- Owner names (Bill and Randi Zwicker) and the Beach & Tennis Club / Bonita Beach Rd, Bonita
  Springs, FL 34134 location.

## Recovering the Flash photo galleries

Each of the four inner pages displayed its real photos through a "click on image below to
enlarge picture" Flash 4/5 `.swf` slideshow (`RentalInfo.swf`, `Amenities.swf`,
`Activities.swf`, `LastMinuteBargains.swf`) — Flash has been unsupported by every modern browser
since 2020, so these rendered as blank space. Rather than drop the photos, the four `.swf` files
were downloaded and inspected for embedded image URLs (via `strings`), which recovered the real
absolute URLs of 11 real condo/amenity/activity photos hosted alongside the Flash files. All 11
were fetched directly and are included in the redesign's photo galleries (a plain CSS grid + a
lightweight vanilla-JS lightbox, no plugin required) on the Amenities and Activities pages. No
photo was invented, substituted, or dropped — only the dead Flash wrapper was replaced with a
working modern equivalent.

## Judgment call: personal media/software links omitted (AGENTS.md rule 5)

The live homepage currently has several links that are not vacation-rental business content:
a 1965 Corvette-transport video, four personal "family"/"Michelle" videos, and two Avigilon
CCTV software installer downloads captioned "Files for Kathy Adgate." These read as the site
owner using unused space on their own web host for personal file-sharing, unrelated to renting
the condo — there's no vacation-rental content in any of them (confirmed by their filenames/
captions; the video/executable files themselves were not downloaded). Per AGENTS.md rule 5
("you may omit non-content chrome / tech debt... never omit real business information or real
media"), these were treated as personal clutter and left out of the redesign, since including
random home videos and unrelated third-party software installers would not serve a vacation
renter and isn't part of this business's offering. **Flagging explicitly per the task
instructions:** if any of these are actually meant to stay on the public site, let me know and
I'll add them back (e.g. as plain links in the footer) rather than silently keep them dropped.

## Non-content chrome omitted (per AGENTS.md rule 5)

- `Scripts/AC_RunActiveContent.js` (Dreamweaver Flash-detection shim) and all `MM_swapImage` /
  `MM_preloadImages` DHTML nav-button-hover JavaScript — replaced with plain CSS hover states.
- The invisible white-on-white keyword-stuffing paragraph repeated on the Rental Info,
  Amenities, Activities, and Bargains pages (`<font color="#FFFFFF">` text on a white
  background — invisible to visitors, grammatically broken, trails off mid-sentence). This is
  SEO keyword spam, not visible page content, matching the precedent set for the tiny 1pt-font
  keyword footer omitted from the Pleasant Valley Log Cabins redesign. Every page's long
  `<meta name="keywords">` tag content was likewise omitted, as it is not shown to visitors.
- The Google Custom Search embed on four pages (third-party widget, not site content).
- The PayPal "Pay Now" hosted-button embed (its policy text — PayPal/credit card/personal
  check accepted — is preserved as real content on the Rental Info page; the live embedded
  form itself was not reproduced, and its continued validity was not verified).
- The "What is the weather now in Bonita Springs?" Yahoo Weather link (dead third-party
  service; not site content).
- FrontPage `<!-- #BeginLibraryItem -->` / table-layout markup and inline `<font>` tags —
  replaced with semantic HTML and CSS throughout.

## Design

Restrained coastal palette (deep ocean teal, warm sand, a muted coral accent) drawn from the
subject matter itself — beach, tennis club, Gulf sunsets — rather than a generic vacation-rental
template look. An italic serif display face (Fraunces) for headings evokes a relaxed, upscale
beach-club feel; a clean sans body face (Jost) keeps the rate tables and activity list readable.
Mobile-first, fully responsive, click-to-call phone numbers throughout, and a lightweight photo
lightbox (no framework, vanilla JS) replacing the dead Flash slideshows.
