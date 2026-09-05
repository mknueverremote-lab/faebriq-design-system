# FÆBRIQ Product Image Spec

Standards for every product image on faebriq.com. Applies to Printify-generated
mockups and custom-rendered imagery alike.

## Aspect ratio and resolution

**All product images: 1:1 at 2048 × 2048 px.**

Square survives every layout — grid cards, mobile PDP, desktop PDP — without
forcing a crop decision. 4:5 looks better on a phone PDP alone and breaks
everywhere else.

As of this writing the catalogue carries three ratios, which is the direct cause
of the crop bug where "DEPLOYING" is cut off on the crewneck PDP but renders
correctly in the grid:

| Ratio | Pixels | Products |
| --- | --- | --- |
| 1:1 ✅ | 2048 × 2048 | 404 Tee, Code It. Serve It. Tee, Deploying Identity Tee, 404 Cotton Tote, Circuit Cap |
| 4:5 ❌ | 1664 × 2080 | Crewneck, Hoodie, all four statement stickers |
| 4:5 ❌ | 2048 × 2560 | Sticker Sheet (two of four images) |

The 4:5 assets need re-rendering square. Padding them is not sufficient — the
subject must be recomposed for the square frame.

Minimum 2048 px on the long edge; below that Shopify disables zoom on the PDP.
The 404 Sticker images are currently 1200 × 1200 and need re-rendering.

## Gallery structure

Four images, in this order:

1. **Hero — the product in real context.** What the customer actually receives,
   in use. A sticker on a laptop lid, a cap on a head, a tee worn.
2. **Clean product shot.** Isolated, front-on, neutral ground.
3. **Scale or on-model reference.**
4. **Macro detail** of the print and the pride-circuit bar.

Never lead with a mood shot. Art-directed imagery — type floating on a slate
slab — belongs in slot 2 or later. A customer buying a 3 × 3 inch vinyl sticker
must not see a photograph of a rock first.

Four images is the cap. Twenty-one near-identical sticker photos serve nobody.

## Backgrounds

- **Hero and clean product shots: white or light neutral.** Black garments
  disappear against dark grounds.
- **Lifestyle and detail shots: dark.** This is where the dark-tech mood belongs.

The pride-circuit bar beneath each grid card already carries the brand — the
product photography does not need to.

## Print realism

Prints must read as printed *into* the fabric, not pasted on top:

- Artwork follows the weave, folds, and drape of the garment
- Fabric texture shows through the ink
- Edges soften slightly at the thread level — no vector-crisp boundaries

Displacement-mapped mockups achieve this. Flat compositing does not, and it is
the single clearest tell of an amateur POD storefront.

## Alt text

Every image carries descriptive alt text. Pattern:

```
FÆBRIQ '<Statement>' <Product> — <view>, <what is visible>.
```

Example:

```
FÆBRIQ 'Deploying Identity v2.0' Tee — black heavy cotton unisex t-shirt with
the white chest print and six-stripe pride-circuit bar.
```

Never leave alt text empty. Printify-imported images arrive with none and must
be written by hand.

## The pride-circuit bar

Six equal blocks, full width, in this order:

`#E8271C` `#F47B20` `#F9D01F` `#009A44` `#0057A8` `#742B8C`

**One master asset, used everywhere — never regenerated per product.** Source
files live in `assets/`:

- `pride-circuit-bar.svg` — vector master
- `pride-circuit-bar-4500x150.png` — print / DTG
- `pride-circuit-bar-3000x100.png` — large web
- `pride-circuit-bar-1200x40.png` — standard web

At least three incompatible variants were previously in circulation: solid
contiguous blocks, blocks separated by white gaps, and a thin version with node
dots. This is the most repeated element in the brand system; it must be
byte-identical in every appearance.

On tees the bar is full-width and pinned to the bottom edge of the design. On
the cap it sits centred directly beneath the wordmark.
