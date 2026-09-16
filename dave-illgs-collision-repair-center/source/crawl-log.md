# Crawl log — dicrc.com (Dave Illg's Collision Repair Center)

Crawled: 2026-09-16
Method: breadth-first from https://www.dicrc.com/, `curl -s -A "Mozilla/5.0"`, same-domain (dicrc.com) links only. External domains (customerlobby.com, maps.google.com) were identified but not fetched, per task instructions.

## Pages (HTML)

| # | URL | Saved to | Status | Notes |
|---|-----|----------|--------|-------|
| 1 | https://www.dicrc.com/ | source/html/index.html | 200 OK | Homepage |
| 2 | https://www.dicrc.com/Default.htm | source/html/Default.htm | 200 OK | Byte-for-byte identical to `/` (index). Nav "Home" link points here. Duplicate content, not a separate page. |
| 3 | https://www.dicrc.com/Services.htm | source/html/Services.htm | 200 OK | |
| 4 | https://www.dicrc.com/PhotoGallery.htm | source/html/PhotoGallery.htm | 200 OK | Main gallery index (12 thumbnails) |
| 5 | https://www.dicrc.com/Hours%26Directions.htm | source/html/Hours&Directions.htm | 200 OK | Nav label "Hours & Directions"; literal filename has `&` |
| 6 | https://www.dicrc.com/FAQ.htm | source/html/FAQ.htm | 200 OK | 5 Q&A pairs |
| 7 | https://www.dicrc.com/feedback.html | source/html/feedback.html | 200 OK | Third-party "Freedback.com" form (POST to freedback.com) |
| 8 | https://www.dicrc.com/pages/dicrc%20023.htm | source/html/pages/dicrc 023.htm | 200 OK | Photo gallery lightbox page 1 of 12 |
| 9 | https://www.dicrc.com/pages/dicrc%20024.htm | source/html/pages/dicrc 024.htm | 200 OK | Lightbox page 2 |
| 10 | https://www.dicrc.com/pages/dicrc%20025.htm | source/html/pages/dicrc 025.htm | 200 OK | Lightbox page 3 |
| 11 | https://www.dicrc.com/pages/dicrc%20026.htm | source/html/pages/dicrc 026.htm | 200 OK | Lightbox page 4 |
| 12 | https://www.dicrc.com/pages/dicrc%20027.htm | source/html/pages/dicrc 027.htm | 200 OK | Lightbox page 5 |
| 13 | https://www.dicrc.com/pages/dicrc%20028.htm | source/html/pages/dicrc 028.htm | 200 OK | Lightbox page 6 |
| 14 | https://www.dicrc.com/pages/dicrc%20029.htm | source/html/pages/dicrc 029.htm | 200 OK | Lightbox page 7 |
| 15 | https://www.dicrc.com/pages/dicrc%20030.htm | source/html/pages/dicrc 030.htm | 200 OK | Lightbox page 8 |
| 16 | https://www.dicrc.com/pages/dicrc%20031.htm | source/html/pages/dicrc 031.htm | 200 OK | Lightbox page 9 |
| 17 | https://www.dicrc.com/pages/dicrc%20032.htm | source/html/pages/dicrc 032.htm | 200 OK | Lightbox page 10. PhotoGallery.htm's href to this page is NOT percent-encoded (`pages/dicrc 032.htm`, literal space) while the rest use `%20` — both resolve fine, noted as sloppy/inconsistent markup |
| 18 | https://www.dicrc.com/pages/dicrc%20033.htm | source/html/pages/dicrc 033.htm | 200 OK | Lightbox page 11 |
| 19 | https://www.dicrc.com/pages/dicrc%20034.htm | source/html/pages/dicrc 034.htm | 200 OK | Lightbox page 12 (last photo). Same literal-space href quirk as #17 |
| 20 | https://www.dicrc.com/Photo%20Gallery/index.htm | source/html/Photo Gallery/index.htm | 200 OK | Orphaned/duplicate Adobe Photoshop "Web Photo Gallery" auto-generated index. Linked only from an empty anchor (`../Photo Gallery/index.htm#2`) inside each lightbox page, not from main nav. Only lists 11 of the 12 photos (missing dicrc 034) — stale/incomplete duplicate of PhotoGallery.htm. Treated as non-content chrome; PhotoGallery.htm is the real, complete gallery page used in nav. |

