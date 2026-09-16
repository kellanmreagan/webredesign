# Content notes — dicrc.com (Dave Illg's Collision Repair Center)

Verbatim body content extracted from the live site, organized by page. Nothing paraphrased or reworded. HTML entities decoded for readability (e.g. `&amp;` → `&`, `&nbsp;` → space). Source HTML for every page lives in `source/html/`; treat this file as a readable index into that HTML, not a replacement for it.

Site-wide `<title>` (identical on every page): **Dave Illg's Collision Repair Center - Nashua, NH's finest Auto Body Shop**

Site-wide nav (identical on every page, header and footer): **Home | Services | Photo Gallery | Hours & Directions | FAQ | Feedback**

Site-wide footer block (identical on every page):
```
10 W Otterson St | Nashua, NH 03060
Phone: (603)204-5516 | Fax: (603)204-5519 | Email: DICRC@dicrc.com
```
(footer/header banner text also displays "Satisfaction Guaranteed" as a standing graphic-style headline on every page)

---

## Home (`/`, `Default.htm`) — index.html / Default.htm (identical content)

Heading image caption/alt: "Owner David Illg" (photo: Photo Gallery/images/dicrc 026.jpg)

Body copy, in order:

> **Welcome to Dave Illg's Collision Repair Center in Nashua, NH**

> Dave Illg's Collision Repair Center is a full service auto body shop that provides the best in customer service, collision repairs, frame and bodywork, painting and re-finishing for all makes and models, foreign or domestic vehicles. Located in Nashua, NH, Dave Illg's Collision Repair Center prides itself on employing a highly trained staff of auto body and paint specialists who ensure that every car is returned to the customer in the best condition possible.

> Authorized by several National Insurance Companies as a direct repair shop, Dave Illg's Collision Repair Center takes every single repair seriously, no matter how big or small the damage may be. Quality and integrity are our guiding principles and to ensure that every customer is satisfied, Dave Illg's Collision Repair Center offers every client a lifetime warranty on its repairs.

> The links on the top of our web site will take you to the pages where you will find information about auto body, and about the type of company we are and the services we offer you. Please make good use of our web site. We are as proud of it as we are proud of our company, the work we do, the people who work for us and the people for whom we work.

> Our paint and body shop is equipped with the latest technology required to repair today's complex vehicles. Our technicians and staff are continually trained in the latest methods required in the automotive collision repair industry. Our Auto Body Shop meets and surpasses the highest standards in quality paint and repair work. Furthermore, as members of the business community we adhere to a strict code of ethics that is part of our pledge to you of honesty, integrity, safety, and craftsmanship.

> You can contact us by phone, Email, or by stopping by during business hours or by appointment

