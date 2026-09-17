# Crawl log

Crawled 2026-09-16 from http://www.barefootonthebeach.com/ (Apache, no directory listing —
`imgsbtns/`, `Pages/`, and `Scripts/` all return 403 Forbidden when requested directly).

## Case-sensitivity / broken-link anomalies found

This server is case-sensitive (Linux Apache), but the site's own HTML links use inconsistent
casing left over from the original FrontPage-era Windows authoring environment, where filenames
are case-insensitive. As a result, several links **as coded in the live HTML currently 404 on
the live server**:

- The homepage's own horizontal nav links to `Pages/RentalInfo/index.htm` (capital R, capital
  I) → **404**. The working page is at `Pages/rentalinfo/index.htm` (all lowercase) → 200. The
  vertical sidebar nav on the same page correctly uses the lowercase path.
- The homepage's own horizontal nav links to `Pages/Bargains/index.htm` (capital B) → **404**.
  The working page is at `Pages/bargains/index.htm` (lowercase) → 200. Again, the vertical
  sidebar nav uses the correct lowercase path.
- `Pages/amenities/index.htm` and `Pages/activities/index.htm` are already lowercase everywhere
  and both resolve → 200.
- The site root `/index.htm` (as linked from every subpage's vertical sidebar "Home" button)
  → **404**. Only `/` and `/index.html` (lowercase, .html not .htm) resolve → 200, and both
  serve the identical 26420-byte homepage.
- Every page's horizontal-nav "Home" link (`barefootartdesigns/index.htm` from the homepage,
  `../../barefootartdesigns/index.htm` from subpages) resolves → 200, but it is the homepage of
  a **different, unrelated business** ("Barefoot Art Designs" — a painting/mural/illustration
  portfolio site), not this vacation rental. See content-notes.md for detail. Treated as a
  broken/mislinked nav artifact, not real content for this business, and fixed to point to the
  actual home page in the redesign (see CHANGELOG.md).

These are pre-existing bugs on the live site, not crawler errors — confirmed by directly curling
each URL and checking the HTTP status and page `<title>`.

## Pages

- PAGE http://www.barefootonthebeach.com/ -> html/root.html (HTTP 200, 26420 bytes) — canonical home page
- PAGE http://www.barefootonthebeach.com/index.html -> (HTTP 200, 26420 bytes, byte-identical to `/`; not re-saved)
- PAGE http://www.barefootonthebeach.com/index.htm -> (HTTP 404, 355 bytes) — linked from every subpage's sidebar "Home" button; broken
- PAGE http://www.barefootonthebeach.com/Index.htm -> (HTTP 404, 355 bytes) — checked for case-insensitivity; also broken
- PAGE http://www.barefootonthebeach.com/default.htm -> (HTTP 404, 355 bytes) — checked as a possible alternate default doc; not used
- PAGE http://www.barefootonthebeach.com/Pages/RentalInfo/index.htm -> (HTTP 404, 355 bytes) — as coded in homepage's own horizontal nav; broken, see anomaly note above
- PAGE http://www.barefootonthebeach.com/Pages/rentalinfo/index.htm -> html/Pages/rentalinfo/index.htm (HTTP 200, 30381 bytes) — actual working page
- PAGE http://www.barefootonthebeach.com/Pages/amenities/index.htm -> html/Pages/amenities/index.htm (HTTP 200, 25729 bytes)
- PAGE http://www.barefootonthebeach.com/Pages/Amenities/index.htm -> (HTTP 404, 355 bytes) — checked for case-insensitivity; broken
- PAGE http://www.barefootonthebeach.com/Pages/activities/index.htm -> html/Pages/activities/index.htm (HTTP 200, 30200 bytes)
- PAGE http://www.barefootonthebeach.com/Pages/Activities/index.htm -> (HTTP 404, 355 bytes) — checked for case-insensitivity; broken
- PAGE http://www.barefootonthebeach.com/Pages/Bargains/index.htm -> (HTTP 404, 355 bytes) — as coded in homepage's own horizontal nav; broken, see anomaly note above
- PAGE http://www.barefootonthebeach.com/Pages/bargains/index.htm -> html/Pages/bargains/index.htm (HTTP 200, 25460 bytes) — actual working page
- PAGE http://www.barefootonthebeach.com/barefootartdesigns/index.htm -> html/barefootartdesigns_index.htm (HTTP 200, 5225 bytes) — unrelated business's homepage, linked in error as this site's "Home"; not incorporated as content, see anomaly note above

## Images / media referenced by the four real pages

