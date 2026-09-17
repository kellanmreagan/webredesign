# Barefoot On The Beach — Source Content Notes (verbatim)

Site crawled from http://www.barefootonthebeach.com/ on 2026-09-16. This file contains the
verbatim text content of every real page found, organized by page, for use as source-of-truth
in the redesign. Do not paraphrase from this file — copy exactly. See `crawl-log.md` for the
full list of fetches, HTTP statuses, and the case-sensitivity/broken-link anomalies found on
this server.

Business contact info (appears repeatedly, sometimes in different combinations, across pages):
- Phone: 239-287-2603 and 239-947-9728 — ask for Bill or Randi (the two numbers are always
  listed together but their order flips between pages: Home/Rental Info list 287-2603 first,
  Bargains lists 947-9728 first)
- Email (three distinct real addresses, each used in a different real spot on the source and
  preserved in that same spot in the redesign — see crawl-log.md for detail):
  - `barefoot@barefootonthebeach.com` — the horizontal nav's "Contact Us" mailto target on
    every page
  - `bill@barefootonthebeach.com` — the vertical sidebar nav's mailto/"Pay Now" image link
    on every page
  - `info@barefootonthebeach.com` — the "click here to contact us" reservation link on the
    Rental Info and Bargains pages
- Owners: Bill and Randi Zwicker ("Bill Zwicker, Randi Zwicker" in the homepage meta keywords;
  "call Bill or Randi" in every reservations table)
- Location: Beach and Tennis Club, Bonita Beach Rd, Bonita Springs, FL. The vertical sidebar's
  "Map to Resort" mapquest link resolves the street address as 5900 Bonita Beach Rd, Bonita
  Springs, FL 34134.
- Tennis info line (Amenities page only): 239-992-2345

---

## Home (served at `/` and `/index.html`; `/index.htm` 404s — see crawl-log.md)

Title: "Beautiful Bonita Beach Vacation Rental Condo at Beach and Tennis Club, Bonita Springs FL"

Meta description: "Rent a gold rated like new one bedroom efficiency condo apartment on Bonita
Beach near Barefoot Beach in Bonita Springs, Florida just north of Naples, Florida. Plenty of
activities, good restaurants and shopping, and outstanding accommodations. Check us out! This
is an outstanding value and rental rates are at a discount when rented directly through the
owner. Southwest Florida international airport is only 25 minutes away."

Heading graphic (`imgsbtns/IndexTitle.gif`, 590x160): "Barefoot On The Beach — Vacation Rentals
at Beach & Tennis Club, Bonita Beach, Florida — please call 239-287-2603 or 239-947-9728"

"One Bedroom Efficiency" / "Sorry, NO SMOKING, NO PETS"

Unit description: "The unit includes attractive seating in the main area, a king-size bed, high
speed Internet, a full kitchen for your gourmet enjoyment, safety grab bars in the shower, and a
flat screen TV with DVD player."

Beach ranking: "Barefoot Beach was rated 2 out of more than 600 beaches by Dr. Beach. Click here
for details. Last year it was #6!" (links to
http://www.today.com/travel/dr-beachs-top-beach-hint-its-hawaii-2D79687779)
"Delnor Wiggins State Park, immediately south of Barefoot Beach was #10."

Seasonal rate table (identical library-item table repeated on Home and Rental Info pages):
- PEAK SEASON: January 26, 2019 – March 1, 2019 (changeover day Saturday) — $1395/week
- HIGH SEASON: March 2, 2019 – April 12, 2019 (changeover day Saturday) — $1295/week
- LOW SEASON: April 13, 2019 – November 15, 2019 — $795/week
- MID SEASON: November 16, 2019 – December 20, 2019 (changeover day Saturday) — $895/week
- HIGH SEASON: December 21, 2019 – January 24, 2020 (changeover day Saturday) — $1295/week
- PEAK SEASON: January 25, 2020 – February 28, 2020 (changeover day Saturday) — $1395/week
- HIGH SEASON: February 29, 2020 – April 17, 2020 (changeover day Saturday) — $1295/week
- LOW SEASON: April 18, 2020 – November 20, 2020 — $795/week
- MID SEASON: November 21, 2020 – December 18, 2020 (changeover day Saturday) — $895/week
- HIGH SEASON: December 19, 2020 – January 29, 2021 (changeover day Saturday) — $1295/week
- PEAK SEASON: January 30, 2021 – March 5, 2021 (changeover day Saturday) — $1395/week
- HIGH SEASON: March 6, 2021 – April 2, 2021 (changeover day Saturday) — $1295/week

Terms: "One night's stay or 25% whichever is greater due upon reservation; Payment in full 30
days prior to check-in. Stays of 4 or more weeks are discounted by 10%."
"All of the above rates are for two people INCLUDE CLEANING!!! None of the above rates include
local taxes. Minimum stay is one week. Security Deposit of $300 required."
"Call 239-287-2603 or 239-947-9728 for reservations or information. Don't forget to ask for the
Internet Special."
Payment: "You may pay by using PayPal or a major credit card by clicking 'Pay Now' below. Of
course, we also accept your personal check." (PayPal hosted button id PDFXT2QRDRNUL)

