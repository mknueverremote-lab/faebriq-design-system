#!/usr/bin/env python3
"""Render the FÆBRIQ pride-circuit bar to PNG at print and web sizes.

The bar is the most repeated element in the brand system and must be
byte-identical everywhere it appears. Regenerate from this script rather than
recreating it by hand or exporting from a design tool — block edges are placed
on exact integer pixels so no seams or sub-pixel gaps appear at any scale.

Usage:  python3 generate-pride-bar.py
Requires: Pillow
"""

from PIL import Image, ImageDraw

# Locked left-to-right order. Do not reorder or substitute.
COLORS = ["#E8271C", "#F47B20", "#F9D01F", "#009A44", "#0057A8", "#742B8C"]

# (width, height, filename)
SIZES = [
    (4500, 150, "pride-circuit-bar-4500x150.png"),  # print / DTG
    (3000, 100, "pride-circuit-bar-3000x100.png"),  # large web
    (1200, 40, "pride-circuit-bar-1200x40.png"),    # standard web
]


def render(width: int, height: int, path: str) -> None:
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    for i, color in enumerate(COLORS):
        x0 = round(width * i / len(COLORS))
        x1 = round(width * (i + 1) / len(COLORS))
        draw.rectangle([x0, 0, x1 - 1, height - 1], fill=color)
    img.save(path)
    print(f"{path}  {width}x{height}")


if __name__ == "__main__":
    for width, height, path in SIZES:
        render(width, height, path)
