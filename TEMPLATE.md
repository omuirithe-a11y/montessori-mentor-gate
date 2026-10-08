# THE DESIGN TEMPLATE

## Rules of 7 Oct 2026 (chat 21) - these supersede what is below where they disagree
- **EVERY FIGURE OF THE TEXT SPACES APPLIES ON PHONES TOO (390 and 640), not only on the desktop.** They are worked out AT THE BUILD -
  the figure less the half-leading above and below it, from the phone's own lettering (PHONE_HALF in site/pages/source_steps_page.py:
  body 7 each side, a quotation 9.5 above and 0 below, a blue heading 5) - and written into the page's own stylesheet, one class per
  figure. A QUOTATION takes data-space-phone instead, which the engine swaps into data-space at phone widths (the engine spaces a
  quotation with padding of its own, which no stylesheet rule can reach, and its step from the source replaces any figure given to it).
- **THE FREEZE.** The last step of every build opens the built page at 390 and measures every space the template set, letters to letters,
  writing the difference back into the page (`sh p41/build.sh final` runs it; site/pages/source_steps_page.py freeze_phone). Nothing is
  measured at the reader's end: a pass that did was right on the first load and wrong on 92 of 96 spaces after a scroll.
- **THE BEIGE LINE'S SPACE IS SET LAST OF ALL** (glFix in site/template/mm_template.py), from the letters above it, after the engine and
  the page's own placing have finished - 30 above and 30 below, at every width, however late the photos arrive.
- **THE DESKTOP PASS SETTLES IN EIGHT PASSES** and runs again whenever the engine finishes a layout.
- **A WRAPPING TAB LINE (p.mm-hang) READS AS PLAIN TEXT ON A PHONE** - no tab column, no hanging indent; the desktop keeps its columns.
- **CHECKED BY IK1 (qa/ink_check.py) AT 1440, 1088 AND 390**: IK1a the beige lines, IK1b no block past its own last letter, IK1c every
  block the template spaced standing its figure, by whichever route that figure reaches the page.

## Rules of 7 Oct 2026 (chat 20) - these supersede what is below where they disagree
- **A slash between words carries no spaces**: "Junk/Adventure", not "Junk / Adventure". Every page, the menu included (SL2).
- **Every photo fills its frame.** The 15% rule of 5 Oct is DELETED - "Always crop photos to fit" (CK9, turned round).
- **The menu's panels open on a click, not on hover** (HV1). The keyboard still opens them; a link still underlines under the pointer.
- **Every audience card carries the navy band** with the standing footer quotation ("I obtained most surprising results ...  - Maria Montessori.") whether or not its own document names one (CK10).

**Last updated: 4 October 2026, chat 7 ("Mathematics Curriculum 7"), template step 4.** The wording this file held before
the clean, with every superseded value and its history, is in references/archive/TEMPLATE-before-4oct-clean.md and
references/rules-history.md. Nothing here is re-opened without the user.

