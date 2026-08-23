#!/usr/bin/env python3
"""
Render all 16 cards to uncompressed 24-bit BMP files at exact 528x792 resolution.
Verify:
- Exact 528x792 dimensions.
- 24-bit RGB uncompressed BMP format (1,254,582 bytes each).
- Clean naming: card_01.bmp ... card_16.bmp.
"""

import os
import subprocess
from PIL import Image

def export_bmp():
    cwd = os.getcwd()
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    card_dir = os.path.join(cwd, "x3_somatic_cards")
    bmp_dir = os.path.join(card_dir, "x3_bmp_export")
    os.makedirs(bmp_dir, exist_ok=True)

    print("Rendering cards to 24-bit uncompressed BMP (528x792)...")

    for i in range(1, 17):
        card_id = f"{i:02d}"
        html_path = f"file://{card_dir}/card_{card_id}.html"
        png_temp = f"{bmp_dir}/temp_{card_id}.png"
        bmp_final = f"{bmp_dir}/card_{card_id}.bmp"

        # 1. Render high-precision screenshot via Headless Chrome
        cmd = [
            chrome_bin,
            "--headless",
            "--disable-gpu",
            f"--screenshot={png_temp}",
            "--window-size=528,792",
            "--default-background-color=00000000",
            html_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 2. Open with PIL, ensure exact (528, 792) in 24-bit RGB, and save as BMP
        img = Image.open(png_temp).convert("RGB")
        if img.size != (528, 792):
            img = img.resize((528, 792), Image.Resampling.LANCZOS)
        
        img.save(bmp_final, format="BMP")
        os.remove(png_temp)

        file_size = os.path.getsize(bmp_final)
        print(f"Exported card_{card_id}.bmp -> Size: {file_size:,} bytes | Dimensions: {img.size} | Mode: {img.mode}")

    print("\nAll 16 BMP files successfully generated in:", bmp_dir)

if __name__ == "__main__":
    export_bmp()