Second homepage photo: Photos/dicrc 027.jpg (large, unscaled copy of the gallery's dicrc 027.jpg)

Customer Lobby review widget/badge embedded at bottom of page (external, links to `https://www.customerlobby.com/reviews/23341/dave-illg-s-collision-repair/`, alt text "Statistics" / "Review of Dave Illg's Collision Repair"). This is a third-party review badge, not on-site testimonial copy — no testimonial text is present on the page itself.

---

## Services (`Services.htm`)

> With more than 25 years of Auto body experience, Dave Illg's Collision Repair Center in Nashua, NH offers expert quality work in a clean and professional atmosphere.

Services list (bulleted, verbatim, in order):
- Unibody Repairs
- Computerized Wheel Balancing
- Unibody Frame Machines
- Expert Color Matching
- Computerized Color Mixing System
- Oven Baked Painting
- Computerized Free Estimates
- Full Glass Work
- Auto / SUV Detailing
- Leased Vehicle Return Preparation
- Rust Repair
- 24 Hour Towing Service
- Rental Car Arrangements

Closing line: **Ask About Our LIFETIME Warranty**

---

## Photo Gallery (`PhotoGallery.htm`)

No body copy beyond the page title/nav — this page is a 5-column thumbnail grid of 12 photos (dicrc 023.jpg through dicrc 034.jpg), each thumbnail linking to its own full-size lightbox page. No captions are present under any thumbnail (the `<font>` tags under each thumbnail are present in the markup but empty).

Thumbnails / lightbox pages, in gallery order:
1. dicrc 023 → pages/dicrc 023.htm
2. dicrc 024 → pages/dicrc 024.htm
3. dicrc 025 → pages/dicrc 025.htm
4. dicrc 026 → pages/dicrc 026.htm
5. dicrc 027 → pages/dicrc 027.htm
6. dicrc 028 → pages/dicrc 028.htm
7. dicrc 029 → pages/dicrc 029.htm
8. dicrc 030 → pages/dicrc 030.htm
9. dicrc 031 → pages/dicrc 031.htm
10. dicrc 032 → pages/dicrc 032.htm
11. dicrc 033 → pages/dicrc 033.htm
12. dicrc 034 → pages/dicrc 034.htm

Each lightbox page (`pages/dicrc 023.htm` … `034.htm`) is an Adobe Photoshop "Web Photo Gallery" auto-generated template: alt text is just "dicrc 0NN", no captions, with Previous/Home/Next icon navigation cycling through the 12 photos. No unique text content per photo — image content only (see `source/images/Photo Gallery/images/`).

---

## Hours & Directions (`Hours&Directions.htm`)

> Monday through Friday
> 7:30am to 5:00pm
>
> Nights and Weekends available by appointment

Embedded Google Map (external iframe) for "10 west otterson st nashua nh" with a "View Larger Map" link (external, not crawled).

---

## FAQ (`FAQ.htm`)

Five Q&A pairs, verbatim:

**Q: Do I have to take my vehicle to the body shop recommended by my insurance company?**
A: No, the body shop your insurance recommends is just that, a recommendation. You can choose whichever shop you like to have your vehicle repaired. Dave Illg's Collision Repair Center offers a lifetime warranty on all work performed by us.

**Q: My insurance company wants me to use a LKQ (Like Kind Quality) part to repair my vehicle. What does this mean?**
A: LKQ parts are refurbished parts that the insurance company feels are adequate replacements for the parts needed on your vehicle. Use of these parts reduces the cost of repairing the vehicle which in turn helps keep insurance premiums down. At Dave Illg's Collision Repair Center, we will only use LKQ parts if they are up to our high standards.

**Q: I'm afraid that my frame is bent. If it is, should I sell my car after the repairs are done? I've been told that if the chassis is bent, that the car will never be the same again.**
A: To begin with, your vehicle may have a chassis (frame). or it may of Unibody construction. However, as far as you are concerned, no matter which it is, the answer is simple. If you choose a quality repair facility that has the proper, up-to-date equipment (a Unibody bench for example) to repair your vehicle, you nor anyone else will ever be able to tell the vehicle had ever been damaged. And as for that old wife's tale, of course your car will be just as good after the repair as before. But remember, the quality of the repair comes from the quality of the people who do that repair.

**Q: Is my car going to have two different shades of color because you're only painting the areas that have been damaged instead of the whole car?**
A: Absolutely not! At Dave Illg's Collision Repair Center we say with confidence that your car will look as if it had never been involved in an accident. We can say this because at Dave Illg's Collision Repair Center we are equipped with a fully computerized paint mixing system to assure you of perfect color matching which makes exotic colors as easy to match as standard factory shades.

**Q: How soon after my vehicle is repaired and painted can I wash and wax it?**
A: The rule we have at Dave Illg's Collision Repair Center is that a car should not go through a car wash for at least 2 weeks. You may, however, wash it by hand at anytime.

*(Content oddity, minor: Q3's answer contains an apparent source typo — "your vehicle may have a chassis (frame). or it may of Unibody construction" — reproduced here verbatim per content-lock rule; do not "fix" the grammar when redesigning, per instructions not to rewrite copy.)*

---

## Feedback (`feedback.html`)

Third-party embedded form ("Freedback.com" — `<form action="http://www.freedback.com/mail.php" method="post">`). Field labels, verbatim, in order:

1. **First Name:** (text input)
2. **Last Name:** (text input)
3. **Email Address:** (text input)
4. **How satisfied were you with the service you received?** — radio options: Very Satisfied / Somewhat Satisfied / Somewhat Unsatisfied / Very Unsatisfied
5. **How satisfied are you with our company overall?** — radio options: Very Satisfied / Somewhat Satisfied / Somewhat Unsatisfied / Very Unsatisfied
6. **How likely are you recommend our company to others?** — radio options: Very Satisfied / Somewhat Satisfied / Somewhat Unsatisfied / Very Unsatisfied
7. **How would rate the overall friendliness of our staff?** — radio options: Great / Good / Average / Fair / Poor
8. **What are things that you believe we do well?** (textarea)
9. **What are things that you believe we can improve on?** (textarea)
10. Submit button labeled: **Submit Form**

*(Content oddity, minor, source typos reproduced verbatim per content-lock: "How satisfied were you with the service you recieved?" [sic, "recieved"] appears in the raw HTML as "recieved" though rendered label reads the same; "How likely are you recommend" [sic, missing "to"] and "How would rate" [sic, missing "you"] are both grammatically off in the source and should be kept as-is per the no-rewrite rule, or flagged to the business owner rather than silently corrected.)*

Note for redesign: this form currently POSTs to a third-party service (freedback.com). Whether that service is still active/receiving submissions was not verified (out of scope for a content crawl); flag to the user before deciding whether to keep, replace, or point it at a different back end — AGENTS.md says keep the same fields and purpose if a form is kept.

---

## Content oddities / inconsistencies (AGENTS.md rule 6)

1. **Email address mismatch between link and display text**, present on every single page (header/footer, identical everywhere): the mailto link target is `djillg@dicrc.com` (`<a href="mailto:djillg@dicrc.com">`) but the visible/displayed text is `DICRC@dicrc.com`. These are two different addresses (djillg@ vs DICRC@). Since this is 100% consistent across all 18 unique pages, there's no conflicting "second value" to cross-reference against — flagging for the business owner to confirm which address is correct/live before the redesign goes live, rather than guessing. Recommend keeping the visible text "DICRC@dicrc.com" as shown (matches content-lock: display text is the "content"), but confirm the mailto: target with the owner.
2. **`Default.htm` is a byte-for-byte duplicate of the homepage** (`/`). Only one "Home" page of content exists; no unique content lost by treating these as a single page in the redesign.
3. **`Photo Gallery/index.htm` is an orphaned, stale duplicate gallery index.** It's an Adobe Photoshop-generated page not linked from the site's nav or footer (only reachable via an empty anchor fragment inside each lightbox page's "Home" link target region), and it's missing photo 034 (lists only 11 of the 12 gallery photos, whereas the real `PhotoGallery.htm` lists all 12). This reads as leftover tooling output/tech debt, not real content — safe to omit per AGENTS.md rule 5. All 12 photos are still fully captured via `PhotoGallery.htm` and its lightbox pages, so no media is lost by omitting this file.
4. **Inconsistent link encoding for two gallery thumbnails:** on `PhotoGallery.htm`, the links to photos 032 and 034 use a literal space in the href (`pages/dicrc 032.htm`, `pages/dicrc 034.htm`) while all other 10 thumbnails use `%20` (`pages/dicrc%20023.htm`, etc.). Both forms resolve correctly server-side; purely a markup inconsistency, not a content issue, but worth normalizing (URL-encode consistently) in the redesign rather than reproducing the inconsistency.
5. **No captions/alt text of substance anywhere in the photo gallery** — all 12 gallery photos have only generic alt text ("dicrc 023", "dicrc 024", etc.) and no descriptive captions in the source. Per AGENTS.md, do not invent marketing alt copy; carry over the same generic alt text (or reuse filenames) rather than writing new descriptions.
6. **Two different-resolution copies of "dicrc 027.jpg" exist at different paths**: `/Photos/dicrc 027.jpg` (1.1MB, full resolution, used directly on the homepage) and `/Photo Gallery/images/dicrc 027.jpg` (~29KB, gallery-resized version, used in the lightbox page). Both were downloaded; use the homepage's higher-resolution copy in the redesign where a large image is needed, and the gallery version is fine for thumbnails/lightbox use.
7. **Minor grammar/typos in source copy, reproduced verbatim per the no-rewrite rule** (see FAQ and Feedback sections above for exact locations): "or it may of Unibody construction" (FAQ Q3, likely meant "may be of"), "How likely are you recommend our company" (Feedback form, missing "to"), "How would rate the overall friendliness" (Feedback form, missing "you"). These are being kept as-is in the source archive; whether to silently fix small typos like this when the redesign copy is set is a decision for the user, not something to resolve here.
8. **No dead/duplicate nav items, Flash, marquees, or IE hacks found** — the nav (Home / Services / Photo Gallery / Hours & Directions / FAQ / Feedback) is identical and fully functional on every page, header and footer. The only "tech debt" found were the two duplicate pages noted above (#2 and #3) and the boilerplate `Scripts/AC_RunActiveContent.js` (FrontPage/Dreamweaver Active Content compatibility shim, loaded on every page, no business content).