**The authority for every curriculum page is the live Mathematics page** (montessorimentor.co.uk/the-mathematics-curriculum/;
the user, 3 Oct: "This final version of the Mathematics page is perfect. Font size and colour. Headings and sub-headings size
and spacing. Line spacing. Placement of images horizontally and vertically, size of images. Etc."). Its rules are code:
`site/pages/curriculum_rules.py` (THE CURRICULUM-PAGE RULES - every new page starts from it; a page's own settings hold data
and hooks only); its values are a record: `qa/reference.json` (measured from the live page 4 Oct by `qa/ref_spec.py`); the
check RS1 (in the gate) fails any curriculum page whose measured values differ, unless the page's settings name the value
in SPEC_EXCEPTIONS. **Where this file and the live page disagree, the live page is right - correct this file.**

Two kinds of page share one engine: **curriculum essays** (The Practical Life, Sensorial, Culture, English Language and
Mathematics Curriculum; The Montessori Curriculum, Scope and Sequence) and **resource lists** (the Resources pages).

## Files and tools
- `site/template/mm_template.py`: the shared engine (menu, hero, photos, spacing, phones). Nothing page-specific.
  `site/template/curriculum.py` / `resources.py`: what only that kind needs. `site/template/protect.py`: copy protection.
- `site/pages/frame.html`: the approved page frame. `site/pages/rules_2oct.py`: css(KIND), apply(api, KIND) - the 2 Oct
  values for both kinds. `site/pages/curriculum_rules.py`: everything a curriculum page does, driven by the page's data.
- A page's settings `site/pages/<page>_settings.py`: for a curriculum page, data (SOURCE_DOCX, SOURCE_PDF, GEOM, HERO, the
  named photos, captions, TOC_MODEL, the user's one-off values) and PAGE_<hook> functions, then as its last lines run the
  rules (precedent: math1_settings.py, 263 lines). Resources pages: as culture_resources_settings.py (precedent).
- `site/convert_curriculum.py <docx> <pdf> frame.html src.html /<link>/ "<Title>" --settings=<settings> [--photos=a,b] [--preview]`
  reads Word as rules (title; blue/red lines on their own = headings; short bold lines = labels; italic quotation + its
  attribution; lists; tables; links, italics, bold, underline, inline colours; hidden text left out; every photo as Word
  crops it - a:srcRect; a photo turned in Word turned) and the PDF for which photos stand together and beside what.
  `--photos=` names folders of working copies, comma-separated, the first that has a photo wins; `--preview` = 900px photos.
- `site/make_page.py src.html out.html <page>` applies the engine and the page's settings; `MM_FULL=1` adds the copy
  protection (final build only). `math/pdf_geom.py` (3.6.1 precedent) reads every picture's PDF box -> GEOM json.
- `site/rename_photos.py full.html out.html map.json` renames the final page's photos to page order in EVERY attribute.
  `site/split_photos.py full.html <out_dir> [--preview p.html]` -> index.html + images/ (refuses Word names or no protection).
  `site/shrink_preview.py built.html preview.html [--long=500]` the light preview copy. `site/add_protection.py`.
- Checks (all run by `qa/preview_gate.py page.html --page=<page>`, which stamps a page only when every one passes):
  `qa/check_layout.py` (the layout rules at 1440/1170/1024/390; CP1-3; ST1); `qa/pdf_place.py` PL1 (every photo where the PDF
  has it); `qa/word_check.py` WD1 (every word in its Word colour); `qa/pdf_size.py` PL2 (placement from the PDF, sizes from the
  rules, the painted picture); `qa/ask.py` AS-steps / text / indents / gaps / photos (the 3 Oct rules, every instance listed);
  `qa/phone_check.py` PH1 (390px: stable, no overlap, no empty band over 400px); `qa/ref_spec.py` RS1 (the reference spec).
  `qa/pdf_compare.py` (the PDF comparison record), `qa/preview_log.py` (every preview a new link), `qa/scroll_test.py`.
- Page exceptions: `EXCEPTIONS = {'<check code>': '<the user's edit and date>'}` (check_layout, PL1, WD1);
  `SPEC_EXCEPTIONS = {'<kind> <property>': '<the user's edit>'}` for RS1. The user's edits are known to the checks by name:
  REMOVED, ADDED, NEW_PHOTOS, ROW_ORDER, MOVED, UNDER, BETWEEN_LINES, STEP_EDITS, STEP_CUT, TEXT_FIXES, TEXT_SUBS,
  data-colour-exception - a check never passes a fault by these; each names one photo, row or line of the user's.

## Vocabulary
**Set** - photos that belong together, beside text or in a row. **Row** - photos side by side across the column, between
paragraphs. **Group** - rows stacked with nothing but captions between them. **Pair** - two photos under one caption.
**Centred on the page** - equal space to the left and right margins. **Gap** - the space between photos side by side.
**Line unit** - the page's own body line step (37.2px); steps between text blocks are counted in it (1.00 / 1.33 / 1.64).

## Look (the reference values, measured on the live Mathematics page 4 Oct at 1440px; phones 390px in brackets)
- Typefaces: Vollkorn for the site name and page titles; EB Garamond for everything else. Background Oat #F5EEE3; the
  menu bar navy #1E4D7B; body text #2B2B2B. Column 1140px at 150px from the left (342px at 24px).
- Body text 18px, 37.2px lines (= 14px between the letters of one line and the next) (17px / 36px). Lists 18px, 29.7px
  lines, numbers and dashes at the margin, the text 31px in (dash lists 62px; a dash list inside a numbered item 93px).
- Title (hero) 40px (28px), white Vollkorn on the hero photo with a corner gradient; a Word title "A: B" shows B with A on a
  second smaller line.
- Section headings (the red ones in Word - the Contents headings) 22px Regular #EE0000 with a full-width 2px red line 8px
  under the letters (20px on phones). 45px from what is above to the heading's letters; 25px from the line to the first text.
  **Black sub-headings** (h2 not red in the Contents) 20px bold #2B2B2B, no line. Blue h2 lines in Word are NOT headings:
  they are **names of materials / activities** - 20px Regular #0432FF body lines, a full-width 2px beige line #E7DCC6
  28px above the letters (the user names the sections and names that take no line), 2.46 lines above (= 1.64 x 1.5).
- Labels (Word's short bold black lines: Materials, Aims, Presentation, Exercise 1, Control of Error, Age, Notes ...) 18px
  bold #2B2B2B, 29.7px lines. **Text in red, blue, green or orange is never bold** (Word's bold or not) - one exception
  the user named on 3.6.1 (orange "Second Period - Experience / Practice"), recorded in its settings.
- Captions (Word's text boxes) 16px italic in Word's colour, centred over (or under) their photos; one caption over a pair.
- Quotations 17px italic, the box 20px in from both margins, the text 31px in (the indent set); attribution in round brackets.
- Contents box: no "Contents" label (removed 3 Oct on 3.6.1; all pages at the review); an Introduction entry first; three
  columns read downward, each red heading with its entries, entries 19px (18px), red headings red; one column on phones.
- Links in the title blue #0432FF. Orange text black - ALWAYS, also a run inside a line that mixes colours (a quotation in orange, then its black attribution): it takes the page's text colour, italic kept (4 Oct 2026, chat 10, "Orange quotations are always changed to regular black"; built in curriculum_rules.py, THE ORANGE RULE; Resources pages: when the next one is built; finished pages: at the review). Short dashes everywhere (every long dash shown as "-").
- Tables: the "How to touch" style - a hairline #E6E6E4 above the header row, under it and under every row; 16px above and
  below the text; 24px between columns; no vertical lines, no outer box; only the header row bold, coloured headers not bold.
- Menus: no lines; only the current-page markers. Curriculum menu order and dropdown columns: mm_template.py CURRICULUM.

## Text rules (curriculum pages; site/steps.py, qa/ask.py)
- **The source is the document.** Structure from the Word document, geometry from the PDF (a rendering): a soft wrap in
  the source is never a break on the page (only <w:br/> or a new paragraph); tab columns come from Word's TAB STOPS, laid
  out at any width (TABSTOP_JS); every paragraph without <w:br/> is ONE unbroken block (AS-text).
- **Every step from the source, at the template's values:** the page has ONE line unit; every step between text blocks is
  1.00 (a line), 1.33 (after Word's w:after=120) or 1.64 (before a bold sub-heading / the next name), which one decided from
  the PDF's rendered step (mechanism-blind: an empty paragraph, w:after or a page break all count as the step they make).
  A blank line in Word is a blank line on the page, always and only where Word has one. A text step runs over a caption;
  text never clears a photo - only a heading does. A bold sub-heading is one line from its first line. (AS-steps.)
- **THE MATERIAL BLOCK:** [1.64] Name · [1.00] one-line description · [1.33] **Materials** [1.00] its lines · [1.64] **Aims**
  · [1.64] **Presentation** (its lead line, then the numbered list, items 1.00 apart) · [1.64] **Exercise n** · [1.64]
  **Control of Error** · [1.64] **Age** · [1.64] **Notes**. No other gap exists inside a block.
- **The indent set 0 / 31 / 62 / 93px** (at the 1140px column): every text block at the value nearest its PDF indent (a tie
  to the larger); ONE mechanism - padding-left on the block, text-indent 0. Captions and Word's columns are not indents.
  (AS-indents.) **One mechanism per visual property; a run of lines the source treats identically is identical on the page.**
- **Follow the Word/PDF:** colours of headings, labels and words inside lines (WD1), bold, italic, underline, lists and
  their numbering, Word's columns (two-column lists and sections, the three periods side by side), captions, which photos
  stand together and where. Where a rule and the Word/PDF conflict, the Word/PDF wins; the user's own answers stand over both.
- **THE WORD-PAPER RULE:** formatting whose only purpose is to overcome Word's white paper (a highlight behind white text)
  is not carried over; every highlighted or near-white run is LISTED at build time and decided once (3.6.1: "7. White" stays
  white with a 0.4-0.6px #8A9099 keyline).
- **No wording of Claude's on the page**: the text comes from Word word for word; the user's rewrites are TEXT_FIXES /
  TEXT_SUBS in the settings (named, counted by the checks).

## Photos (THE SOURCE PLACEMENT RULE and THE PICTURE RULES - PL1, PL2, AS-photos, AS-gaps)
- **Size from the rules, never from the PDF:** every photo 168px tall (a row that would not fit the column shrinks to fit;
  a group of rows takes the one height its widest row fits at). Bigger or smaller ONLY when the user names the photo
  (PDF_SIZE: the PDF's size and place; SMALL: a named height; FIT_TEXT: as tall as the text beside it). No automatic exception.
- **Place from the PDF:** side of the text (float on the PDF's side, its distance from the margin as in the PDF; the
  user's MOVED photos excepted and marked), which photos stand together (one PDF row = one row; pairs stay pairs), their
  order (ROW_ORDER names the user's reorders), a row's place between its paragraphs. On phones: order and pairs kept, photos
  44vw wide, rows wrap, photos beside text become rows (PH1).
- **The picture fills its frame as Word fills it:** the frame is Word's shape (its crop applied, a:srcRect; NO_CROP only
  for a photo the user names); never letterboxed, never short (object-fit fill/cover). Every check measures the PAINTED
  picture, not the frame (ratio within 2% of Word's frame, fills it within 1px, same-height photos within 1px).
- **A photo beside text is centred on the text beside it** (the PDF lines on its text side that overlap it; headings and
  the line the PDF puts below the photo excluded), within 3px (PL2). Where no centred place exists (centring re-wraps the
  paragraph above) it takes the LOWER place, at most one line below centre (data-nocentre). Named exceptions: TOP_ALIGN
  (top on the first line of the text beside it - the Group photos, Summary), BOTTOM_ALIGN, BETWEEN_LINES (centred between
  the beige line above its name and the next), RIGHT_EDGE (a column of photos sharing one right edge).
  Photos Word stacks beside the same text keep the PDF's space between them. 24px between a photo and the text beside it.
- **Beside or below, line by line:** a text line the PDF puts above a photo's bottom sits beside it; only a line the PDF
  puts below it starts below it. A photo never sits outside the column (THE COLUMN RULE): a right-hand photo's right
  edge is at the column's right edge; it moves left, its size unchanged. A photo starts below a heading's red line, never
  across it. A heading beside a photo stops short of it.
- **THE ROW SETTINGS (every row of photos between paragraphs):** gaps 25px; 80px between the pairs of a row of pairs;
  30px from the text above to the row's top (captions included); 64px from the photos to the text after; 48px between
  stacked rows, 77px where the lower row carries captions over its photos (one value per kind, PL3 / AS-gaps). Rows of
  4 or more photos CENTRED on the column; 3 or fewer at the LEFT margin. The user names exceptions one by one (CENTRE_ROWS,
  ROW_GAPS, ROW_ABOVE, UNDER - each marked data-exception on the row). A group of rows shares ONE span - the widest row's
  width at 168px, never wider than the column: photos stay 168px and the narrower rows' gaps grow equally. Rows of two pairs
  are placed by the centre axis: the 80px gap on the column's centre, so photos 2 and 3 line up in two columns.
  **Vertical rhythm is regularised, not copied:** each kind of step has ONE value on the page; the source decides which kind.
- **Captions:** from Word's text boxes, with their photos as in the PDF; a caption over a photo beside text is part of its
  box. Captions over the photos of a row: the row's top is the top of its captions.
- **THE CONCRETE-TO-ABSTRACT TREATMENT:** every "concrete to abstract" progression is a slim graduated bar under the row of
  materials - navy #1E4D7B at the concrete end to pale #D9E2EA at the abstract end, 6px, no arrowhead - with the words
  CONCRETE and ABSTRACT in small caps at the ends and a tick under the centre of each photo above (names only where the
  user asks); without a row to align with, the same bar without ticks; on phones vertical with the labels beside it.
- Word's two-column blocks of material (3.6.1 Group 5): a 2x2 grid read across, each block's photo on its right, the photo's
  top on the first line of text under its name, photos lined up in rows and columns (GRID2; the page's height and gap).
- Every photo opens in the lightbox (previous/next, counter, arrow keys, swipe); photos that stand together page together.
- Faces, watermarks, originals: SKILL.md. Working copies only; originals never altered.

## Copy protection (every page, only in the final build)
Text of the content (hero title and main#content) cannot be selected, copied or cut; right-click and dragging off on every
photo and in the lightbox (phones: the long-press menu); links and the menu keep their right-click. Previews carry none;
`MM_FULL=1 site/make_page.py` adds it; split_photos.py refuses a page without it. Checks CP0 (preview: none), CP1-CP3.
Settled - do not raise again: the limits of this protection were explained and accepted on 28 Sept.

## Photo files and page weight (every Hostinger page)
index.html + images/: every photo twice - `<n>-480.jpg` on the page (long side 480px, JPEG 82, loaded as the visitor
scrolls) and `<n>.jpg` in the lightbox (long side up to 1600px, JPEG 85, never enlarged); the hero `images/hero.jpg` at its
own size; JPEG only. **Names are page-order numbers 002, 003 ... (001 the hero), never Word numbers** - the same numbers as
the private full-size folder. Previews (claude.ai) are one self-contained file under 16 MB: photos 900px, 500px when the
page would be over 16 MB (never the hero). Hostinger's CDN re-compresses photos (the hero served at 1600px): compare a live
page's index.html byte for byte, its photos by picture.

## Resources pages (every Resources page; engine site/template/resources.py, values rules_2oct.py)
- Colours as in Word: section headings green #00B050 (35px before, 20px after), sources red #EE0000, titles blue #0432FF,
  links in the title blue #0432FF, PDF badges in the link blue, text black. Type: headings 20px, everything else 18px
  (phones 19 / 17). Nothing in red, blue or green is bold; Word's black bold stays bold (labels inside entries: 24px before,
  10.7px to their text; paragraphs 21px apart; lists 23px from a paragraph). Quotations italic; book titles italic in lists
  of books (not a book on its own title line); nothing else italic.
- Title lines: each link, date and PDF badge its own part, 24px apart, lines 14px apart; a badge and its date are a pair
  (10px between, 30px after). Lists of links 11px apart; a book 42px before its title and 10.5px after it; 30px from a
  book's description to the next title in a list; 40px between entries; 10px from a red source to its first line.
- Photos beside an entry 180px wide, shape kept, centred on their text; rows one height (150px at 1440, shrinking together);
  64px above a row; background Oat; body lines 37.2px.
- Hidden Word text left out; links in Word fields become links; a red source that is a link stays red and starts its own
  entry; Word's column on source lines (badges lined up at the widest name + 24px). The creators' marks on other people's
  work (charts, printables) stay; copyright notices are never removed.

### Rules of 4 Oct, chat 9 (every page)
- PDF badge: 30px after the last letter of its title or text (THE PDF GAP RULE; was 10px / 24px). No badge columns. After a date: 10px.
- Photos of objects on white: the white painted Oat #F5EEE3 (site/mask_white.py). Book covers and pages keep their white.
- One line pitch for every wrapping text block: 37.2px (phones 36px) - paragraphs under a heading too (rules_2oct RESOURCES styles only p.res-desc; 3.6.2 adds
  `main section.section>p` by CSS and, on phones, pitch() in its QUEUE_JS).
- 3.6.2's own values (this page only until the user answers open question #14): blue title line -> its description 30px, description -> next blue title line 60px,
  green heading -> first line 70px (main data-head-after=35), 42px under a bold heading, no beige lines, the first line 42.5px under the Contents list.
- The Contents label reads "Table of contents".

## Phones (640px and narrower)
Photos below their text as rows, 44vw wide, order and pairs kept; Word's columns one after another; tab columns stacked;
quotations without side margins; one Contents column; the concrete-to-abstract bar vertical. Checked by PH1 at 390px.

## Hostinger (every page)
What to tell the user: only the name of the folder to create in public_html and the zip (the user unzips on the Mac and
uploads index.html and images/; Hostinger takes no zip upload; the folders are new). Then check the live page: index.html
byte for byte, every photo file loads, layout identical to the tested page at 1440/1024/390, copy protection on,
qa/scroll_test.py 0 pull-backs.

## When the user asks for an improvement (THE BRIEF RULE - the full rule is in SKILL.md)
A request about how a page READS is never answered by editing only the examples the user gave. Build 3 or more approaches that
differ in STRUCTURE - containers, columns, order, grouping, what carries the eye - each a full page at its own link, and say which
one Claude would choose. Gaps, sizes and colours are values, not approaches. The gate refuses to stamp a preview while a brief is
open with fewer than 3 approaches built (qa/brief.py, qa/preview_gate.py).

## The finished pages and the template (the user, 4 Oct, chat 7)
At the review of all Curriculum pages each finished page is POSSIBLY rebuilt from curriculum_rules.py and the reference - decided
later, page by page. First make the template version of the page, so the user can compare the existing live page and the page made
with the new template side by side; the decision follows the comparison. Until then the finished pages keep their values.

## Making a new curriculum page (from the template)
1. Faces and watermarks on working copies (SKILL.md). `math/pdf_geom.py` on the PDF -> the page's GEOM.
2. `site/pages/<page>_settings.py` from math1_settings.py's shape: sources, HERO, GEOM, TOC_MODEL, captions; everything
   else empty; its last lines run curriculum_rules.py. No value of the user's belongs in the rules module; no mechanism in
   the page file.
3. Convert with --settings, make_page, shrink_preview if needed; the PDF comparison (qa/pdf_compare.py, every page looked
   at); the gate (--page=<page>: layout + PL1 + WD1 + PL2 + AS-* + PH1 + RS1); preview_log; the preview as a new link.
4. The user's one list of edits; every item as DATA in the settings (a named photo, row, line or step), never as code in
   the rules unless the user makes it a standing rule - then it goes into curriculum_rules.py AND this file AND the
   reference, in the same reply.
5. Final build: converter without --preview, `MM_FULL=1 make_page`, rename_photos.py to page order, split_photos.py, the
   upload page checked with a `<page>_fin_settings.py` (the names mapped), layout compared with the last preview; the
   Hostinger zip and the private full-size folder (001 hero, 002 ... in page order, INDEX.md).


## Rules of 4 Oct 2026, chat 10 (page 1.1 Montessori Mentor)
- THE ORANGE RULE: see "Orange text black" above.
- THE PDF GAP RULE on curriculum pages (curriculum_rules.py, PDFGAP_JS): a PDF badge on a Word tab line stands 30px after the last letter of its title, at any width; the tab column is dropped (your words: "PDF spacing is what was set previously - for ALL documents/pages").
- A page built from a source you wrote: THE SOURCE-STEP RULE for every block (h11_settings.py _source_steps; precedent 3.6.2).

## Rules of 4 Oct 2026, chat 11
- Resources pages: a blue title line to its description 30px; a description to the next blue title line 60px (standing, every Resources page; as 3.6.2).
- The Home menu: nine entries, columns 4 / 3 / 2 (1.8 deleted).


## THE SECTION LINE RULE (5 Oct 2026, chat 13 - the user's words: "the spaces between sections just needs to be standardised however: row of images - space - beige line - space - section heading"; "Spacing above/below beige line looks good. save these numbers to the template for all pages")
Between sections: ONE beige line (2px #E7DCC6), **30px above it and 30px below it** (7 Oct 2026, chat 19, the user's words: "the space above and below a beige line must be the same, irrespective of what sits above or below the line" and "30 above 30 below on this and every page" - SUPERSEDES the 36 / 28 of 5 Oct), measured from the letters or photos above to the line and from the line to the letters below - the same whether a row of photos, a quotation, a floated picture or text stands above.
A heading that stands just under a line Word already has (a quotation or a line or two of text between) takes no second line. SUPERSEDES the template's step before a blue heading (3.69 / 2.46 lines + 28px) and the 2 Oct "no line under section headings (curriculum)" where they differ.
Values: SEC_ABOVE = 30, SEC_BELOW = 30 in site/pages/curriculum_rules.py; checked by IK1 (qa/ink_check.py, in the gate at 1440 and 1088); first built on 4.1 Play (site/pages/p41_settings.py). Finished pages: at the review. Resources pages: with the next Resources page. qa/reference.json: to be re-measured from 4.1 when it is live.

## EVERY SPACE IS MEASURED FROM THE LETTERS - IK1 (7 Oct 2026, chat 19 - the user's words: "those huge empty spaces")
A block that has to clear a picture floating beside the text is pushed down with padding INSIDE its own box; its letters are then pulled back up to the template distance, but the box keeps the full height. Whatever follows begins at the foot of the box and not under the last line - 80 to 290px of empty page on the live 4.1, which the spacing engine could not take back (its correction came out negative and was clamped to 0).
THE RULE: a block's box ends with its last letter. site/template/mm_template.py boxEnds() gives such a block a negative margin-bottom equal to the overhang, in the spacing pass and once more after the page's own placing (which moves a quotation's letters after the engine has finished).
A full-width rule (the beige line) spans its own box, not its one blank character of ink (mm_template.py span()), and a block that carries its own space (data-space) keeps that space from a floated picture too, instead of the general 32.
THE CHECK: qa/ink_check.py - IK1a every beige line 30 above and 30 below, letters to letters; IK1b no block more than half a line past its own last letter. In qa/preview_gate.py at 1440 and at 1088. Box measurement is what let this through a green gate: LK1 counts a padded box as full page, EV1 and WS1 measure boxes.

## THE TEXT SPACING TEMPLATE (5 Oct 2026, chat 13 - the user's words: "These also come from the PDF - we need to create a template that we can use with all documents"; "Between ordinary paragraphs the line-to-line step = 40"; "Spaces above bold text = 40"; "numbered bold lines = 30")
On every page, whatever the source has: an ordinary paragraph after an ordinary paragraph - 40px from the top of the last line to the top of the first line; bold text (a bold sub-heading, a paragraph that opens in bold) - 40px of space above its letters; a numbered bold line ("1. ...") - 30px of space above its letters.
Not yet in the template (still the source's distances): the steps around lists, quotations, tables and the line after a bold sub-heading. Code: site/pages/source_steps_page.py standard_steps(); values PARA_STEP / BOLD_SPACE / NUM_BOLD_SPACE in site/pages/curriculum_rules.py. First built on 4.1 Play. Finished pages: at the review.
## THE FOOTER LINE (5 Oct 2026, chat 13 - the user's words: "The footer corner - a copyright line, \"(c) 2026 Montessori Mentor\". I'll decide on the contact details later. No need to remind me.")
The footer's left corner reads "© 2026 Montessori Mentor" (site/pages/frame.html, site/shell.py). The twelve live pages still read "Montessori Mentor" - they change with the next upload of every live page (a new page going live). Contact details: the user decides later - do not raise it.

## THE 4.1 TEMPLATE (5 Oct 2026, chat 13 - your words: "everything about this document is perfect: Font sizes, Font colours, Use of bold font, Table of Contents - layout/organisation/etc, Quotations, Spacing in every area, Spacing of beige lines, Numbered Lists, Dashed lists, Image size and placement, Heros.
Save all of these settings as a template to be used to create every document. Source documents are to be used to give an idea of where images are to be placed -roughly/approximately- but everything I have listed above (and any element of the formatting that I may have forgotten to list) is to fit this template.").
Preview 4 of 4.1 Play (p41/build/p13.html, https://claude.ai/artifact/DTKLmGNGZjPUMK6vvzxFD2) IS the template for every document: its font sizes, colours, bold, Table of contents, quotations (centred, attribution upright), every space, the section line (36 / 28), numbered and dashed lists, image sizes and placement, the hero.
A source document (Word / PDF) only shows ROUGHLY where its images go; it no longer sets spacing, indents, sizes or alignment. SUPERSEDES: "the live Mathematics page is the template" (chat 7), THE SOURCE-STEP RULE / "a page built from a source you wrote follows its spacing" (chats 8, 10), THE PDF COMPARISON as a test of spacing (it stays as a test that every text and picture is there and in order),
"follow the Word/PDF over any rule" (1 Oct) for formatting, and the PL1 / PL2 / AS-* checks where they compare formatting with the PDF.
Its record: qa/reference_play41.json (every kind of element measured, qa/ref_spec.py) and qa/template_play41_spaces.json (the space between every pair of text kinds, with counts). NOT YET DONE: (1) the code still lives partly in site/pages/p41_settings.py and still reads this page's PDF for the steps the template does not yet name -
move it into site/pages/curriculum_rules.py as fixed values with the next document; (2) RS1 still reads qa/reference.json (Mathematics) - switch it to qa/reference_play41.json then; (3) some pairs have more than one value on this page (dash item to dash item 17 / 21px; paragraph to quotation 29-42px; quotation to paragraph 29-43px; a tab line 17 or 40px under a paragraph):
one value each is to be fixed with the user BEFORE the next document is built; (4) whether the hero pictures show in turn on every section or only in Play ("in the Play section", THE PLAY HERO RULE) - ask when the next section's first page is built. Finished pages: at the review.

## THE 4.1 TEMPLATE - FIVE MORE FIGURES (5 Oct 2026, chat 13 - your answers to the examples page: "Dash item to dash item: 21px"; "Paragraph to quotation: 40px"; "Quotation to paragraph: 40px"; "A line with a tab under a paragraph: 40px"; "between two separate quotations: 40px"). Spaces letters to letters, on every page:
dash item to dash item 21; any text to a quotation 40 (built also after a numbered bold paragraph and after a list item - my reading); quotation to paragraph 40; a line with a tab under a paragraph 40; two separate quotations 40 (the lines of ONE quotation, up to its attribution, keep 16).
With the earlier figures: paragraph to paragraph 40 line to line (17 of space); 40 above bold text; 30 above a numbered bold line; the section line 36 / 28. Code: site/pages/source_steps_page.py standard_steps(). Still from this page's PDF (no figure yet): after a blue heading (13 / 21 / 26), after a bold sub-heading (16), numbered item to numbered item (16), into and out of a list (16-30), under a tab line (16-17).

## THE MENU UPLOAD RULE (5 Oct 2026, chat 13 - your words: "I don't want to do it every time I add a page ... I could update each individual page from time to time, not after every single new page gets made"; "uploading in batches when it suits you gets most of the benefit with no rebuild - yes, I'll do this").
The menu stays written inside every page (NO shared menu file). With each new page send the new page's zip; make the zip of every other live page (the whole current menu) only when the user asks for it, or offer it once at a handover - do not ask the user to upload it after every page and do not raise it again.
A live page with an older menu is not a fault: the live check of the other pages runs only after the user says a menu batch is up.

## THE TEMPLATE'S TEXT SPACES - THE FIGURES OF 6 OCT 2026 (chat 15, the user's list; they complete THE 4.1 TEMPLATE; letters to letters, every document)
Dash item to dash item 20 (was 21). Lines inside one quotation 20 (was 16). After a blue heading 20. Between lines of text: 37.2px line to line, phones 36 - UNCHANGED (6 Oct: 38 chosen by Claude under "you choose", then withdrawn the same day on the user's comment: a visible cost outweighs a tidy number). After a bold sub-heading 20. Numbered item to numbered item 20.
Into and out of a list 25. Under a line with a tab 20. Unchanged: paragraph to paragraph 40 line to line; 40 above bold text; 30 above a numbered bold line; text to a quotation 40; quotation to paragraph 40; a tab line under a paragraph 40; two separate quotations 40; the section line 36 / 28.
Values: site/pages/curriculum_rules.py (DASH_SPACE ... TAB_UNDER_SPACE). NOT YET WIRED except DASH_SPACE; 4.1 itself is live with the older figures.
Paragraph to paragraph: 25px of space (6 Oct 2026, chat 15, the user: "25"; chosen from a live comparison of 17 / 25 / 30 / 35) - SUPERSEDES "40 line to line" (17px of space). All spaces are stated in ONE measure, letters to letters.
A SHORT ONE-LINE NUMBERED LIST keeps 16px between its items (6 Oct 2026, chat 15 - the user on the live "Responsibilities to the ..." list: "i prefer this spacing"; "only to short one-line lists like this one"); other numbered lists 20. Short = every item 60 letters or fewer (SHORT_ITEM_CHARS).
AFTER A BLUE HEADING: 13px (6 Oct 2026, chat 15 - the user: "I prefer the original here also"; "yes" to 13 on every document) - SUPERSEDES 20 of the same morning.


## THE LIST RULE (6 Oct 2026, chat 18 - your words: "all lists have a space of 30 above and below. the list sets the space, not what comes after it")
Every list - a dash list, a numbered list or a run of tab lines - stands 30 of space from the text above it and 30 from the text below it, letters to
letters, on every document. The list sets both, whatever stands on the other side: a numbered bold line after a list no longer brings its own 30, and a
paragraph after one no longer brings 25. Inside the run the members keep their own figure (dash 20, numbered 20, tab lines 20, a short one-line numbered
list 16). SUPERSEDES LIST_EDGE_SPACE 25 and TAB_LINE_SPACE 40 at a list's edge.
Code: site/pages/source_steps_page.py TEMPLATE_SPACES['LIST_SPACE'] = 30; record: qa/settled_record.json figures.
Checked by EV1 (qa/even_check.py), in the gate.

## A RUN OF LIKE LINES IS EVEN (6 Oct 2026, chat 18 - your words: "this is a mistake and needs to be caught in future")
Lines that read as one list are spaced as one list, whatever the source has inside them: where Word's tab runs out on the last lines of a block, those
lines keep the run's figure instead of falling through to the paragraph figure. A run is a set of blocks one after another with the same kind, the same
left edge and the same size, each on one line, with no heading, photo, beige line or table between them.
Code: site/pages/source_steps_page.py (the run carries its figure to its end). Checked by EV1 (qa/even_check.py), in the gate; a page may name its own
runs in its settings as EV1_SKIP, with your words beside them.

## THE WORD GAPS INSIDE A RUN (6 Oct 2026, chat 18 - your words: "a few of the lines in this list have irregular spacing between the words")
Inside a run, either every line opens a column - a gap wider than two ordinary spaces - at the same x, or no line in the run has one; and no line carries
a double space between words. Where the source gives a tab to some lines of a run and not to others, the run is given ONE column and every description
starts at the same place; on phones the column collapses and the lines run on with a single space.
Checked by WS1 (qa/word_gap_check.py), in the gate, on every document.

## THE PHONE AND A WIDE BLOCK (6 Oct 2026, chat 18)
A table wider than the phone's column stacks at 640px and under: each row becomes a block, each cell under its own label from the header row. A picture
that carries small print (a graphic, a chart) takes the full column on a phone instead of the size the PDF gives it on the desktop.
Precedent: site/pages/p41_settings.py (table.mm-stack, div.mm-pdf.mm-phone-wide).
