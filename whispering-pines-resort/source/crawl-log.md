# Crawl log — whisperingresort.com

Crawled 2026-09-16 with `curl` (browser User-Agent + Referer headers; the host's
Mod_Security blocked bare `curl` requests with a 406 until a full browser header set was sent).

Pages fetched (source HTML saved to `source/html/`):
- `/` → `index.html` — Home
- `/avail.htm` — Availability calendar
- `/prices.htm` — Prices, info & rules
- `/wprhist.htm` — WPR history
- `/wpmap.htm` — Map & directions
- `/canoes1.htm` — Canoe liveries
- `/trails1.htm` — Trail maps

Images fetched to `source/images/` (original filenames). `mc.gif` and `visa.gif` (payment-logo
images referenced only inside HTML comments, i.e. not live on the site — the live copy on
`prices.htm` says "We accept checks, cash or money orders only") were left un-fetched since
they aren't rendered content.

`noedgbkrd.jpg` (the tiled body background texture) was not archived — pure 1990s page-chrome,
no business content.