Location paragraph: "Wouldn't you love to vacation just steps from Bonita Beach, one of the most
beautiful beaches in the world? Enjoy the Florida sunshine when you vacation in our beautifully
refurbished, non-smoking, vacation rental in Southwest Florida between Naples and Ft. Myers
Beach in Bonita Springs, Florida. Boating, kayaking, and canoeing are easily accessible. Many
restaurants are close by and the shopping is great!!! Very convenient to Ft. Myers International
Airport."

Nav (horizontal, bottom of page): "Home | Rental Info | Amenities | Activities | Map to Resort |
Bargains | Contact Us" — see crawl-log.md for which of these links actually resolve as coded on
the live source (two are broken/mis-cased).

Weather link (external, non-content chrome, omitted): "What is the weather now in Bonita
Springs?" → weather.yahoo.com.

Non-business items present on the live homepage (personal media/software links, not part of the
vacation-rental business — see judgment call in CHANGELOG.md): a 1965 Corvette video link, four
family/"Michelle" personal video links (.MOV/.mp4 files), and two Avigilon Control Center
installer download links "Files for Kathy Adgate" (unrelated CCTV software installers, clearly
left on the page by the site's current webmaster/owner for personal file-sharing, not vacation
rental content).

---

## Rental Info (`/Pages/rentalinfo/index.htm`, lowercase path — see crawl-log.md)

Title: "Rental Specials for vacation condo in Bonita Beach, Florida"

"INTERNET SPECIAL: When calling or writing, please make sure to mention that you want the
internet special to receive the rates listed below. Monthly rentals will save even more!"

"For Availability and Reservations:" table —
- call Bill or Randi: 239-287-2603 or 239-947-9728
- e-mail: "Please click here to contact us" → mailto:info@barefootonthebeach.com

Same seasonal rate table and terms as Home (see above), inside a `<a name="Rates">` anchor.

Location paragraph (visible, black text): "Vacation villa located in Lely Barefoot Beach also
known as Bonita Beach in Bonita Springs Florida near Naples Florida and Ft. Myers Beach and
Sanibel and Captiva Island. It is located in the Beach and Tennis Club on Bonita Beach Road. ...
The apartment is discounted thru the internet. It is owner owned and is a weekly rental, monthly
rental, with 3 day minimum." (Note: on this page this paragraph is rendered in white text —
`<font color="#FFFFFF">` — on a white background, i.e. invisible on screen; it is the same
keyword-stuffed boilerplate that repeats, also invisible, on the Amenities, Activities, and
Bargains pages. Treated as omittable SEO chrome per AGENTS.md rule 5 — see CHANGELOG.md.)

A Flash movie ("Click on image below to enlarge picture", `imgsbtns/RentalInfo.swf`) held a
photo slideshow. Flash is unsupported by modern browsers; its embedded photo references were
recovered from the .swf file's strings and re-fetched directly: `imgsbtns/bedroom.jpg`,
`imgsbtns/diningroom.jpg`, `imgsbtns/kitchen.jpg` (all real 1024x768 condo interior photos, now
in `source/images/`).

---

## Amenities (`/Pages/amenities/index.htm`)

Title: "Features and Amenities in vacation condo in Bonita Beach, FL"

- Beach: "Just steps west of the resort is Bonita Beach, a beautiful sandy white beach on the
  Gulf of Mexico. Charcoal grills are available for your use."
- Tennis: "The Club's har-tru clay tennis courts offer a complete program with organized play,
  tournaments, and private lessons. Tennis is free if staying at our condo. Please call
  239-992-2345 for more tennis information."
- Swimming: "Two heated swimming pools that are always inviting, refreshing, and relaxing are
  available."
- Bocci Ball: "Join in the Bocci Ball leagues and make new friends."
- Basketball: "A basketball hoop is available east of the tennis courts. A basketball can be
  checked out from the manager's office."
- Golf: "Bring your own clubs and balls to enjoy the chipping green which is located just west
  of the tennis courts."
- Barbecue Grills: "Two gas barbecue grills are located near the tennis court entrance."
- Schuffleboard [sic, kept verbatim]: "Schuffleboard is on site and equipment is available in
  the lobby."
- Horseshoes: "Horseshoes are on site and equipment is available in the lobby"

Flash slideshow (`imgsbtns/Amenities.swf`) photo references recovered: `Barefoot%20Beach%20
Preserve.jpg`, `BeachTennisClubAir.jpg`, `DelnoreWigginsPass.jpg`, `Lovers%20Key%20w%20car.jpg`,
`TennisCourts.jpg`.

Same invisible white-on-white boilerplate paragraph as Rental Info (omitted, see above).

---

## Activities (`/Pages/activities/index.htm`)

Title: "Activities near Bonita Beach in Southwest Florida"

Heading: "Nearby Attractions and Activities"

