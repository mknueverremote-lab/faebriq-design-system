# Printify Mockup Workflow

How to produce FÆBRIQ product imagery. This is the *only* approved method for
product photography. See `image-spec.md` for the standards this workflow exists
to meet.

## Why this workflow and not image generation

Product images must show exactly what the customer receives. Generated imagery
cannot do that — it invents a garment that does not exist, drifts on typography,
and re-renders the pride bar as a gradient or an uneven line instead of using
the master asset.

Printify composites the **real design file** onto **real garment photography**,
with correct fabric behaviour, and outputs 2048 × 2048 natively.

The evidence is already in the catalogue. Every product sourced from Printify is
1:1 at 2048 and reads as a real garment. Every product sourced from generated
imagery is 4:5 and reads as artwork pasted onto a photo. The aspect-ratio problem
and the fabricated-imagery problem are the same problem, and this workflow fixes
both at once.

## Order of operations

**Artwork first, then mockups.** Printify bakes the design file into the mockup,
so any error in the artwork — wrong pride bar, wrong type sizing — is baked into
every image that follows. Fixing artwork after generating mockups means
generating them twice.

---

## Step 1 — Rebuild the design files

Each design is rebuilt once and reused across every product carrying it.

| Design | Products |
| --- | --- |
| Deploying Identity v2.0 | Crewneck, Tee, Sticker |
| Off The Clock. Still Iconic. | Hoodie |
| Code It. Serve It. | Tee, Sticker |
| It's Not A Bug. It's Me. | Sticker |
| Please Hold, I'm Rebranding My Identity | Sticker |
| Error 404: Straight Not Found | Tee, Tote, Sticker |
| Sticker sheet | Sticker Sheet (all five statements) |

Requirements for every file:

- **Pride bar: place `assets/pride-circuit-bar.svg` directly.** Do not redraw it,
  do not export a new one from a design tool, do not let a generator produce one.
  Six equal blocks, no gaps, no node dots, no gradient:
  `#E8271C` `#F47B20` `#F9D01F` `#009A44` `#0057A8` `#742B8C`
- **Typeface: Instrument Serif**, all text.
- **Transparent background**, PNG, 300 DPI at print size (roughly 4500 px wide
  for a tee front).
- **Type sizing follows the existing product**, which is not uniform across the
  line and is not meant to be:
  - Crewneck — `DEPLOYING` large, `IDENTITY V2.0` smaller beneath
  - Hoodie — `OFF THE CLOCK.` large, `STILL ICONIC.` smaller beneath
  - 404 Tee — massive `404`, small italic `Straight Not Found` beneath
  - Stickers — single type size throughout

There is no brand rule requiring uniform type size. Do not introduce one.

**Layout:** on garments the bar is full-width, pinned to the bottom edge of the
design. On the cap it is centred directly beneath the wordmark.

## Step 2 — Generate mockups in Printify

For each product, in the Printify product editor:

1. Replace the existing design file with the rebuilt one from Step 1.
2. Confirm placement and scale on the blank.
3. In the mockup selection, choose **four** views matching the gallery structure
   in `image-spec.md`: product in real context → clean product shot → on-model or
   scale reference → macro detail.
4. Save.

Printify renders at 2048 × 2048. Do not crop, pad, or post-process the output.

**Do not change the cap's fulfilment.** It stays OTTO Cap 18-253, Printify
Choice, DTF — matching the approved physical sample. Embroidery is not a
substitute.

## Step 3 — Publish to Shopify

Publish from Printify. Printify owns the sync, so the publish action is what
pushes new media to Shopify.

## Step 4 — Repair what the sync overwrites

**A Printify publish replaces product media wholesale.** It will discard the alt
text and gallery order currently set on those products. Both must be restored
after every sync — this is expected, not a failure.

After publishing, for each synced product:

1. **Reorder the gallery** so the real-context shot is first. Never lead with a
   mood shot.
2. **Rewrite alt text** on every image, following the pattern in
   `image-spec.md`:
   `FÆBRIQ '<Statement>' <Product> — <view>, <what is visible>.`
3. **Confirm the title and tags survived.** Printify sometimes restores its own
   product names and operational tags (`Neck Labels`, `Personalization Picks`,
   `2 day delivery`, `Embroidery`). The catalogue uses FÆBRIQ titles and a fixed
   15-tag vocabulary; restore them if they were clobbered.

## Products awaiting this workflow

Seven products still carry generated 4:5 imagery:

| Product | ID |
| --- | --- |
| Deploying Identity v2.0 Crewneck | 7778652127299 |
| Off The Clock. Still Iconic. Hoodie | 7778654126147 |
| It's Not A Bug. It's Me. Sticker | 7785339322435 |
| Code It. Serve It. Sticker | 7785339519043 |
| Please Hold Sticker | 7785339617347 |
| Deploying Identity v2.0 Sticker | 7785339682883 |
| Sticker Sheet | 7785341190211 |

One further product is Printify-sourced but under-resolution — 404 Sticker
(`7785339584579`), currently 1200 × 1200, below Shopify's 2048 zoom threshold.
Re-export its mockups at 2048.

Five products already meet the standard and need no image work: the three tees,
the tote, and the cap.
