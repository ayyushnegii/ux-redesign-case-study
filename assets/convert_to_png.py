#!/usr/bin/env python3
import cairosvg
import os

files = ['before-after-comparison.svg', 'before-only.svg', 'after-only.svg']
for svg in files:
    if os.path.exists(svg):
        png = svg.replace('.svg', '.png')
        print(f"Converting {svg} -> {png}...")
        cairosvg.svg2png(url=svg, write_to=png, scale=2)
        size = os.path.getsize(png) / 1024
        print(f"  Created {png} ({size:.1f} KB)")

print("\nDone! PNG files ready for LinkedIn.")
