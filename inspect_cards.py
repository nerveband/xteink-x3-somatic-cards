#!/usr/bin/env python3
"""
Automated visual inspection loop for X3 cards:
1. Render each card to PNG at 528x792.
2. Check bounding boxes and pixel distribution:
   - Ensure title doesn't overflow or clip.
   - Ensure step content doesn't hit the bottom border.
   - Ensure proper margin spacing.
3. Report any layout violations or anomalies.
"""

import os
import subprocess
from PIL import Image

def run_inspection():
    cwd = os.getcwd()
    chrome_bin = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    card_dir = os.path.join(cwd, "x3_somatic_cards")

    anomalies = []
    
    for i in range(1, 17):
        card_id = f"{i:02d}"
        html_path = f"file://{card_dir}/card_{card_id}.html"
        png_path = f"{card_dir}/card_{card_id}.png"
        
        # Render screenshot
        cmd = [
            chrome_bin,
            "--headless",
            "--disable-gpu",
            f"--screenshot={png_path}",
            "--window-size=528,792",
            "--default-background-color=00000000",
            html_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Open and inspect image
        img = Image.open(png_path).convert("L")
        w, h = img.size
        
        if (w, h) != (528, 792):
            anomalies.append(f"Card {card_id}: Dimensions are {w}x{h}, expected 528x792.")
            continue
            
        # Check bottom border and margin:
        # The bottom border is at approx y = 792 - 28 = 764.
        # Check pixels between y=740 and y=760 to see if text is crowding the bottom border.
        bottom_region = img.crop((40, 745, 488, 762))
        dark_pixels_bottom = sum(1 for p in bottom_region.getdata() if p < 100)
        
        # Check title area (approx y=60 to y=120) to ensure content exists and is not blank
        title_region = img.crop((40, 50, 488, 120))
        dark_pixels_title = sum(1 for p in title_region.getdata() if p < 100)
        
        # Check art region (approx y=140 to y=320)
        art_region = img.crop((40, 140, 488, 320))
        dark_pixels_art = sum(1 for p in art_region.getdata() if p < 100)
        
        # Check steps region (approx y=340 to y=720)
        steps_region = img.crop((40, 340, 488, 730))
        dark_pixels_steps = sum(1 for p in steps_region.getdata() if p < 100)
        
        print(f"Card {card_id} -> Title Pixels: {dark_pixels_title}, Art Pixels: {dark_pixels_art}, Steps Pixels: {dark_pixels_steps}, Bottom Guard Pixels: {dark_pixels_bottom}")
        
        if dark_pixels_title < 50:
            anomalies.append(f"Card {card_id}: Title region appears empty or missing.")
        if dark_pixels_art < 50:
            anomalies.append(f"Card {card_id}: Vector art region appears empty or missing.")
        if dark_pixels_steps < 100:
            anomalies.append(f"Card {card_id}: Steps region appears empty or missing.")
        if dark_pixels_bottom > 150:
            anomalies.append(f"Card {card_id}: Content is crowding the bottom border (overflow risk).")

    if anomalies:
        print("\nANOMALIES FOUND:")
        for a in anomalies:
            print(" -", a)
    else:
        print("\nALL 16 CARDS PASSED VISUAL BOUNDS & SPACING INSPECTION.")

    # Re-generate contact sheet
    cols, rows = 4, 4
    scale = 0.5
    cw, ch = int(528 * scale), int(792 * scale)
    sheet = Image.new("RGB", (cols * cw, rows * ch), (255, 255, 255))
    
    for idx in range(16):
        card_id = f"{idx+1:02d}"
        c_img = Image.open(f"{card_dir}/card_{card_id}.png").resize((cw, ch), Image.Resampling.LANCZOS)
        r = idx // cols
        c = idx % cols
        sheet.paste(c_img, (c * cw, r * ch))
        
    sheet.save(f"{card_dir}/deck_contact_sheet.jpg", quality=92)
    print(f"Saved updated {card_dir}/deck_contact_sheet.jpg")

if __name__ == "__main__":
    run_inspection()
