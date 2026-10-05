---
name: Savarino's Market
description: A Sicilian family bakery sign translated to the web. Navy ink on ivory, teal rules, one fat display serif, one wide geometric sans.
colors:
  navy: "#001c41"
  navy-2: "#3b4c68"
  navy-lift: "#0a2d5c"
  navy-deep: "#07295a"
  ivory: "#fdfef8"
  ivory-2: "#f3f5e8"
  ivory-on-navy: "#c5cedc"
  teal: "#069da3"
  saffron: "#f1b21c"
  cannoli-gold: "#f2bb5d"
  note-wash: "#fbf0cd"
  error: "#b3261e"
  error-text: "#9c1c15"
  error-on-navy: "#ffb4ab"
typography:
  display:
    fontFamily: "Abril Fatface, Bodoni 72, Didot, Georgia, serif"
    fontSize: "clamp(3.05rem, 2.519rem + 2.17vw, 4.475rem)"
    fontWeight: 400
    lineHeight: 1.06
    letterSpacing: "-0.005em"
  headline:
    fontFamily: "Abril Fatface, Bodoni 72, Didot, Georgia, serif"
    fontSize: "clamp(2.4375rem, 2.094rem + 1.4vw, 3.356rem)"
    fontWeight: 400
    lineHeight: 1.06
    letterSpacing: "-0.005em"
  title:
    fontFamily: "Abril Fatface, Bodoni 72, Didot, Georgia, serif"
    fontSize: "clamp(1.953rem, 1.744rem + 0.862vw, 2.519rem)"
    fontWeight: 400
    lineHeight: 1.06
  subtitle:
    fontFamily: "Abril Fatface, Bodoni 72, Didot, Georgia, serif"
    fontSize: "clamp(1.5625rem, 1.442rem + 0.495vw, 1.8875rem)"
    fontWeight: 400
    lineHeight: 1.1
  item:
    fontFamily: "Abril Fatface, Bodoni 72, Didot, Georgia, serif"
    fontSize: "clamp(1.25rem, 1.19rem + 0.257vw, 1.42rem)"
    fontWeight: 400
    lineHeight: 1.2
  body:
    fontFamily: "Montserrat, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1rem, 0.96rem + 0.1vw, 1.0625rem)"
    fontWeight: 450
    lineHeight: 1.6
  lede:
    fontFamily: "Montserrat, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(1.25rem, 1.19rem + 0.257vw, 1.42rem)"
    fontWeight: 500
    lineHeight: 1.45
  label:
    fontFamily: "Montserrat, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "0.14em"
  button:
    fontFamily: "Montserrat, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 700
    letterSpacing: "0.12em"
  sign-word:
    fontFamily: "Montserrat, Avenir Next, Segoe UI, system-ui, sans-serif"
    fontSize: "clamp(0.9375rem, 0.75rem + 1vw, 1.375rem)"
    fontWeight: 600
    letterSpacing: "0.26em"
rounded:
  none: "0"
  focus: "2px"
  dot: "50%"
spacing:
  s1: "0.5rem"
  s2: "1rem"
  s3: "1.5rem"
  s5: "2.5rem"
  s8: "4rem"
  s13: "6.5rem"
  gutter: "clamp(16px, 4.4vw, 56px)"
  max-width: "1440px"
components:
  button-teal:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.navy}"
    typography: "{typography.button}"
    rounded: "{rounded.none}"
    padding: "0 28px"
    height: "52px"
  button-teal-hover:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.ivory}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.navy}"
    rounded: "{rounded.none}"
    padding: "0 28px"
    height: "52px"
  button-line-hover:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.ivory}"
  button-saffron:
    backgroundColor: "{colors.saffron}"
    textColor: "{colors.navy}"
    rounded: "{rounded.none}"
    padding: "0 28px"
    height: "52px"
  button-saffron-hover:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.navy}"
  button-line-light:
    backgroundColor: "transparent"
    textColor: "{colors.ivory}"
    rounded: "{rounded.none}"
    padding: "0 28px"
    height: "52px"
  button-line-light-hover:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.navy}"
  sign-block-star:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.ivory}"
    typography: "{typography.subtitle}"
    padding: "1.5rem"
    height: "220px"
  designer-note:
    backgroundColor: "{colors.note-wash}"
    textColor: "{colors.navy}"
    padding: "8px 12px"
  framed-panel:
    backgroundColor: "{colors.ivory}"
    textColor: "{colors.navy}"
    padding: "2.5rem 1.5rem"
  dock:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.ivory}"
    height: "60px"
  dock-primary:
    backgroundColor: "{colors.saffron}"
    textColor: "{colors.navy}"
