# Savarino's Market: concept notes

A two page concept (Homepage, Menu) for Carmelo Savarino. These notes are for whoever presents it. Keep them out of anything you deploy.

## The layout idea

**The site is the sign, continued.** The logo's ivory field, navy lettering, teal rules and saffron dots run the whole page. Nothing new is invented: the headings use Abril Fatface, the closest match to the SAVARINO'S wordmark, the labels and body use Montserrat, the wide clean sans from the register screen, and the corner flourishes are traced from the logo's own maiolica corners.

**Rail and field.** The grid is lopsided on purpose, about one part rail to five parts field. Section names sit in the narrow rail, the content hangs in the wide field, and the only centered thing on the page is the logo lockup. The page runs in three equal acts: come in (hero, know before you go, the eight words), order (crowd favorites, catering and cakes, wholesale), trust (proof, family, footer). Spacing moves in short beats of 8, 16, 24, 40 and 64px with a rare long pause of 104px. No two neighboring sections share a structure, so nothing repeats like a template.

**The eight words are the spine.** They sit in two dotted lines above and below the logo, exactly as on the register screen. They return as eight blocks in two rows (Sandwiches and Pastries are the navy blocks, so the grid does not read as eight identical cards), as the eight section headings on the Menu, and as one dotted line in the footer. Each one links to its Menu section.

**The tiles run down the page.** The maiolica tile from your logo appears three times, always as a single full width row: a slim one under the hero (it opens the navy Know before you go room), a slim one before Wholesale, and the full one in the footer. They mark where the page turns from ivory to navy. They never sit behind text. The original brief asked for the footer band only; the other two were added after the first review.

**The menu is a deli board.** Names, dotted leaders, `$00`. No cards. On a phone the eight categories stick to the top and follow you down the page. On a desktop they sit in the rail.

## The delight moment

**Fill the cannoli.** In Crowd Favorites the cannoli starts as an empty engraved shell. Tap it, or tap Fill it, and the ricotta fills both ends, left then right. The cannoli is lifted from your own logo, so it matches the etching exactly. It happens once, on purpose, where it belongs: cannoli filled to order is one of the most repeated things in your reviews. With reduced motion switched on it simply changes state.

## Things that work today

- The open or closed line is computed from the hours in Central time. Add `?now=2026-10-10T16:30` to the address to preview any moment (read as Central time).
- Tap to call in the hero, the sticky mobile bar, the header and the footer. Directions open Google Maps.
- Designer notes (the gold boxes) can be hidden with the button in the top bar. They are remembered per browser.
- Both forms check their fields (a real phone number, a date that is not in the past) and show a confirmation. They do not send anything yet.
- The hero says "Yes, we're open." only while the shop is actually open. When it is closed the line disappears and the status line says when you reopen.
- On short phones (under 800px tall) the hero puts the status, address and phone first and the headline and buttons after, so the facts stay above the bottom bar.

## CONFIRM WITH OWNER

Every one of these is also marked on the page in a gold box.

1. **Prices.** Every `$00` on the Menu.
2. **Lead times.** How much notice cakes, cookie trays, the family meal and catering need. Notice, sizes and flavors for custom cakes.
3. **Catering terms.** Minimums, pickup or delivery, deposits, order sizes the form should offer, and the catering menu.
4. **Accessibility.** Porch steps or ramp, door width, restroom, how many outdoor tables.
5. **Daily specials.** How to show what is in the case today, and when hot food runs out.
6. **Hours.** Holiday and seasonal hours. The hours shown are the ones supplied.
7. **Parking.** Where the gravel lot sits, any time limits or signage, and whether customers may use it. The diagram is a sketch, not a survey.
8. **Sandwich details.** What goes on The Sicilian, The Corrado and the classics, which names are still on the board, and who each was named for.
9. **Focaccia.** What time it comes out on Fridays and whether it sells out.
10. **Family-size pans.** Sizes and how many each feeds.
11. **Where forms go.** Email, text or phone, and how fast the family can promise to answer.
12. **Wholesale.** Delivery area, delivery days, minimums, lead times, and a wholesale email or direct line.
13. **Press.** Exact Nashville Scene wording and permission, and the Diners, Drive-Ins and Dives details.
14. **Reviews.** Three real Google reviews to paste in, with names as they appear.
15. **Photos.** One temporary photo (a toasted meringue drink in a green glass, not a muffuletta, with a child's hand in it) stands in for the muffuletta shot on both pages and is labeled "Temp photo". Every other frame is a placeholder that names its shot. People photos need the family's okay.
16. **Social links.** Instagram and TikTok links are built from @savarinosmarket. Check they land on the right accounts.
17. **Headline and voice.** The hero line and every other line of copy.

## What to replace before launch

- The `noindex` meta tag in both page heads. Remove it, or the site will not appear in search. It is there so the concept does not get indexed under the real business name.
- `SITE_URL` in `tools/build_pages.py`, then rerun the script. Set it to the deployed origin so the link preview image works. The images are `assets/img/og.png`, `apple-touch-icon.png` and `favicon-32.png`.
- The form confirmation heading reads "Nothing sent yet." because the forms send nothing. Change it back to a real confirmation when the handlers are wired.

- Placeholder photo frames, review slots and `$00` prices.
- The form handlers. The simplest route on Cloudflare Pages is a Pages Function that emails the family, or a form service pointed at the family inbox.
- The parking sketch, if the family prefers a photographed or surveyed version.
- The map in the footer is a live Google embed; it needs an internet connection to draw.
