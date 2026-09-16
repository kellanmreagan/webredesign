# Crawl log — skippersgoodfood.com (Skipper's Restaurant)

Crawled: 2026-09-16
Method: manual fetch from http://www.skippersgoodfood.com/, `curl -s -A "Mozilla/5.0"`, plus a browser pass to render JS-injected content (hero image) and resolve the obfuscated mailto link. Same-domain links only.

## Pages (HTML)

| # | URL | Saved to | Status | Notes |
|---|-----|----------|--------|-------|
| 1 | http://skippersgoodfood.com/ | source/html/index.html | 200 OK | Only real HTML page on the site. |

The site's nav has 3 items — Home, Menu, Contact Us — but only Home is an actual page:
- **Menu** links directly to a PDF (`templates/skippersgoodfood.com/includes/Skippers-2025-Menu.pdf`), not an HTML page.
- **Contact Us** is a `mailto:` link (hex-entity obfuscated in the source), not a page: decodes to `mailto:info@skippersgoodfood.com?subject=Website Contact Request from skippersgoodfood.com`.

Confirmed no `menu.html` or `contact.html` exist on the live site (both return 404); `copycred.php` (footer copyright link) returns 200 but is a Brooks-Jeffrey Marketing CMS credit-page stub, not business content.

## Menu PDF

| # | URL | Saved to | Status | Notes |
|---|-----|----------|--------|-------|
| 1 | http://skippersgoodfood.com/templates/skippersgoodfood.com/includes/Skippers-2025-Menu.pdf | source/pdf/Skippers-2025-Menu.pdf | 200 OK | 4 pages: cover/story, Skippetizers+Burgers+Soups&Salads+Sides+Desserts+Beverages, Catfish+Entrees, Breakfast. Full text transcribed in content-notes.md. |

## Images

| # | URL | Saved to | Status | Notes |
|---|-----|----------|--------|-------|
| 1 | .../images/logo.png | source/images/logo.png | 200 OK | Site logo — catfish illustration + "Skipper's Restaurant" wordmark |
| 2 | .../images/home-photo.jpg | source/images/home-photo.jpg | 200 OK | Hero photo, injected via JS into `#site_rotate` (only image actually used — a "rotator" with 3 more images exists in main.js but is commented out) |
| 3 | .../images/3plates.png | source/images/3plates.png | 200 OK | 3-photo food collage (salad, waffle, fried fish plate), alt "Good Food" |
| 4 | .../images/facebook.png | source/images/facebook.png | 200 OK | Facebook icon |
| 5 | .../images/go.png | source/images/go.png | 200 OK | Decorative "Go" arrow button icon, used twice (Menu CTA, Contact CTA) |
| 6 | .../images/dshadow_one.jpg | source/images/dshadow_one.jpg | 200 OK | Decorative drop-shadow strip graphic (template chrome, not content) |
| 7 | .../images/dshadow_two.jpg | source/images/dshadow_two.jpg | 200 OK | Decorative drop-shadow strip graphic (template chrome, not content) |
| 8 | .../images/spacer.jpg | source/images/spacer.jpg | 200 OK | 1x78 transparent-ish spacer gif-equivalent, layout chrome only |
| 9 | .../images/bjm.jpg | source/images/bjm.jpg | 200 OK | "Site Design & Hosting by BJM" — third-party template vendor's own credit logo, not Skipper's content |
| — | .../favicon.ico, .../apple-touch-icon.png | — | 404 | Referenced by convention in `<head>` comment but not actually present on the server |

Total unique internal image URLs found: 9 (+1 PDF). All fetched successfully, 0 failures (excluding the 2 favicon paths that 404, which were never linked, just conventionally commented).

## Summary
- Pages found: 1 real HTML page (Home). Menu and Contact nav items point to a PDF and a mailto link, not pages.
- 1 menu PDF crawled and transcribed in full.
- Images found: 9 internal image URLs, all fetched, 0 failures. 2 are pure third-party template chrome (drop shadows, BJM vendor logo) with no business content.