---

# Design System: Savarino's Market

## Overview

**Creative North Star: "The Sign Over the Door"**

The site is the family's hand-lettered shop sign made navigable. Eight words (Catering, Deli, Pastas, Sandwiches, Pastries, Cookies, Cakes, Bread) run the whole site in the same order and spelling, and every surface is built so those words read as a sign: heavy display serif, wide-set sans caps, teal rules, a saffron dot between neighbors. Navy ink on ivory paper is the default; navy as a ground is the exception that makes a moment feel lit.

The world is the owner's own color logo. Palette, ornament and illustration are sampled or cropped from it (see Provenance). Nothing is a rebrand. Space and hairlines do the grouping, not shadow or card chrome: the system is flat, square-cornered and ruled. Density is airy on ivory, tighter inside the menu where dotted leaders and prices need to scan.

Voice in the interface is short and direct. Placeholders are plain, labeled frames and amber "CONFIRM WITH OWNER" notes, never confident guesses.

**Key Characteristics:**
- Roughly 60 percent ivory, 30 navy, 10 teal plus saffron.
- Two families only: Abril Fatface for anything headline-like, Montserrat for everything read.
- Rail-and-field grid: a 2fr rail for the section title, a 10fr field for content, under a 2px teal rule.
- Square corners everywhere; circles only for dots.
- Flat. No gradients, no cast shadows.
- Dotted teal leaders connect labels to values (hours, menu prices, footer hours).
- One delight moment: filling the cannoli.

## Colors

A sign-painter's palette: deep navy ink, warm ivory paper, a cool teal for rules and one hot accent used like a dot of gold leaf.

