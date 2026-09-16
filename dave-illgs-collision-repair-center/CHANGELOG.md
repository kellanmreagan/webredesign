# Dave Illg's Collision Repair Center — Redesign Change Log

Source: https://www.dicrc.com/ (crawled and archived to `source/`). Redesign built as static
HTML/CSS/JS in this folder: `index.html`, `services.html`, `gallery.html`,
`hours-directions.html`, `faq.html`, `feedback.html`, plus `css/style.css`, `js/main.js`, and
`images/`.

## Layout & navigation — kept as-is

The source site's nav and IA (Home / Services / Photo Gallery / Hours & Directions / FAQ /
Feedback) were already clear, non-duplicated, and fully functional on every page. Per AGENTS.md
rule 1 ("if the current nav and IA is decent... keep the general layout and structure"), the
redesign keeps the same 6 pages, same names, same order, same primary conversion path
(call/email). Only spacing, typography, and visuals were modernized.

Two pieces of pure tech debt were omitted per rule 5 (no real content lost):
- `Default.htm` — a byte-for-byte duplicate of the homepage.
- `Photo Gallery/index.htm` — a stale, orphaned Adobe "Web Photo Gallery" auto-generated index,
  not linked from the site's nav, and missing photo 034 (the real `PhotoGallery.htm` has all 12).

## Content preserved

- All homepage, Services, Hours, and FAQ body copy carried over verbatim, including source
  grammar as-is per the no-rewrite rule (e.g. FAQ's "or it may of Unibody construction").
- All 13 services, in original order, and the closing line "Ask About Our LIFETIME Warranty".
- Both business hours lines and the "Nights and Weekends available by appointment" note.
- All 5 FAQ question/answer pairs, verbatim.
- The Feedback form: all 9 original fields (name, email, 4 satisfaction/rating questions with
  their original radio-button option labels, 2 free-text questions), including verbatim source
  typos in the field labels ("How likely are you recommend...", "How would rate..."). The form
  still POSTs to the same third-party endpoint (freedback.com) the source site used — its
  continued availability was not verified; flagging this for the business owner to confirm
  before relying on the form for real submissions.
- All 12 photo-gallery photos (in original order, dicrc 023–034), reused directly from the
  source site — no stock photos substituted, no images dropped. Alt text carries over the
  source's generic "dicrc 0NN" labels rather than inventing descriptive captions, since none
  existed in the source (per rule: don't invent marketing alt copy).
- The owner photo (dicrc 026) and the high-resolution exterior/Mustang photo (dicrc 027, using
  the source's full-resolution copy from `/Photos/` rather than the lower-res gallery copy).
- The site's actual logo/brand graphic (`Header.jpg`, the red-Mustang banner with "Dave Illg's
  Collision Repair Center" wordmark) — reused directly on the homepage rather than replaced with
  new brand styling, satisfying "keep all logos, don't replace with stock."
- Contact info: phone (603) 204-5516, fax (603) 204-5519, address 10 W Otterson St, Nashua, NH
  03060. Click-to-call added on the phone number throughout.

## Content oddity flagged, not resolved (AGENTS.md rule 6)

The source site's mailto link target (`djillg@dicrc.com`) does not match its own displayed
footer text (`DICRC@dicrc.com`) — this mismatch is 100% consistent across every page of the
source site, so there's no third value to resolve it against. The redesign reproduces the same
pairing (visible text "DICRC@dicrc.com", mailto target "djillg@dicrc.com") to match current site
behavior exactly, rather than guessing which address is correct. **Flagging for the business
owner:** please confirm which email address should be used, and I'll update both the display
text and the link target to match.

## Non-content chrome omitted (per AGENTS.md rule 5)

- Adobe Photoshop "Web Photo Gallery" auto-generated lightbox pages (12 separate `.htm` files
  with Previous/Home/Next navigation) — replaced with a single gallery page and an in-page
  lightbox with the same prev/next/close behavior, keeping all 12 photos.
- `Scripts/AC_RunActiveContent.js` — a FrontPage/Dreamweaver Active Content compatibility shim
  with no business content.
- Inconsistent URL-encoding in two gallery thumbnail links (literal space vs. `%20`) — normalized.

## Design

Palette pulled directly from the site's own logo graphic (deep black, signal red, chrome
silver) rather than introducing a new brand identity — matches the "auto garage" personality
called for in AGENTS.md. Condensed bold headings (Oswald) evoke automotive signage without
tipping into gaudy; clean body type (Inter) keeps long-form copy (FAQ, services) readable.
Mobile-first, fully responsive, click-to-call phone numbers, and a lightweight photo lightbox
with keyboard (arrow key / Escape) and on-screen prev/next controls covering all 12 gallery
photos (no framework, vanilla JS).