- Bonita Beach: "Simply cross the street from your vacation apartment to enjoy beautiful Bonita
  Beach. About 100 yards north on the beach is Doc's Beach House, a local favorite restaurant. A
  favorite activity of many residents is to walk either north or south on the beach and view the
  beautiful beachfront mansions. Enjoy happy hour in the restaurant or at the tables directly on
  the beach. Wave runners, man-powered boats, and para-sailing is available at Doc's. You can
  even enjoy your own picnic meals at the chicki-huts on the beach."
- Barefoot Beach Preserve: "Drive or bike to one of the most pristine beaches in the world only 1
  1/2 miles south of the resort.. Kayak and canoe rentals are available. See many species of
  wildlife including land tortoises and an occasional eagle. Harold Saylor, a former park
  ranger, guides a nature walk every Saturday morning at 9:00 am followed by a lecture. Nominal
  parking fee. HIGHLY RECOMMENDED!"
- Lovers Key / Carl Johnson State Park: "Travel only 5 miles north of the resort to the
  beachfront park on beautiful Lover's Key. Kayak and canoe rentals are available. Nominal
  parking fee."
- Delnor-Wiggins Pass State Recreational Area: "A beautiful beach front state park that was
  voted as a National Gold Medal Winner. Six miles south of the resort. Charcoal grills
  available. Nominal entrance Fee. HIGHLY RECOMMENDED!"
- Koreshan State Historical Site: "A historical park that houses the remnants of a religious
  sect that flourished during the late 19th and early 20th century."
- Kayaks and Canoe Rentals: "Barefoot Beach Preserve is 1/5 miles south on Barefoot Beach Blvd.
  Lovers Key State Park is located on Lover's Key 5 miles north on Hickory Blvd. Estero River
  Outfitters is located 10 miles north of the resort. Rent a kayak or canoe and paddle down the
  Estero River."
- Boating: "Cocohatchee River Park (4 miles southeast) for boat launching. Lovers Key (5 miles
  north) for boat launching. Lots of boat rental establishments too numerous to list."
- Miniature Golf: "Jungle Golf is located 1 mile east of resort on Bonita Beach Rd."
- Naples Pier: "A public pier that extends 1000 feet into the Gulf of Mexico and is great for
  fishing, sunning, and strolling. Sunsets are very popular. Pelicans are always present begging
  for fish scraps from the fishermen. (13 miles south) Free. HIGHLY RECOMMENDED"
- Ft. Myers Beach: "Restaurants, shopping, fun! A fishing pier (free) is on the northern part of
  the island."
- Sanibel and Captiva Islands: "Once a haven for pirates. My, how things have changed! Great
  restaurants, good shopping, and beautiful beaches make it a great place to visit. The islands
  have been developed with the environment in mind. A drive through Ding Darling Park, located
  on Sanibel Island, is worthwhile. There is a fee to drive across the causeway"
- Corkscrew Swamp Sanctuary: "From this 2 1/2 mile elevated wooden nature trail, wildlife can be
  viewed in its natural setting. Don't miss the wood storks nesting high in the trees and the
  alligators sleeping in the swamp. Entrance fee. HIGHLY RECOMMENDED!"
- Naples Zoo (formerly called Jungle Larry's and Carribean Gardens): "Acres of beautiful
  tropical plants and wild animals in captivity. Entrance fee."

Flash slideshow (`imgsbtns/Activities.swf`) photo references recovered: `BeachTennisClubAir.jpg`,
`TennisCourts.jpg`, `beachview.jpg`, `diningroom.jpg`, `sunset1.jpg`.

Same invisible white-on-white boilerplate paragraph as Rental Info (omitted, see above).

---

## Bargains (`/Pages/bargains/index.htm`)

Title: "Rental Discounts and Bargains in Bonita Beach, Florida"

"If you can travel at the last minute, there are some great deals here. Come back and check
often!!! These offers are only through the owner on the internet."

"These are 'Last minute Specials' (other dates are available at prices listed above)"
"Dates eligible for last minute specials are: None at this time / none"

"INTERNET SPECIAL: When calling or writing, please make sure to mention that you want the
internet special to receive the rates listed above."

"For Availability and Reservations:" table —
- call Bill or Randi: 239-947-9728 or 239-287-2603 (note: reversed order vs. Home/Rental Info)
- e-mail: "Please click here to contact us" → mailto:info@barefootonthebeach.com

Flash slideshow (`imgsbtns/LastMinuteBargains.swf`) photo references recovered:
`bedroom.jpg`, `kitchen.jpg`, `livingroom.jpg`.

Same invisible white-on-white boilerplate paragraph as Rental Info (omitted, see above).

---

## "Home" nav link bug (all pages)

Every page's horizontal-nav "Home" link points to `barefootartdesigns/index.htm` (or
`../../barefootartdesigns/index.htm` from subpages), which is a live 200-OK page — but its
`<title>` is "Barefoot Art Designs home page", a completely unrelated art/illustration business
site (paintings, murals, illustrations), not the vacation rental. This is a FrontPage-era
mislinked-template artifact, not real content for this business. See CHANGELOG.md for how this
was handled (link fixed to point to the real home page; the unrelated Barefoot Art Designs
content was not incorporated, since it belongs to a different business entirely).