### Primary
- **Sign Navy** (`navy`, #001c41): all text on ivory, the dark field and footer ground, button text on teal, borders of line buttons and form fields.
- **Door Teal** (`teal`, #069da3): structure and wayfinding. Section rules, block borders, dotted leaders, the fleuron lines, link underlines, framed-panel borders, tile work, the filled face of the primary button (with navy text), scrollbar, selection fill.

### Secondary
- **Saffron Dot** (`saffron`, #f1b21c): the sparing accent. Dot separators between sign words and blocks, the open-status dot, the "today" dot in the hours table, the active menu category dot, the mobile Call tab, the arrow on navy sign blocks, the inline wholesale list bullets. Also the secondary button face.

### Tertiary
- **Cannoli Gold** (`cannoli-gold`, #f2bb5d): lives inside the cannoli engraving only. Never a UI color.

### Neutral
- **Ivory** (`ivory`, #fdfef8): page ground, header, framed panels.
- **Ivory Deep** (`ivory-2`, #f3f5e8): placeholder frames, hover wash on sign blocks, form-success panel, scrollbar track.
- **Navy Soft** (`navy-2`, #3b4c68): secondary text on ivory (descriptions, captions, the hero "since" line).
- **Ivory On Navy** (`ivory-on-navy`, #c5cedc): secondary text on navy.
- **Navy Lift** (`navy-lift`, #0a2d5c) and **Navy Deep** (`navy-deep`, #07295a): hover and inset surfaces inside navy fields (star block hover, placeholder frames, map box, success panel).
- Hairlines: `rgba(0,28,65,0.16)` on ivory, `rgba(253,254,248,0.22)` on navy.

### Functional
- **Note Wash** (`note-wash`, #fbf0cd) with a saffron border: the designer-note component only.
- **Error** (#b3261e border, #9c1c15 text on ivory, #ffb4ab on navy): form validation only.

### Contrast pairs (measured against the build's values)
- Navy on ivory: 16.7:1 (body text).
- Navy on teal: 5.1:1 (teal buttons).
- Navy Soft on ivory: 8.6:1 (secondary text).
- Ivory On Navy on navy: 10.6:1 (secondary text in navy fields).
- Teal on ivory is a rule color only; it does not carry text.

### Named Rules
**The Teal Is Structure Rule.** Teal draws lines, leaders, borders and button faces. It never sets paragraph or label text on ivory. Text on a teal face is navy, never ivory.

**The Saffron Dot Rule.** Saffron is a dot, a bullet, a single button or a single tab, never a surface wash or a text color on ivory. If a screen has more than a handful of saffron marks, remove some.

**The Field Owns Its Ink Rule.** A `field-navy` section re-declares foreground, secondary, hairline and focus ring tokens. Never hand-color text inside a field; swap the field.

## Typography

**Display Font:** Abril Fatface (with Bodoni 72, Didot, Georgia, serif), single weight 400, self-hosted latin woff2.
**Body Font:** Montserrat (with Avenir Next, Segoe UI, system-ui, sans-serif), variable 400 to 700, body at 450, self-hosted latin woff2.

**Character:** A fat, high-contrast Didone that echoes the SAVARINO'S wordmark, set against a wide geometric sans that echoes the register screen. The serif speaks; the sans explains and points. Scale runs 1.25 on phones to about 1.333 at desktop via clamp.

### Hierarchy
- **Display / t5** (Abril 400, `clamp(3.05rem, 2.519rem + 2.17vw, 4.475rem)`, 1.06): menu page h1, wholesale h2.
- **Headline / t4** (Abril 400, `clamp(2.4375rem, 2.094rem + 1.4vw, 3.356rem)`, 1.06): favorites and catering heads, menu board h2, rating.
- **Title / t3** (Abril 400, `clamp(1.953rem, 1.744rem + 0.862vw, 2.519rem)`, 1.06): hero line on phones, rail h2 on phones, route line, favorite h3. At 56rem the hero line becomes `clamp(2.2rem, 1.2rem + 1.7vw, 3.1rem)` and the rail h2 `clamp(1.75rem, 1.2rem + 1.1vw, 2.4rem)`.
- **Subtitle / t2** (Abril 400, `clamp(1.5625rem, 1.442rem + 0.495vw, 1.8875rem)`, 1.1): sign block words (multiplied by a per-block scale), phone numbers, offer titles, the wink line.
- **Item / t1** (Abril 400, `clamp(1.25rem, 1.19rem + 0.257vw, 1.42rem)`, 1.2): menu item names, row labels, point headings. Also the sans lede at weight 500, 1.45, max 38ch.
- **Body / t0** (Montserrat 450, `clamp(1rem, 0.96rem + 0.1vw, 1.0625rem)`, 1.6, max 62ch): paragraphs.
- **Small** (Montserrat 450 to 600, 0.8125 to 0.9375rem, 1.45 to 1.5): descriptions, captions, form notes.
- **Label** (Montserrat 700, 0.8125rem, 0.14 to 0.16em, uppercase): nav links, category nav, form labels, dock tabs, button text (0.875rem, 0.12em).
- **Sign word** (Montserrat 600, `clamp(0.9375rem, 0.75rem + 1vw, 1.375rem)`, 0.24em phones / 0.26em desktop, uppercase): the eight-word list. Footer variant `clamp(0.875rem, 0.78rem + 0.5vw, 1.0625rem)`, 0.22em.

### Per-word type scale on sign blocks
Each sign block sets `--k` and renders its h4 at `t2 * k`, so the words read as hand-fitted lettering rather than a uniform grid. Values in the build: Catering 1.1, Deli 1.5, Pastas 1.3, Sandwiches 1.0, Pastries 1.1, Cookies 1.15, Cakes 1.5, Bread 1.5. Short words get the larger multiplier. Keep scale between 1.0 and 1.5.

### Named Rules
**The Two Voices Rule.** Display serif for names and headings, sans for everything that is read or tapped. Never set paragraphs in the serif; never set a heading in the sans except the uppercase sign-word list and labels.

**The Tabular Price Rule.** Prices and hours use tabular numerals, bold, with 0.04em tracking on prices.

## Layout

**Rail and field.** Every content section opens with a 2px teal top rule. At 56rem and up the section becomes a two-column grid, 2fr rail (section title) and 10fr field, with a 2.5rem column gap. Below 56rem it stacks. The menu page repeats the same 2fr/10fr split with a sticky category nav in the rail.

**Container.** Max width 1440px, fluid gutter `clamp(16px, 4.4vw, 56px)`.

**Spacing beats.** An 8px unit on a 1, 2, 3, 5, 8, 13 sequence: 0.5, 1, 1.5, 2.5, 4, 6.5rem. Section padding is 4rem on phones, 6.5rem at 56rem. Gaps inside components use s1 to s3; gaps between components use s5 to s8.

**Three acts.** The homepage is read as three acts. (1) The sign: hero, hours and what to know. (2) The goods: everything on the sign, crowd favorites, catering and cakes, wholesale on a navy field. (3) The family: proof, route, and the navy footer with tile band. Fields alternate ivory, ivory-deep and navy to mark act changes; the footer is always navy.

**Hero first viewport.** Top to bottom: header (logo hidden on home until scrolled past, replaced by a small place line), the eight words as a sign (two-column grid of four rows on phones with saffron dots between pairs; one centered row with 2.4em gaps at 56rem), the full color logo at up to 44rem wide, then the info band: display tagline, open/closed status, address and tap-to-call phone, and Call / Directions / Menu buttons. At 56rem the info band is 8fr tagline and actions, 4fr where-block. The primary call, directions and menu actions are always within the first viewport, and on phones also in the dock.

**Know-before-you-go.** Two equal columns at 56rem (hours and diagram on one side, points and photo on the other), single column on phones.

**Breakpoints.** 40rem (button sizing, two-up form rows, long concept bar text), 56rem (the main switch: rail and field, desktop header, hidden dock and toggle, sign-row column ratios), 80rem (footer words single row).

**Sign rows.** Two rows of four blocks. Row one columns `1fr 0.9fr 1fr 1.45fr`, row two `1.45fr 1fr 0.9fr 1fr`, mirrored so the featured navy blocks fall on a diagonal. Two-up on phones.

## Elevation & Depth

Flat. No cast shadows, no gradients, no blur. Depth is carried by field changes (ivory, ivory-deep, navy), 1 to 3px rules and borders, and surface insets. The only shadow in the build is an inset 4px saffron underline marking the current dock tab. Focus is a 3px outline with 3px offset, navy on ivory and ivory on navy.

**The Flat Rule.** A surface rises by changing ground or gaining a teal rule, never by casting a shadow.

## Shapes

Square. Buttons, inputs, panels, blocks and frames have 0 radius. The only curves are circular dots (saffron separators, status dot, active-nav dot, bullets), the 2px focus rounding, and the curves inside ornament artwork. Borders carry the structure: 2px for buttons, inputs, framed panels and section rules; 1px for block dividers and hairlines; dashed teal for placeholder and quote frames; dotted for leaders.

**Ornaments.** Two ornament assets come from the logo: the corner flourish (52 by 49px, mirrored with scale transforms to all four corners of a framed panel, inset 3px) and the fleuron divider (72 by 24px, flanked by 1px teal lines). The tile band is a 96px strip of the logo's maiolica tile, repeated on x, over a 3px navy top border, sitting between footer and legal line.

**The Ornaments Never Wallpaper Rule.** Corner flourishes belong to a framed panel (the order forms), the fleuron to a single section break, the tile band to the footer only. Never tile ornament behind content, never repeat a flourish on a surface that does not frame something.

## Components

### Buttons
Square, 52px minimum height, 0 28px padding, Montserrat 700 at 0.875rem, 0.12em tracking, uppercase, 2px border. Transition 180ms on the system ease. Active presses 1px down.
- **Teal** (primary): teal face, navy text, teal border. Hover flips to navy face, ivory text. Inside a navy field hover flips to ivory face, navy text.
- **Line:** transparent, navy text and border. Hover fills navy, ivory text.
- **Saffron:** saffron face, navy text. Hover turns ivory. The one-per-screen call-out and the dock's Call tab.
- **Line light:** transparent with ivory text and border, for navy fields. Hover fills ivory, navy text.
- On phones hero buttons share the row equally (smaller padding, 0.8125rem) and become auto-width at 40rem.
- Navy text on the teal button is mandatory; ivory on teal fails contrast.

### Header
Ivory bar, 60px on phones, 76px sticky at 56rem with a hairline that appears once past the hero (always on the menu page). **Logo swap:** on the homepage the logo is hidden while the hero logo is visible and the small "place" line shows in navy-2; once the hero logo scrolls out (IntersectionObserver, 72px margin) they cross-fade over 300ms. Elsewhere the 48px logo shows. Nav links are 0.8125rem caps with a 3px teal underline for hover and current page. A 44px square toggle opens a full-width panel of 56px rows on phones, where the current page gets a saffron dot with navy ring.

### Sign words list
The eight words as a centered caps list with a 6 to 7px saffron dot between neighbors, never after the last item in a row. Links underline in teal 2px on hover. Reused in the footer at a smaller size.

### Sign blocks
Hairless grid cells separated by 1px teal rules, each a full-cell link with a serif word, a short description in navy-2, and a 34 by 16px arrow that nudges 6px right on hover. At 56rem, minimum height 220px, a 7px saffron dot sits on each junction. **Featured navy cells** (`block--star`: Sandwiches and Pastries) invert to navy ground, ivory word, ivory-on-navy description, saffron arrow, and lift to navy-lift on hover. Two featured cells per page at most. Each row has a serif row label underlined with a 2px navy dotted line.

### Framed panel
2px teal border on ivory with corner flourishes on all four corners, generous padding (2.5rem by 1.5rem; the form variant 4.25rem vertical, 2.5rem horizontal at 56rem to clear the ornaments). Houses the order and inquiry forms.

### Hours table
Semantic table whose rows are three-column grids: day, dotted leader, time. Leader is a 2px dotted teal bottom border lifted 5px. Today's row is bold and gains a 10px saffron dot (set by script in Central time). Times are tabular. The footer repeats the pattern as a definition list.

### Menu item
Serif item name (t1), a flexing 2px dotted teal leader (minimum 14px), then a bold tabular price; description below in navy-2 at 0.9rem, max 46ch, with a 1px hairline under each item. Prices read `$00` until the owner confirms them. Two columns at 56rem for long boards. A featured "meal" item takes 2px teal rules above and below, a larger name (t2) and navy description.

### Category nav
Sticky strip on phones: caps links, horizontally scrollable, 2px teal bottom border, 4px teal underline on the current item. At 56rem it becomes a sticky vertical list in the rail (top 100px) where the current item carries a saffron dot with navy ring instead of an underline.

### Form fields
Underline inputs: transparent, 48px minimum, 2px navy bottom border, no radius. Textareas take a full 2px box. Labels are 0.75rem bold caps at 0.16em. Focus is a 3px teal outline with 2px offset. Invalid fields turn the border `#b3261e` and show a 0.8125rem semibold error line. On navy fields borders and text flip to ivory. The success panel is an ivory-deep box with a 2px teal border.

### Designer note
A development-and-review scaffold: pale wash (`#fbf0cd`) with a 1px saffron border, small text, and a navy chip with saffron text reading CONFIRM WITH OWNER. On navy it inverts (navy-lift ground, saffron chip with navy text). A bar at the top of the page can hide all notes by toggling `notes-off`. This is the one place saffron is allowed to shout, and it is meant to be removed or hidden before launch.

### Dock
Mobile fixed bottom bar, grid 1.2fr 1fr 1fr, navy with a 3px teal top border, 60px tabs in ivory caps with hairline dividers. The first tab (Call) is saffron with navy text. The current tab gets the inset saffron underline. Hidden at 56rem; body gains 66px bottom padding to clear it.

### Tile band and footer
Navy footer: ivory plate holding the logo, caps word list, four columns (address, hours with dotted leaders, social, map), tile band, then a navy legal line in ivory-on-navy. Column heads are serif with a 1px teal underline.

### Cannoli (signature delight)
A button-wrapped engraving of an empty shell with two fill images clipped by circles that grow from each open end. Fill takes 1500ms on `cubic-bezier(0.25, 0.8, 0.35, 1)`, the right side delayed 350ms, circles grow to 46 percent radius. A "Fill it / Start over" button and a status line (aria-pressed, live text) mirror it. Without script the finished full cannoli shows. Reduced motion collapses the transition to near zero.

### Placeholders and quote slots
Dashed 1px teal frames on ivory-deep with centered caps text naming the exact shot (4/3, 16/9). Quote slots use a dashed teal frame and an oversized teal serif opening quote on a ivory knock-out patch.

## Motion

One easing: `cubic-bezier(0.16, 1, 0.3, 1)` (`--ease`), an out-expo. Durations: 180ms for button color, 200ms for block hover, 240ms for arrow nudge, 300ms for the header logo cross-fade. The cannoli fill is the only long motion (1500ms). Smooth scroll with an 88px scroll padding for the sticky header. All transitions drop to 0.01ms under `prefers-reduced-motion`.

## Do's and Don'ts

### Do:
- **Do** set all text in navy on ivory (16.7:1), navy-2 for secondary (8.6:1), and ivory or ivory-on-navy (10.6:1) on navy fields.
- **Do** put navy text on every teal button face (5.1:1).
- **Do** use teal for rules, leaders, borders, underlines and tile work.
- **Do** keep the eight words spelled exactly, in the sign order, prominent in the hero, the sign blocks, the menu headings and the footer.
- **Do** group with space, hairlines and type before reaching for a box.
- **Do** use the rail and field grid (2fr/10fr at 56rem) for every sectioned page.
- **Do** keep tap targets at 44px or more and every control visibly focusable.
- **Do** use dotted teal leaders for any label-to-value pair.
- **Do** make any new illustration in the logo's etched engraving style, derived from the logo, or leave it out and ship a labeled placeholder frame.
- **Do** keep the cannoli fill as the only delight moment.

### Don't:
- **Don't** set paragraph or label text in teal on ivory. Teal is structure.
- **Don't** set ivory text on a teal face.
- **Don't** use saffron as a surface wash, a text color on ivory, or on more than a few marks per screen. Cannoli gold never appears in UI.
- **Don't** use gradients, drop shadows, rounded corners, or thick side stripes. Borders go all the way around or run as full rules.
- **Don't** let ornaments become wallpaper: corner flourishes only on framed panels, the fleuron only as a single section divider, the tile band only above the footer legal line.
- **Don't** add a second delight interaction, or any decorative animation.
- **Don't** introduce a third typeface, a script face, emoji, glyph icons, or stock or scraped photography.
- **Don't** use Italian flag color combinations, checkered patterns, or illustrations in any other style than the logo's etching.
- **Don't** invent facts. Unknown details stay as a labeled placeholder or a CONFIRM WITH OWNER note.

## Provenance and not canonized

The rasters in `site/assets/img/` (logo, cannoli empty, full, fill-left, fill-right) carry sidecar `.json` files stating they are crops of the owner's supplied color logo with background flattened or removed, no generation. The corner ornament, fleuron and tile are SVG redrawings in the logo's palette.

Not canonized: the `.caps` utility class exists in the stylesheet but is unused in either page; the "Designer notes" yellow wash is a review scaffold, not a pattern for shipped surfaces.
