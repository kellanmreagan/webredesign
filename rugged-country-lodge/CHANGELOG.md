# Rugged Country Lodge redesign — change log

## Layout / nav

Kept the source information architecture and labels:

- Home, Rooms (Single Room, Double Room, Mini Suite, Standard Suite), About Us (Our History, Our Story, Amenities, Mission Statement), Location, Photo Gallery, Policies, Contact
- Footer Privacy Statement and Accessibility Statement
- Primary conversion remains Book / Call

Refined spacing, typography, and mobile behavior only. Did not invent pages or rename nav items. Contact was in the header on the source; it is in the primary nav here so it is reachable on every page.

On screens 760px and under, the header phone link and Book Now button stay visible beside the menu (wordmark beside the logo stays hidden so the name is not repeated). Privacy Statement and Accessibility Statement are the current footer links on those pages; Home is not marked current there.

The rooms listing shows the live page’s room names, photos, and links only. Sleep lines stay on the individual room pages, where the live site has them, and are not repeated on the listing.

## Content / headlines / media

- All source body copy, headlines, subheads, policies, hours, fees, staff name, contact details, and legal lines are preserved as written (including original punctuation and wording).
- All source photos, the wordmark logo, Google mark, and favicon are downloaded into `images/` and reused. Gallery interiors and Property photos are all present.
- Room intro lines, amenity lists, and photo alts follow the live pages (including the Double Room page’s on-page intro, which currently matches the Single Room wording).
- Meta titles/descriptions reuse the source text. The Standard Suite title’s leftover “Astoria, OR” (Fisher Bros location) was corrected to Pendleton, OR.

## Booking / leftover branding (tech debt, omitted)

- Removed the nav “Book Now” URL `hotels.cloudbeds.com/reservation/N9H4Cz` (Fisher Bros Flats Cloudbeds).
- Removed leftover `the-flats` aliases (`data-target-page-alias`, `runtime_url` paths).
- Removed the homepage newsletter form’s hidden “Fisher Bros. Flats” autoreply-from value.
- Book Now now uses the source’s valid Rugged Country Lodge engine: `https://book.bookingcenter.com/03/?site=RUGGED` (confirmed on the live header button; the BookingCenter page is titled for Rugged Country Lodge in Pendleton). No new booking URL was invented.

## Non-content chrome omitted

- Duda/cdn-website chrome: “Add your custom HTML here”, placeholder “Button” / “Slide title” / “Write your caption here”
- AudioEye widget, and the Accessibility Statement sentences that claimed the widget, its corner menu, and the AudioEye scanner were in use. Remaining statement copy is unchanged. No replacement widget was added.
- Flash/marquee/IE-era artifacts (none present as content)
- Third-party Duda form endpoints; contact and newsletter keep the same fields and send via the lodge email `info@ruggedcountrylodge.com`