**External links found, not crawled (different domain, per instructions):**
- `https://www.customerlobby.com/reviews/23341/dave-illg-s-collision-repair/` (review widget link, homepage)
- `https://www.customerlobby.com/ctrack-23341` and `https://www.customerlobby.com/img/23341/compact/` (tracking pixel + badge image embedded on homepage)
- `http://maps.google.com/maps?...` (embedded iframe map + "View Larger Map" link, Hours & Directions page)
- `mailto:djillg@dicrc.com` (not a page)

Total internal pages found: 20 (all fetched successfully, 0 failures)
Real unique content pages: 18 (Default.htm is a duplicate of index.html; Photo Gallery/index.htm is an orphaned duplicate/stale gallery index)

## Images

| # | URL | Saved to | Status |
|---|-----|----------|--------|
| 1 | https://www.dicrc.com/Header.jpg | source/images/Header.jpg | 200 OK |
| 2 | https://www.dicrc.com/Vertical%20Spacer.jpg | source/images/Vertical Spacer.jpg | 200 OK |
| 3 | https://www.dicrc.com/spacer.gif | source/images/spacer.gif | 200 OK |
| 4 | https://www.dicrc.com/Photos/dicrc%20027.jpg | source/images/Photos/dicrc 027.jpg | 200 OK — large (1.1MB) full-resolution homepage photo, distinct file from gallery's dicrc 027.jpg |
| 5 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20023.jpg | source/images/Photo Gallery/images/dicrc 023.jpg | 200 OK |
| 6 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20024.jpg | source/images/Photo Gallery/images/dicrc 024.jpg | 200 OK |
| 7 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20025.jpg | source/images/Photo Gallery/images/dicrc 025.jpg | 200 OK |
| 8 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20026.jpg | source/images/Photo Gallery/images/dicrc 026.jpg | 200 OK — same file also used inline on homepage ("Owner David Illg") |
| 9 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20027.jpg | source/images/Photo Gallery/images/dicrc 027.jpg | 200 OK — gallery-resolution version, smaller than images/Photos/dicrc 027.jpg |
| 10 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20028.jpg | source/images/Photo Gallery/images/dicrc 028.jpg | 200 OK |
| 11 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20029.jpg | source/images/Photo Gallery/images/dicrc 029.jpg | 200 OK |
| 12 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20030.jpg | source/images/Photo Gallery/images/dicrc 030.jpg | 200 OK |
| 13 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20031.jpg | source/images/Photo Gallery/images/dicrc 031.jpg | 200 OK |
| 14 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20032.jpg | source/images/Photo Gallery/images/dicrc 032.jpg | 200 OK |
| 15 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20033.jpg | source/images/Photo Gallery/images/dicrc 033.jpg | 200 OK |
| 16 | https://www.dicrc.com/Photo%20Gallery/images/dicrc%20034.jpg | source/images/Photo Gallery/images/dicrc 034.jpg | 200 OK |
| 17–28 | https://www.dicrc.com/Photo%20Gallery/thumbnails/dicrc%20023.jpg … dicrc%20034.jpg (12 files) | source/images/Photo Gallery/thumbnails/dicrc 023.jpg … 034.jpg | 200 OK (all 12) |
| 29 | https://www.dicrc.com/Photo%20Gallery/images/previous.gif | source/images/Photo Gallery/images/previous.gif | 200 OK — lightbox nav arrow icon |
| 30 | https://www.dicrc.com/Photo%20Gallery/images/next.gif | source/images/Photo Gallery/images/next.gif | 200 OK — lightbox nav arrow icon |
| 31 | https://www.dicrc.com/Photo%20Gallery/images/home.gif | source/images/Photo Gallery/images/home.gif | 200 OK — lightbox nav "home" icon |

Total unique internal image URLs found: 31. All 31 downloaded successfully. 0 failures.

**Not downloaded (external domain, per instructions):**
- `https://www.customerlobby.com/ctrack-23341` (1x1 hidden tracking pixel)
- `https://www.customerlobby.com/img/23341/compact/` (Customer Lobby review badge image, homepage)

**Not an image (script asset, not fetched — not content):**
- `Scripts/AC_RunActiveContent.js` — loaded on every page, boilerplate FrontPage/Dreamweaver Active Content shim, not business content.

## Summary
- Pages found: 20 internal URLs (18 unique content pages + 1 exact duplicate + 1 orphaned/stale duplicate index). All 20 fetched, 0 failures.
- Images found: 31 internal image URLs. All 31 fetched, 0 failures.
- No 404s, timeouts, or other errors encountered anywhere in the crawl.