- IMG http://www.barefootonthebeach.com/imgsbtns/IndexTitle.gif -> images/IndexTitle.gif (HTTP 200, 13497 bytes) — site's logo/title banner, used on every page
- IMG http://www.barefootonthebeach.com/imgsbtns/RentalInfo.swf -> images/RentalInfo.swf (HTTP 200, 42871 bytes) — Flash slideshow on Rental Info page, unplayable in modern browsers; photo filenames recovered from its embedded strings (see below)
- IMG http://www.barefootonthebeach.com/imgsbtns/Amenities.swf -> images/Amenities.swf (HTTP 200, 21422 bytes) — Flash slideshow on Amenities page, same treatment
- IMG http://www.barefootonthebeach.com/imgsbtns/Activities.swf -> images/Activities.swf (HTTP 200, 32998 bytes) — Flash slideshow on Activities page, same treatment
- IMG http://www.barefootonthebeach.com/imgsbtns/LastMinuteBargains.swf -> images/LastMinuteBargains.swf (HTTP 200, 44182 bytes) — Flash slideshow on Bargains page, same treatment
- IMG http://www.barefootonthebeach.com/imgsbtns/bedroom.jpg -> images/bedroom.jpg (HTTP 200, 59336 bytes) — recovered from RentalInfo.swf / LastMinuteBargains.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/diningroom.jpg -> images/diningroom.jpg (HTTP 200, 73314 bytes) — recovered from RentalInfo.swf / Activities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/kitchen.jpg -> images/kitchen.jpg (HTTP 200, 75073 bytes) — recovered from RentalInfo.swf / LastMinuteBargains.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/livingroom.jpg -> images/livingroom.jpg (HTTP 200, 82608 bytes) — recovered from LastMinuteBargains.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/beachview.jpg -> images/beachview.jpg (HTTP 200, 78000 bytes) — recovered from Activities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/sunset1.jpg -> images/sunset1.jpg (HTTP 200, 62091 bytes) — recovered from Activities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/TennisCourts.jpg -> images/TennisCourts.jpg (HTTP 200, 103559 bytes) — recovered from Amenities.swf / Activities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/BeachTennisClubAir.jpg -> images/BeachTennisClubAir.jpg (HTTP 200, 104093 bytes) — recovered from Amenities.swf / Activities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/DelnoreWigginsPass.jpg -> images/DelnoreWigginsPass.jpg (HTTP 200, 69611 bytes) — recovered from Amenities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/Barefoot%20Beach%20Preserve.jpg -> images/Barefoot Beach Preserve.jpg (HTTP 200, 67673 bytes) — recovered from Amenities.swf strings
- IMG http://www.barefootonthebeach.com/imgsbtns/Lovers%20Key%20w%20car.jpg -> images/Lovers Key w car.jpg (HTTP 200, 88108 bytes) — recovered from Amenities.swf strings

Note on recovering the Flash photo galleries: each `Pages/*/index.htm` embeds an `AC_FL_
RunContent(...)` call loading a Flash 4/5 `.swf` "click on image below to enlarge picture"
slideshow (`RentalInfo.swf`, `Amenities.swf`, `Activities.swf`, `LastMinuteBargains.swf`).
Flash is not supported by any current browser, so these slideshows render as nothing. The
`.swf` files were downloaded and inspected with `strings` for embedded URLs, which recovered
full absolute-URL references (`http://www.barefootonthebeach.com/imgsbtns/<name>.jpg`) to 11
real condo/amenity/activity photos. All 11 were fetched directly and are real, high-resolution
(1024x768 / 800x600) photos of the actual unit and resort — not stock images. They are the same
photos the Flash slideshows displayed; only the Flash wrapper (a dead technology) was dropped.

## Non-content chrome noted, not saved to source/

- `Scripts/AC_RunActiveContent.js` — Dreamweaver Flash-detection compatibility shim, no content.
- Google Custom Search embed (`google.com/custom` form) on Rental Info, Amenities, Activities,
  Bargains pages — third-party search widget, not site content.
- `http://weather.yahoo.com/forecast/USFL0043_f.html` "What is the weather now in Bonita
  Springs?" link on every page's sidebar — dead third-party service (Yahoo Weather forecast
  pages of this form no longer exist), not site content.
- PayPal "Pay Now" hosted-button form (hosted_button_id `PDFXT2QRDRNUL`) in the sidebar of every
  page — third-party payment widget; the underlying "pay by PayPal, credit card, or personal
  check" policy text is preserved as real content on the Rental Info page, but the embedded
  PayPal form itself was not reproduced (its continued validity was not verified).
- Personal, non-business links on the homepage: a 1965 Corvette transport video, four family/
  "Michelle" personal videos (`1BBchSite/...mov|mp4`), and two Avigilon CCTV software installer
  downloads "Files for Kathy Adgate" — not vacation-rental business content. See CHANGELOG.md
  for the judgment call.
- Per-page invisible white-on-white keyword-stuffing paragraph (identical boilerplate repeated
  on Rental Info, Amenities, Activities, and Bargains — `<font color="#FFFFFF">` text on a white
  background) — see content-notes.md and CHANGELOG.md.
- `<meta name="keywords">` long keyword-stuffing lists on every page — not visible content.
