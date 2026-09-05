#!/usr/bin/env python3
"""Build FÆBRIQ print-ready design files deterministically.

Text is set in Instrument Serif and auto-fitted to the print width in-browser,
so every design fills its canvas properly. The pride bar is emitted as six
solid rects with exact integer edges — identical geometry to
assets/pride-circuit-bar.svg — never redrawn, gradiented, or generated.
"""

import json
import os
import subprocess

OUT = os.path.dirname(os.path.abspath(__file__)) + "/designs"
os.makedirs(OUT, exist_ok=True)

CANVAS = 4500          # print width in px (300 DPI, 15in)
MARGIN = 300           # side margin
CONTENT = CANVAS - 2 * MARGIN
BAR_H = 110            # pride bar height
GAP_BAR = 230          # gap between text block and bar

COLORS = ["#E8271C", "#F47B20", "#F9D01F", "#009A44", "#0057A8", "#742B8C"]

# name -> (lines, fit_ratio)
#   line = (text, relative_size, italic)
#   fit_ratio = fraction of CONTENT the widest line should span
DESIGNS = {
    "deploying-identity-v2": ([("DEPLOYING", 1.0, False),
                               ("IDENTITY V2.0", 0.34, False)], 1.0),
    "off-the-clock":         ([("OFF THE CLOCK.", 1.0, False),
                               ("STILL ICONIC.", 0.44, False)], 1.0),
    "code-it-serve-it":      ([("CODE IT.", 1.0, False),
                               ("SERVE IT.", 1.0, False)], 0.72),
    "not-a-bug":             ([("IT'S NOT A BUG.", 1.0, False),
                               ("IT'S ME.", 1.0, False)], 1.0),
    "please-hold":           ([("PLEASE HOLD,", 1.0, False),
                               ("I'M REBRANDING", 1.0, False),
                               ("MY IDENTITY.", 1.0, False)], 1.0),
    "error-404":             ([("404", 1.0, False),
                               ("Straight Not Found", 0.15, True)], 0.80),
}

# Statements on the sticker sheet, top to bottom.
SHEET = ["DEPLOYING IDENTITY V2.0", "CODE IT. SERVE IT.",
         "PLEASE HOLD, I'M REBRANDING MY IDENTITY.",
         "IT'S NOT A BUG. IT'S ME.", "404 STRAIGHT NOT FOUND"]


def bar_svg(width, height):
    rects = []
    for i, c in enumerate(COLORS):
        x0 = round(width * i / 6)
        x1 = round(width * (i + 1) / 6)
        rects.append(
            f'<rect x="{x0}" y="0" width="{x1 - x0}" height="{height}" fill="{c}"/>'
        )
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
            f'height="{height}" viewBox="0 0 {width} {height}">'
            + "".join(rects) + "</svg>")


def page(lines, fit_ratio, canvas=CANVAS, content=CONTENT, bar_h=BAR_H):
    line_html = "".join(
        f'<div class="line" data-rel="{rel}" '
        f'style="font-size:{400 * rel}px;{"font-style:italic;" if ital else ""}">'
        f"{txt}</div>"
        for txt, rel, ital in lines
    )
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{background:transparent}}
  #print{{width:{canvas}px;padding:0 {MARGIN}px;display:inline-block;background:transparent}}
  #text{{display:flex;flex-direction:column;align-items:center}}
  .line{{font-family:"Instrument Serif",Georgia,serif;font-weight:400;
        color:#FFFFFF;line-height:0.94;white-space:nowrap;text-align:center}}
  #bar{{margin-top:{GAP_BAR}px;width:{content}px;height:{bar_h}px;display:block}}
</style></head><body>
<div id="print"><div id="text">{line_html}</div>{bar_svg(content, bar_h)}</div>
<script>
window.__ready = (async () => {{
  await document.fonts.load('400 400px "Instrument Serif"');
  await document.fonts.load('italic 400 400px "Instrument Serif"');
  await document.fonts.ready;
  const target = {content} * {fit_ratio};
  const lines = [...document.querySelectorAll('.line')];
  // Scale the whole block so the widest line lands exactly on target width.
  let widest = 0;
  for (const l of lines) widest = Math.max(widest, l.getBoundingClientRect().width);
  const k = target / widest;
  for (const l of lines) {{
    l.style.fontSize = (parseFloat(getComputedStyle(l).fontSize) * k) + 'px';
  }}
  return true;
}})();
</script></body></html>"""


def render(name, html):
    html_path = f"{OUT}/{name}.html"
    with open(html_path, "w") as f:
        f.write(html)
    js = f"""
const {{ chromium }} = require('playwright');
(async () => {{
  const b = await chromium.launch({{ executablePath: '/opt/pw-browsers/chromium' }});
  const p = await b.newPage({{ viewport: {{ width: {CANVAS}, height: 2000 }},
                              deviceScaleFactor: 1 }});
  await p.goto('file://{html_path}');
  await p.evaluate(() => window.__ready);
  await p.waitForTimeout(400);
  const el = await p.$('#print');
  await el.screenshot({{ path: '{OUT}/{name}.png', omitBackground: true }});
  await b.close();
}})();
"""
    subprocess.run(["node", "-e", js], check=True,
                   env={**os.environ, "NODE_PATH": "/opt/node22/lib/node_modules"})


def sheet_page():
    """Five statements as individual stickers on one sheet, each with its own bar."""
    cell_w = 3200
    cell_bar_h = 70
    cells = "".join(
        f'<div class="cell"><div class="ctext">{s}</div>'
        f'{bar_svg(cell_w, cell_bar_h)}</div>'
        for s in SHEET
    )
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  html,body{{background:transparent}}
  #print{{width:{CANVAS}px;padding:{MARGIN}px;display:flex;flex-direction:column;
         align-items:center;gap:290px;background:transparent}}
  .cell{{display:flex;flex-direction:column;align-items:center;width:{cell_w}px}}
  .ctext{{font-family:"Instrument Serif",Georgia,serif;font-weight:400;color:#FFFFFF;
         line-height:0.98;white-space:nowrap;text-align:center;font-size:300px;
         margin-bottom:70px}}
  .cell svg{{display:block}}
</style></head><body>
<div id="print">{cells}</div>
<script>
window.__ready = (async () => {{
  await document.fonts.load('400 300px "Instrument Serif"');
  await document.fonts.ready;
  // Fit each sticker's text to the cell width independently.
  for (const t of document.querySelectorAll('.ctext')) {{
    const w = t.getBoundingClientRect().width;
    const k = {cell_w} / w;
    t.style.fontSize = (parseFloat(getComputedStyle(t).fontSize) * k) + 'px';
  }}
  return true;
}})();
</script></body></html>"""


for name, (lines, fit) in DESIGNS.items():
    render(name, page(lines, fit))
    print("built", name)

render("sticker-sheet", sheet_page())
print("built sticker-sheet")
