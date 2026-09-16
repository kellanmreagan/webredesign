# Claude web redesigns — agent instructions

This folder (`~/claudewebredesigns`) is the home for Claude Code website redesigns.

- One subfolder per site.
- Do not put new redesigns in the home directory.
- Read that site’s `README.md` for the **Site brief** when present.
- **Claude Code does all designing.** The human/orchestrator only pulls the trigger — do not translate or reinterpret “what the site should look like” beyond these rules and the Site brief.

You are redesigning a dated small-business website. Follow these rules for every chat in this tree.

## Mission

Modernize the design and UX so the site is classier and easier to use — especially on mobile — while keeping the local / owner-operated personality.

Do not turn the site into a generic SaaS, startup, or glossy agency portfolio template.

## Content lock (strict)

1. Keep **ALL** existing content from the source site: body copy, headlines, subheads, labels, lists, menus, hours, addresses, phones, emails, prices, names, bios, legal lines, footers — every piece of real business content.
2. **Do not rewrite headlines** or any other copy. No paraphrasing, no “improved” marketing language, no new slogans.
3. Keep **ALL** photos, logos, icons, and other media from the source site. Reuse the same assets. Do not replace with stock. Do not drop gallery images.
4. Do not invent testimonials, awards, ratings, prices, services, team members, claims, or pages that are not on the source site.
5. You may omit non-content chrome / tech debt (Flash, marquee, blink, IE hacks, keyword-spam city footers, dead nav items like “Reservations-old”). Never omit real business information or real media.
6. Contact details must match the source. If one place has an obvious typo and another consistent value, use the correct one and note it in the change log.

## Layout & navigation

1. If the current nav and information architecture are decent (clear labels, sensible pages, obvious hierarchy): **keep the general layout and structure**. Refine spacing, typography, and visuals only. Do not reshuffle or rename for novelty.
2. If nav/IA is confusing, thin, duplicated, or broken: modernize structure (clear primary nav, logical flow, obvious path to the primary conversion) while still placing **all** content and media on the appropriate pages.
3. Preserve personality in visual tone (warm shop, rustic lodge, auto garage, etc.), not in outdated implementation (table layouts, fixed 780px, FrontPage artifacts, no-viewport desktop-only pages).

## Design & UX

- Classier: restrained palette (prefer colors already in the logo/site), tighter typography, consistent spacing; polished, not flashy.
- Easier: scannable hierarchy, obvious CTAs, clear call / email / visit paths.
- Forms: only if the source had one; keep the same fields and purpose.
- Mobile-first and fully responsive: readable type, tap-friendly controls, no horizontal scroll.
- Click-to-call on phone numbers where phones are shown.
- Fast and clean: semantic HTML, accessible contrast, alt text on images (use existing captions/filenames; do not invent marketing alt copy).
- Favicon + basic meta title/description may reuse **existing** site title/tagline text only.

## Deliverables

- Production-ready HTML/CSS for every page listed in the Site brief (minimal JS only if needed for nav/carousel behavior that already existed in spirit).
- One coherent visual system across all pages.
- Source images/logos clearly included and referenced.
- Short change log:
  - Layout/nav kept vs changed (and why)
  - Confirmation that content, headlines, and media were preserved
  - Any non-content chrome omitted

## Out of scope

- Rewriting or upgrading copy/headlines
- New brand strategy, voice, or services
- Blog, chat widgets, popups, or lead magnets not on the source
- A full CMS unless the user explicitly asks in this chat

## Default kickoff

When the user starts work without extra detail, assume: redesign the Site brief URL for the current site folder; content lock on; modernize design/UX only.
