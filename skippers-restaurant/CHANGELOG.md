# Skipper's Restaurant — Redesign Change Log

Source: http://www.skippersgoodfood.com/ (crawled and archived to `source/`). Redesign built as static
HTML/CSS/JS in this folder: `index.html`, `menu.html`, `contact.html`, plus `css/style.css`,
`js/main.js`, `images/`, and a copy of the original menu PDF (`Skippers-2025-Menu.pdf`).

## Layout & navigation — kept, with two pages added

The source site's 3-item nav (Home / Menu / Contact Us) was clear and is kept exactly as-is.
However, per AGENTS.md rule 2, only "Home" was an actual page on the source site — "Menu" linked
straight to a PDF download and "Contact Us" was just a `mailto:` link with no page behind it at
all (see `source/crawl-log.md`). That's thin IA, especially on mobile where a `mailto:` link can
silently do nothing if no mail app is configured. The redesign keeps the same 3 nav labels and
order, but gives Menu and Contact Us real pages:
- `menu.html` — the full PDF menu transcribed to accessible, scannable HTML (every item, every
  price, verbatim), with the original PDF still linked for anyone who wants to download/print it.
- `contact.html` — phone, address, email, Facebook, hours table, and an embedded map, using the
  same contact details that were already on the homepage and in the footer.

## Content preserved

- Homepage body copy carried over verbatim: the "Skipper's Restaurant is a family owned and
  operated restaurant..." paragraph, "We've GOT FISH at Skipper's!", the "Voted BEST CATFISH in
  Town!" badge, and the "Visit Skipper's Restaurant TODAY!" hours callout.
- The entire menu, transcribed item-for-item from the source PDF: Skippetizers, Burgers & More,
  Soups & Salads, Sides, Desserts, Beverages, Farm-Raised American Catfish, Skipper's Entrees, and
  the full Skipper's Breakfast section (Breakfast Plates, Specialties, Omelets, Pancakes Etc.,
  Little Skipper, Breakfast Sides) — every item name, description, and price, including the
  raw/undercooked-food notice and the `*` markers it applies to.
- "The Story Behind Skipper's Name" — the black Labrador story from the menu PDF's cover — added
  to `menu.html`, the page that already links to that PDF. This is genuine, unaltered,
  owner-authored business content already published by the business (see `source/content-notes.md`
  item 2 for the reasoning), not invented copy.
- All 3 real business photos reused directly: the site logo (catfish illustration + "Skipper's
  Restaurant" wordmark), the "got fish?" yellow t-shirt hero photo, and the 3-photo food collage
  (salad, waffle, fried fish plate). No stock photography substituted.
- Contact details: phone (870) 508-4574 (click-to-call throughout), address 711 Hwy. 5 North,
  Mountain Home, Arkansas 72653, email info@skippersgoodfood.com (decoded from the source's
  hex-obfuscated mailto link, same address and subject line preserved), and the Facebook page link.
- "Call in for Carry Out" messaging from the menu PDF, surfaced on both the Menu and Contact pages.

## Content oddity flagged, not resolved (AGENTS.md rule 6)

The homepage states hours as **Sat–Thurs 7am–2pm, Fri 7am–8pm** (extended hours Friday only); the
menu PDF's cover states **Sun–Thurs 7am-2pm, Fri–Sat 7am-8pm** (extended hours Friday **and**
Saturday). These conflict specifically on Saturday evening availability. The redesign uses the
website's version everywhere (homepage hours card, footer, and the Contact page hours table),
since that's the page of record being redesigned — **flagging for the business owner:** please
confirm whether Saturday has extended (7am–8pm) or standard (7am–2pm) hours, and I'll update all
three places to match.

## Non-content chrome omitted (per AGENTS.md rule 5)

- Two decorative drop-shadow strip graphics (`dshadow_one.jpg`, `dshadow_two.jpg`) and a 1×78
  layout spacer image — pure template chrome, no business content.
- The "Site Design & Hosting by BJM" vendor credit logo (`bjm.jpg`) — a third-party template
  provider's own ad for their service, not Skipper's content.

## Design

Palette pulled directly from the site's own logo and menu graphics (bright yellow, red, near-black)
rather than introducing a new brand identity — matches the "family diner" personality called for in
AGENTS.md. A bold, rounded display face (Baloo 2) echoes the hand-lettered, playful tone of the
logo and menu headers ("Skippetizers," "Skipper's Entrees") without copying the exact source
typeface; body copy uses Open Sans, the same family the source site already loaded. The menu page
uses a classic dotted-leader price-list layout (item — · · · · · — price) for scannability at
90+ items. Mobile-first, fully responsive, click-to-call phone numbers throughout, and a real
Contact page with an embedded map in place of the source's mailto-only link.
