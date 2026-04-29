#!/usr/bin/env python3
"""
Convert SVG files to PNG using available methods.
Run: python3 svg_to_png.py
"""

import os
import sys
import subprocess

# SVG files to convert
svg_files = [
    'before-after-comparison.svg',
    'before-only.svg',
    'after-only.svg'
]

def try_cairosvg(svg_path, png_path):
    """Try using cairosvg library"""
    try:
        import cairosvg
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"cairosvg error: {e}")
        return False

def try_pillow(svg_path, png_path):
    """Try using Pillow with svg backend"""
    try:
        from PIL import Image
        # Pillow doesn't natively support SVG
        # Would need additional libraries
        return False
    except ImportError:
        return False

def try_inkscape(svg_path, png_path):
    """Try using inkscape command line"""
    try:
        result = subprocess.run(
            ['inkscape', '--export-type=png', f'--export-filename={png_path}', svg_path],
            capture_output=True,
            timeout=30
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

def try_imagemagick(svg_path, png_path):
    """Try using ImageMagick convert"""
    try:
        result = subprocess.run(
            ['convert', svg_path, png_path],
            capture_output=True,
            timeout=30
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

def try_rsvg(svg_path, png_path):
    """Try using rsvg-convert"""
    try:
        result = subprocess.run(
            ['rsvg-convert', '-o', png_path, svg_path],
            capture_output=True,
            timeout=30
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False

print("Converting SVG files to PNG...")
print("=" * 50)

for svg_file in svg_files:
    if not os.path.exists(svg_file):
        print(f"Skipping {svg_file} (not found)")
        continue
    
    png_file = svg_file.replace('.svg', '.png')
    
    print(f"\nConverting {svg_file} -> {png_file}")
    
    # Try methods in order of preference
    methods = [
        ('cairosvg', try_cairosvg),
        ('rsvg-convert', try_rsvg),
        ('ImageMagick', try_imagemagick),
        ('Inkscape', try_inkscape),
    ]
    
    success = False
    for method_name, method_func in methods:
        print(f"  Trying {method_name}...", end=' ')
        if method_func(svg_file, png_file):
            print("✓ Success!")
            success = True
            break
        else:
            print("✗ Failed")
    
    if not success:
        print(f"  ⚠ No conversion method found for {svg_file}")
        print(f"  Manual option: Open {svg_file} in Chrome and screenshot")

print("\n" + "=" * 50)
print("Conversion complete!")
print("\nIf no PNGs were generated, you can:")
print("1. Open SVG files in Chrome and screenshot")
print("2. Use online converter: https://cloudconvert.com/svg-to-png")
print("3. Install ImageMagick: sudo apt-get install imagemagick")
