# Two Rivers Motel and Cabins — Redesign Change Log

Source: https://www.tworiversmotelandcabins.com/ (crawled 2026-09-16, archived to `source/`).
Redesign built as static HTML/CSS/JS in this folder: `index.html`, `cabins.html`, `motel.html`,
`rates.html`, `activities.html`, `waterfalls.html`, `snowmobiling.html`, `orving.html`,
`paddling.html`, `seasonal-activities.html`, `winter-activities.html`,
`strange-and-unknown-things.html`, `local-establishments.html`, `our-story.html`,
`guest-reviews.html`, `sponsorships-community.html`, `contact.html`, `pine-house.html`,
`privacy-policy-accessibility.html`, plus `css/style.css`, `js/main.js`, and `images/`.

The source site is a modern 26-page Wix site with a nested mega-menu (Home / Stay / Explore /
About / Contact / Book Now & Check Reservation / Blog / Other Rentals). All real content was
kept; some very short or purely transactional source pages were consolidated onto a related
page rather than kept as their own thin page — see "Layout & navigation" below.

## Layout & navigation

The primary nav groups (Stay, Explore, About, Contact, Other Rentals) were clear and sensible,
so the redesign keeps that same information architecture and dropdown grouping. Two changes,
both consolidations of thin/duplicate pages rather than a reshuffle of real content:

- **Parking Information** (`/parking-and-other-info`, a single paragraph) is now a section on
  the **Rates & Policies** page instead of its own page.
- **Get Directions** (`/getdirections`) is now a section on the **Contact** page (`contact.html
  #directions`) instead of its own page, since both pages exist to answer "how do I reach you."
- **Contact Us about a Vacation Rental** (`/contact-us-about-a-vacation-rental`) is folded into
  **The Pine House** page as its own contact section (same fields, same Pine House phone number),
  since it only ever served Pine House inquiries.
- The site's booking engine (`/reservations`, `/check-vacation-rental-reservations`,
  `/reservationcheck`) is a third-party Sirvoy widget with live availability and payment
  processing. A static redesign cannot reproduce a real payment/availability system, so every
  "Check Availability & Book Now" button links out to the live site's real booking pages
  (marked as external links) rather than a fabricated booking UI.
- The **Blog** is frequently-updated dynamic content outside a one-time redesign's scope; the
  header/footer nav item was intentionally left off rather than linking to a blog that would go
  stale. (Two blog posts are referenced as further reading from the ORVing and Spring/Summer/Fall
  Activities pages, per the source content, and link to the live site's posts.)

Every other page and nav label matches the source 1:1.

## Content preserved

- All body copy from every page, verbatim: hero copy, amenity lists, room/cabin descriptions,
  rates and policy tables, all FAQ Q&As (snowmobiling and ORVing), all activity guide text
  (waterfalls, seasonal activities, winter activities, paddling, strange & unknown things, local
  establishments, sponsorships), the full "Our Story" host bios, and all 10 featured guest
  reviews (verbatim quotes, names, and dates).
- All contact info: phone (906) 852-3541, Pine House phone 906-287-1144, text line
  (608) 235-9192, email tworiversmotelandcabins@gmail.com, address 2920 Old M-28, Trout Creek, MI
  49967 — 100% consistent across the source, reproduced identically with click-to-call added.
- All rates and fees: motel $95/night, cabins $115/night, linens $20/night, pet fee $10/night,
  discounts, cancellation windows, smoking/pet policies, check-in/out times, and the Pine House's
  separate rates and house rules.
- The **Trail Distances to Popular Destinations** table (37 towns, snowmobiling page) and the
  **Featured Water Trail Routes** table (19 river segments with put-in/take-out GPS coordinates,
  paddling page) — both live behind a client-side Wix "Table Master" app / paginated data
  repeater that returns no content to a plain HTTP crawl. Every row was read directly from the
  rendered page in a real browser and transcribed verbatim into a single scannable table (see
  `source/crawl-log.md` for how this was done).
- The real site logo, hero artwork, and every real business photo that a plain HTTP crawl could
  reach (60 images) — reused directly, resized/compressed for web, never replaced with stock.
  See the flagged limitation below for the individual room/cabin gallery photos.
- The Little Library flyer graphic, guest-review star ratings, and both the Booking.com and
  TripAdvisor award badges.

## Flagged limitation: individual room/cabin gallery photos (AGENTS.md rule 6)

Each Motel Room and Cabin section on the live site has its own small photo gallery (4–5 photos
per unit) rendered by a Wix "Pro Gallery" component inside a cross-origin, sandboxed iframe. This
content returns nothing to an HTTP crawl, and it is not scriptable from the parent page in a
browser either (cross-origin isolation blocks reading the iframe's DOM, and its images never
appeared in top-frame network traffic during testing). Rather than substitute stock photography
or fabricate images, the redesign reuses the real, verified photography that **is** reachable —
the log cabin exterior, a red cabin exterior, a cabin interior, a knotty-pine motel room, and
winter/summer exterior shots pulled from the homepage, reservations page, and rates page — as
shared representative imagery on the Cabins and Motel Rooms pages. No gallery section was
otherwise dropped, and no per-room photo was invented.

## Non-content chrome omitted (AGENTS.md rule 5)

- Small decorative Wix icon glyphs (Roku TV icon, hair dryer icon, Facebook/Instagram button
  icons, a small Little Library icon) — the emoji and inline SVG icons already used throughout
  the source copy (📺 🌀 📶 etc.) carry the same meaning without importing UI chrome images.
- The live site's cookie-consent/analytics scripts and Wix platform boilerplate.

## Contact forms

Both contact forms (`Contact Us` and `The Pine House`) on the live site post to a Wix backend
that a static GitHub Pages redesign has no server to receive. Per AGENTS.md ("Forms: only if the
source had one; keep the same fields and purpose"), both forms were rebuilt with the identical
fields (Name, Email, Phone, Message) as a `mailto:` form — submitting opens the visitor's email
client addressed to the business — rather than silently dropping the forms or wiring them to a
service the business never asked for.

## Design

Palette drawn from the business's own black-and-white circular logo badge (which includes a
small barn-red cabin icon) and the site's existing forest-green header — deep forest green for
the header/footer, warm cream page background, and the same barn red as an accent/CTA color,
tightened into a single consistent system across all 19 pages. Serif display type (Fraunces) for
headings reads as a warm lodge letterhead; a readable serif body (Newsreader) keeps the long
rate tables, FAQs, and trail guides comfortable to read. Mobile-first and fully responsive, with
a collapsing mobile nav, click-to-call phone numbers throughout, and the two client-side data
tables (trail distances, paddling routes) rebuilt as plain scannable HTML tables instead of a
paginated widget.
