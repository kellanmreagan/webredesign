# Crawl log — Frontier Lodge (frontierlodge.com)

Crawled 2026-09-16, breadth-first from https://www.frontierlodge.com/, following every
internal (frontierlodge.com) link found on any fetched page. All fetches used
`curl -A "Mozilla/5.0"`.

Crawl queue trace: started at `/` (index.html), which linked to 6 pages (fishing.html,
rates.html, location.html, snowmobiling.html, bearhunting.html, moosehunting.html). Each
of those 6 pages was fetched and scanned for additional internal links; each one's only
internal links were the same 6 nav pages + index.html (all already visited/queued) —
no new internal pages were discovered anywhere on the site. Two external domains were
seen as link targets and intentionally NOT crawled per task instructions:
`http://www.duenorth.net` (site designer's own site, footer credit link on index.html),
`http://www.ontariofishingnetwork.com/` (fishing.html footer badge), and
`http://fednor.ic.gc.ca` (badge link on rates.html/location.html/snowmobiling.html/bearhunting.html,
a Canadian federal agency, not the business's own content).

## Pages (7 total — all found, all fetched successfully)

- PAGE https://www.frontierlodge.com/ -> html/index.html (HTTP 200, 8162 bytes)
- PAGE https://www.frontierlodge.com/fishing.html -> html/fishing.html (HTTP 200, 4966 bytes)
- PAGE https://www.frontierlodge.com/rates.html -> html/rates.html (HTTP 200, 13446 bytes)
- PAGE https://www.frontierlodge.com/location.html -> html/location.html (HTTP 200, 4211 bytes)
- PAGE https://www.frontierlodge.com/snowmobiling.html -> html/snowmobiling.html (HTTP 200, 5084 bytes)
- PAGE https://www.frontierlodge.com/bearhunting.html -> html/bearhunting.html (HTTP 200, 5669 bytes)
- PAGE https://www.frontierlodge.com/moosehunting.html -> html/moosehunting.html (HTTP 200, 4937 bytes)

No other internal pages exist/were linked anywhere on the site (no gallery, cottages,
ice-fishing, testimonials, or other pages found despite thorough link-checking on every
page). The site is exactly these 7 pages.

## Images (36 unique images found across all 7 pages — all fetched successfully)

- IMG https://www.frontierlodge.com/b14_13.jpg -> images/b14_13.jpg (HTTP 200, 3124 bytes) [tiled page-background texture, used on all 7 pages]
- IMG https://www.frontierlodge.com/largelogo.gif -> images/largelogo.gif (HTTP 200, 23827 bytes) [main logo, all pages]
- IMG https://www.frontierlodge.com/smalllogo.gif -> images/smalllogo.gif (HTTP 200, 5598 bytes) [host-block small logo, all pages]
- IMG https://www.frontierlodge.com/noto.gif -> images/noto.gif (HTTP 200, 1913 bytes) [NOTO badge, all pages]
- IMG https://www.frontierlodge.com/lilldue.gif -> images/lilldue.gif (HTTP 200, 1528 bytes) [designer-credit logo, all pages]
- IMG https://www.frontierlodge.com/lodge1.jpg -> images/lodge1.jpg (HTTP 200, 25547 bytes) [index.html]
- IMG https://www.frontierlodge.com/newpond1.jpg -> images/newpond1.jpg (HTTP 200, 11837 bytes) [index.html]
- IMG https://www.frontierlodge.com/cabin1.jpg -> images/cabin1.jpg (HTTP 200, 15342 bytes) [index.html]
- IMG https://www.frontierlodge.com/cabin2.jpg -> images/cabin2.jpg (HTTP 200, 15063 bytes) [index.html]
- IMG https://www.frontierlodge.com/cabin3.jpg -> images/cabin3.jpg (HTTP 200, 15127 bytes) [index.html]
- IMG https://www.frontierlodge.com/cabin4.jpg -> images/cabin4.jpg (HTTP 200, 14121 bytes) [index.html]
- IMG https://www.frontierlodge.com/cabin5.jpg -> images/cabin5.jpg (HTTP 200, 11372 bytes) [index.html]
- IMG https://www.frontierlodge.com/cabin6.jpg -> images/cabin6.jpg (HTTP 200, 8728 bytes) [index.html]
- IMG https://www.frontierlodge.com/campfire1.jpg -> images/campfire1.jpg (HTTP 200, 13507 bytes) [index.html]
- IMG https://www.frontierlodge.com/beach1.jpg -> images/beach1.jpg (HTTP 200, 14930 bytes) [index.html]
- IMG https://www.frontierlodge.com/kids1.jpg -> images/kids1.jpg (HTTP 200, 14788 bytes) [index.html]
- IMG https://www.frontierlodge.com/view2.jpg -> images/view2.jpg (HTTP 200, 21216 bytes) [fishing.html]
- IMG https://www.frontierlodge.com/map3.jpg -> images/map3.jpg (HTTP 200, 55715 bytes) [fishing.html]
- IMG https://www.frontierlodge.com/jumpfish.gif -> images/jumpfish.gif (HTTP 200, 8115 bytes) [fishing.html]
- IMG https://www.frontierlodge.com/ofn.jpg -> images/ofn.jpg (HTTP 200, 2701 bytes) [fishing.html, Ontario Fishing Network badge — image hosted locally though it links out]
- IMG https://www.frontierlodge.com/fire1.gif -> images/fire1.gif (HTTP 200, 5442 bytes) [rates.html]
- IMG https://www.frontierlodge.com/fednor.gif -> images/fednor.gif (HTTP 200, 5716 bytes) [rates.html, location.html, snowmobiling.html, bearhunting.html — FEDNOR badge, image hosted locally though it links out]
- IMG https://www.frontierlodge.com/map1.jpg -> images/map1.jpg (HTTP 200, 15456 bytes) [location.html]
- IMG https://www.frontierlodge.com/jeep.gif -> images/jeep.gif (HTTP 200, 20324 bytes) [location.html]
- IMG https://www.frontierlodge.com/newsnowmobile1.gif -> images/newsnowmobile1.gif (HTTP 200, 42993 bytes) [snowmobiling.html]
- IMG https://www.frontierlodge.com/newsnowmobile2.gif -> images/newsnowmobile2.gif (HTTP 200, 39913 bytes) [snowmobiling.html]
- IMG https://www.frontierlodge.com/newsnowmobile3.gif -> images/newsnowmobile3.gif (HTTP 200, 41396 bytes) [snowmobiling.html]
- IMG https://www.frontierlodge.com/newlodge1.gif -> images/newlodge1.gif (HTTP 200, 39733 bytes) [snowmobiling.html]
- IMG https://www.frontierlodge.com/gas.gif -> images/gas.gif (HTTP 200, 1445 bytes) [snowmobiling.html]
- IMG https://www.frontierlodge.com/newsmallmap1.jpg -> images/newsmallmap1.jpg (HTTP 200, 28728 bytes) [snowmobiling.html, thumbnail]
- IMG https://www.frontierlodge.com/newbigmap1.jpg -> images/newbigmap1.jpg (HTTP 200, 85972 bytes) [snowmobiling.html, full-size map linked from thumbnail above]
- IMG https://www.frontierlodge.com/skidoo.gif -> images/skidoo.gif (HTTP 200, 21902 bytes) [snowmobiling.html]
- IMG https://www.frontierlodge.com/newbear1.gif -> images/newbear1.gif (HTTP 200, 41006 bytes) [bearhunting.html]
- IMG https://www.frontierlodge.com/blackbeartent.gif -> images/blackbeartent.gif (HTTP 200, 7281 bytes) [bearhunting.html]
- IMG https://www.frontierlodge.com/newmoose1.gif -> images/newmoose1.gif (HTTP 200, 38836 bytes) [moosehunting.html]
- IMG https://www.frontierlodge.com/anielg.gif -> images/anielg.gif (HTTP 200, 18700 bytes) [moosehunting.html]

All 36 unique image URLs found across the site returned HTTP 200 and were saved to
source/images/ with their original filenames preserved exactly. No images failed to
download; no broken image links (404s) were encountered on any page.

## Notes on the crawl process

- First attempt at bulk-downloading all images via a single backgrounded shell for-loop
  produced no output and no files after several minutes (likely an issue with the
  background-execution environment for long-running loops, not a site/network problem —
  individual foreground `curl` calls to the same URLs completed in well under a second
  each). Recovered by re-running every image download as its own individual foreground
  `curl` call; all 36 succeeded on first try this way. Verified afterward: no zero-byte
  files, no stray/duplicate files left behind in source/ from the aborted attempt.
- No robots.txt restrictions encountered; no authentication/paywall; no JavaScript-rendered
  content (site is static FrontPage-era HTML, so a plain `curl` fetch captures full page
  content — no headless-browser rendering was needed).
