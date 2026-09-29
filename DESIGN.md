---
name: Savarino's
description: A painted wall sign on 19th-century brick for a Sicilian-American bakery, deli and market on 11th Street.
colors:
  white: "#FFFFFF"
  ink: "#1C1714"
  ink-2: "#5A4E47"
  brick: "#8F3421"
  ochre: "#F0B43A"
  ochre-lit: "#F6C45A"
  on-brick-2: "#F4DCD3"
  on-ink-2: "#D9CFC8"
  rule-ink: "rgba(28, 23, 20, .16)"
  rule-light: "rgba(255, 255, 255, .26)"
typography:
  display:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "30.2cqw"
    fontWeight: 400
    lineHeight: 0.8
    letterSpacing: "0.01em"
  headline:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(3rem, 2.2rem + 3.4vw, 4.5rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.005em"
  headline-lg:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(3.75rem, 2.6rem + 5vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.005em"
  headline-sm:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(2.5rem, 2rem + 2vw, 3.1875rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.005em"
  title:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "clamp(1.75rem, 1.5rem + 1.1vw, 2.25rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.02em"
  label:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "1.3125rem"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "0.08em"
  button:
    fontFamily: "League Gothic, Arial Narrow, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.03em"
  lede:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "clamp(1.4375rem, 1.3rem + .5vw, 1.5625rem)"
    fontWeight: 600
    lineHeight: 1.35
  quote:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "clamp(2.5rem, 2rem + 2vw, 3.1875rem)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Besley, Georgia, serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
rounded:
  keyline: "2px"
  button: "3px"
spacing:
  s1: "8px"
  s2: "16px"
  s3: "24px"
  s5: "40px"
  s7: "56px"
  s12: "96px"
  s14: "112px"
  gutter: "clamp(16px, 5vw, 56px)"
  col-gap: "24px"
components:
  button-call:
    backgroundColor: "{colors.ochre}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.button}"
    padding: "12px 22px 10px"
    height: "56px"
  button-call-hover:
    backgroundColor: "{colors.ochre-lit}"
    textColor: "{colors.ink}"
  button-call-block:
    backgroundColor: "{colors.ochre}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.button}"
    padding: "12px 22px 10px"
    height: "56px"
    width: "100%"
  chip-pounce-on-white:
    textColor: "{colors.brick}"
    rounded: "{rounded.keyline}"
    padding: "1px 8px 2px"
  chip-pounce-on-brick:
    textColor: "{colors.white}"
    rounded: "{rounded.keyline}"
    padding: "1px 8px 2px"
  chip-pounce-on-ink:
    textColor: "{colors.ochre}"
    rounded: "{rounded.keyline}"
    padding: "1px 8px 2px"
  field-brick:
    backgroundColor: "{colors.brick}"
    textColor: "{colors.white}"
  field-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.white}"
    padding: "56px 24px 40px"
  field-white:
    backgroundColor: "{colors.white}"
    textColor: "{colors.ink}"
---

# Design System: Savarino's

## Overview

**Creative North Star: "The Painted Wall on 11th Street"**

The page is the building. Every surface is a wall a sign painter worked on: white plaster ground, brick-red courses with the mortar showing, a lamp-black menu board hung on the brick, and ochre sign paint reserved for the things you act on and the numbers you dial. Type is what a painter would letter: condensed American gothic caps for anything painted, a Clarendon for anything spoken. Structure comes from painted rules, never from boxed cards.

The density is a sign's density: a few big words, then plain sentences. Fields stack full-bleed down the page and alternate white and brick, with the black board and footer as the darkest paint; white leads, brick follows, ink is the smallest share. Anything not yet known or photographed is left as a sign painter's pounce layout: dotted outline, labelled, clearly unpainted. The one motion that carries meaning is the wall repainting itself through the building's past lives.

The confirmed anti-reference is the food-photo bakery template: cream grounds, script faces, soft cards and glossy hero photography.

**Key Characteristics:**
- Three paint fields (white, brick, ink), each re-tinting its own secondary text, rules, focus ring and placeholder ink.
- League Gothic uppercase for everything painted; Besley for everything read.
- Hairline and 2-3px painted rules divide content; no bordered cards, no shadows.
- Ochre is the call to action and the phone number, nothing decorative.
- Dotted means unpainted: placeholders are pounce patterns, never grey boxes.
- Mortar courses read through painted lettering on the hero sign and the repaint wall.

## Colors

A sign painter's short kit: white, brick, lamp-black and one can of ochre, with warm tints of each for secondary text.

### Primary
- **Sign-Painter's Ochre** (`ochre`): the call button face, board titles and the star sandwich name, the descriptor under the wordmark, the footer mark, "since" stamps on the board, focus rings on dark fields, text selection, and pounce ink on the black board. It is the paint for calling and for numbers. Hover lightens to **Fresh Ochre** (`ochre-lit`).

### Secondary
- **Eleventh Street Brick** (`brick`): full-bleed wall fields (hero, pans, the repaint wall, visit, and the surround of the board), section titles on white, timeline years, quote marks, and pounce ink on white. Also the browser theme color and scrollbar thumb.

### Neutral
- **Painted White** (`white`): the ground of every white field and the lettering color on brick and ink.
- **Lamp-Black** (`ink`): body text on white, the menu board and footer fields, the call button keyline, and heavy 2px section rules on white.
- **Worn Ink** (`ink-2`): secondary body text on white.
- **Brick Wash** (`on-brick-2`): secondary text, fact keys and the phone nav on brick.
- **Board Chalk** (`on-ink-2`): secondary text on the black board and footer.
- **Ink Hairline** (`rule-ink`) and **White Hairline** (`rule-light`): 1px dividers on light and dark fields respectively.

### Named Rules
**The Field Owns the Ink Rule.** Every section declares one field (white, brick or ink) and the field sets its own secondary text, rule, focus and pounce colors. Never hard-code a secondary color inside a component; read it from the field.

**The Ochre Is for Calling Rule.** Ochre marks the call to action, the phone number, and the painted headline on the board. It never becomes a background wash, a divider, or ornament.

## Typography

**Display Font:** League Gothic (with Arial Narrow, sans-serif)
**Body Font:** Besley (with Georgia, serif)

**Character:** A condensed American gothic, always in caps, does every job a brush would do on a wall: the name, section titles, product names, labels, the phone button. Besley, a Clarendon, carries the family's voice in sentences, with weight 600 for ledes and 800 for the one pull quote.

### Hierarchy
- **Display** (400, sized to the container at 30.2cqw, line-height 0.8): the SAVARINO'S wordmark only, filling the sign width at every size.
- **Headline** (400, uppercase, line-height 0.9): section titles on the middle step; the board title, the star sandwich and the visit address step up to the large size; shelf names, the descriptor and porch title use the small size.
- **Title** (400, uppercase, 0.02em tracking, line-height 1): individual goods and family pans.
- **Label** (400, uppercase, 0.08em tracking, line-height 1.2): definition keys (Today, Find us), wholesale fact keys and the "since" stamps on the board. Nav uses the same face at 1.1875rem with 0.07em tracking.
- **Lede** (600, line-height 1.35, max 26-36ch): the one-line offer, section ledes, the wall caption.
- **Quote** (800, line-height 1.08, -0.01em, max 14ch): the press pull quote, with a hanging opening mark from 600px.
- **Body** (400, 17px, 18px from 1080px, line-height 1.55, max 44-62ch).

The scale is a square-root-of-two ramp (tokens t1 to t6); it hits roughly 1.41 between steps at the top of each clamp and compresses on phones so the smaller steps do not collide.

### Named Rules
**The Brush or Voice Rule.** If it would be painted on the wall, set it in League Gothic caps. If someone would say it, set it in Besley sentence case. Never set Besley in caps or League Gothic in lowercase.

**The Tabular Number Rule.** Phone numbers, street numbers and years are set in the display face with tabular figures and slight tracking (0.02-0.05em).

## Layout

Mobile-first single column inside a fluid gutter (`gutter`), capped at a 1440px wrap. At 720px, content pairs into two columns with the 24px column gap. From 1080px everything sits on a **seven-column grid** (24px gap): section heads split 3 columns of title to 4 of lede via subgrid, and content blocks use 3/2/2, 4/3 and 2/3/2 splits. The first viewport on desktop places the sign across all 7 columns and the offer, today's facts and the call button beneath in 3/2/2.

Spacing is an 8px rhythm stepped on primes (1, 2, 3, 5, 7) plus 12 and 14: 8, 16, 24, 40, 56, 96, 112. Sections pad 96px on phones and 112px from 1080px; section heads sit 56px (96px desktop) above content; list rows pad 16-40px. The black board is inset inside a brick surround and caps at 1328px.

A sticky ink call bar appears at the bottom on phones only, once the hero's call button has scrolled away.

## Elevation & Depth

Flat. There are no shadows anywhere; depth is paint order. A field is either the wall (white, brick) or something painted or hung on it (the ink board inside a brick surround). The only texture is the mortar course: a 64 by 40px running-bond pattern of 1.5px black lines at 13% opacity, tiled on every brick field. On the hero and the repaint wall the courses are lifted into an overlay above the lettering so the bricks read through the paint, while navigation, facts and buttons stay above it.

### Named Rules
**The Paint Has No Shadow Rule.** Paint sits in the surface. No drop shadows, glows or offset shadows on type, buttons or fields.

**The Mortar Shows Through Rule.** Large painted lettering on brick sits under the mortar overlay, not on top of it. Interactive elements sit above.

## Shapes

Square and painted. Corners are near-sharp: 2px on placeholder outlines and focus rings, 3px on the call button. Rules do the structural work: 1px hairlines between list rows, 2px ink or light rules to open a menu, shelf or timeline, a 3px white rule under the wordmark and above the porch. The only closed outlines are dotted (pounce placeholders) and the ink keyline of the call button.

## Components

### Buttons
Painted, loud and square: the call button is the only button that matters.
- **Shape:** near-square (3px radius), 2px lamp-black keyline, minimum 56px tall.
- **Primary (call):** ochre face, ink text in League Gothic caps at 1.75rem, "Call to order" plus the number in tabular figures, wrapping as a pair. Full width in the hero, sticky bar, pans, wholesale and visit; natural width on the board foot.
- **Hover / Focus:** lightens to fresh ochre over 150ms ease-out; presses down 1px on active; focus is a 3px outline offset 3px in the field's focus color (ink on white, ochre on brick and ink).
- **Text link:** Besley 600, 2px underline at 0.22em offset, thickening to 3px on hover. The repaint wall's replay control is a text link with an ochre underline.

### Chips
- **Style:** the pounce chip. Transparent, 2px dotted outline in the field's pounce color (brick on white, white on brick, ochre on ink), Besley 600 at 0.875rem, text reading "X: confirm with owner".
- **State:** static; it marks an unknown and disappears when the real value is painted in.

### Cards / Containers
There are no cards. Lists are stacks of rows separated by rules. The **pounce frame** is the image container: a 2px dotted outline at the placeholder's target aspect ratio (3:2 on phones, the shot's own ratio on desktop, default 4:5), with dotted registration ticks centered on all four edges and a label naming the exact shot in the display face ("PHOTO:"), the subject in Besley 600 and the spec in italic.

### Navigation
League Gothic caps with wide tracking, text only, underlined in ochre on hover. On phones it becomes a single horizontally scrolling line in brick wash that fades out at the right edge.

### The Menu Board
The signature component. A lamp-black field hung inside a brick surround; ochre title at the largest headline step; each sandwich is a row with its name in white display caps, a one-line story in board chalk, and an ochre "since" stamp or pounce chip. The star item (the Palermo) steps up to the large headline in ochre and pairs with a pounce frame.

### The Repaint Wall
The single delight. On a brick field, JAIL, HOTEL, UPHOLSTERY and SAVARINO'S are lettered in white display caps at container-relative sizes, each letter brushed in top to bottom (340ms, 70ms stagger, expo-out) with a one-line caption, earlier words fading to 15% as ghost signs. Plays once when 55% in view, offers "Paint it again", and shows the finished state with no motion under reduced motion.

## Do's and Don'ts

### Do:
- **Do** assign every section one field (white, brick or ink) and let it supply secondary text, rules, focus and pounce colors.
- **Do** keep ochre for the call button, phone numbers and board headlines; every call button is ochre with a 2px ink keyline.
- **Do** separate content with rules: 1px hairlines between rows, 2px rules to open a list, 3px white rules on brick for emphasis.
- **Do** mark every unknown with a dotted pounce chip or pounce frame that names exactly what is missing.
- **Do** lay out desktop on the seven-column grid with the 24px gap and space with the 8/16/24/40/56/96/112 steps.
- **Do** tile mortar courses on brick fields and lift them above big painted lettering.

### Don't:
- **Don't** use cream grounds, script faces, soft rounded cards or glossy food-photo heroes; that is the bakery template this world rejects.
- **Don't** draw solid-bordered boxes around content; closed outlines are only the dotted pounce or the call button's keyline.
- **Don't** add shadows, glows or color gradients to fields, type or buttons.
- **Don't** fill a missing photo with a grey box, stock image or blur; use the pounce frame.
- **Don't** set League Gothic in lowercase or Besley in caps.
- **Don't** add a second animated moment; the wall repaint is the one delight, and all motion yields to reduced-motion preferences.
