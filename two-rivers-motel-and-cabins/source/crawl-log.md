# Two Rivers Motel and Cabins — Crawl Log

Source: https://www.tworiversmotelandcabins.com/ — crawled 2026-09-16.

## Method

The site is built on Wix and server-side renders full page content, so pages were fetched with
a plain HTTP GET (`curl`) rather than a headless browser, which is faster and sufficient for
nearly everything. `pages-sitemap.xml` was used to enumerate every real page (26 URLs, excluding
the blog sitemap). Each page's rendered text was extracted from the `<main>` element, and every
`static.wixstatic.com/media/...` image reference was collected, deduplicated by media ID, and
downloaded at full original resolution to `source/images/`.

## Pages crawled (24, excluding the blog and its per-post URLs)

/, /motel, /cabins, /thepinehouse, /rates-deposits-policies, /parking-and-other-info,
/winterinfo, /activities, /waterfalls, /snowmobiling, /paddling-adventures-western-up, /orving,
/spingsummerfallactivities, /strangeandunknownthings, /local-establishments,
/sponsorships-community, /our-story, /guest-reviews, /contact-us, /getdirections, /reservations,
/check-vacation-rental-reservations, /reservationcheck, /privacy-policy-and-accessibility,
/contact-us-about-a-vacation-rental

Raw fetched HTML for each is archived in `source/html/`.

## Two client-side widgets that a plain HTTP crawl cannot see

Two pages embed a Wix "Table Master" app as a same-origin-but-JS-rendered `<iframe>` with no
data present in the initial HTML response — only an empty `<iframe>` tag:

1. **Snowmobiling page** — "Trail Distances to Popular Destinations (from Kenton, MI)" — a
   37-row city/mileage table.
2. **Paddling Adventures page** — a paginated (5-page) repeater of MI-TRALE water-trail route
   cards, 19 routes total, each with river, segment, max difficulty, length, notes, and put-in/
   take-out GPS coordinates.

For both, the actual data was read directly out of a real rendered browser session (scrolling to
each table/page and reading the visible rows) and transcribed by hand into the notes below and
then into the redesign's own plain HTML `<table>` markup. This is the one place in the crawl
where "the crawl" means "read it in a browser and copied it down" rather than an automated
`curl` — flagged here for transparency since it's a different process than the rest of the site.

## Known gap: per-room/cabin photo galleries

The Cabins and Motel Rooms pages each show a small photo gallery per unit (Wix "Pro Gallery"),
rendered inside a **cross-origin sandboxed iframe** (`static.parastorage.com/.../Thumbnails.html`)
that loads its image list via an internal API call the parent page/crawl never sees. This was
confirmed by inspecting the live DOM (`document.querySelectorAll('iframe')` on `/motel` returns
several `static.parastorage.com` gallery iframes, cross-origin from `tworiversmotelandcabins.com`)
and by watching network traffic while manually scrolling through every room — no per-photo image
URL was ever observed outside that iframe. These individual room/cabin gallery photos could not
be retrieved. See `CHANGELOG.md` for how the redesign handled this (reusing the real,
independently-reachable lodging photography instead of stock images).

## Images

65 unique `static.wixstatic.com` media items were found across all crawled pages. 60 are real
business photography/graphics and were downloaded at original resolution to `source/images/`
(full-size, unedited — the versions in the live site's `images/` folder are resized/recompressed
copies for web delivery). 5 were small decorative Wix UI icon glyphs (Roku TV icon, hair dryer
icon, Little Library icon, Facebook icon, Instagram icon) and were intentionally not carried
into the redesign — see `CHANGELOG.md`, "Non-content chrome omitted."
