# Xteink X3 Somatic Reset Card Deck

> 16 somatic nervous system reset exercise cards specifically engineered for the **Xteink X3** pocket E-Ink display (**3.7-inch, 528 &times; 792 pixels, uncompressed 24-bit BMP**).

<p align="center">
  <img src="preview/deck_contact_sheet.jpg" alt="X3 Somatic Card Deck Overview" width="800" />
</p>

## Overview

Living in chronic tension trains the nervous system to treat downtime as alert time. Somatic exercises provide physical, bottom-up physiological signals (vagal nerve stimulation, neuromuscular release, acoustic resonance, and bilateral grounding) that shift the nervous system out of fight-or-flight.

This deck translates 16 evidence-based somatic exercises into dedicated, high-contrast digital cards formatted for pocket E-paper devices running **CrossPoint Reader** or standard X3 image viewers.

---

## Device & Display Specifications

* **Target Device:** Xteink X3 (ESP32-based 3.7-inch ultra-compact E-Reader)
* **Firmware:** CrossPoint Reader / Native X3 OS
* **Display Resolution:** Exact **528 &times; 792 pixels** (1:1 native pixel mapping, zero scaling artifacts)
* **File Format:** **Uncompressed 24-bit BMP** (RGB888, 1,254,582 bytes per file)
* **Typography:**
  * **Titles:** High-contrast Slab Serif (`Roboto Slab 900`), single-line locked
  * **Step Guidance:** 31px medium sans-serif (`font-weight: 450`) with **bold + underlined action cues**
  * **Duration:** 24px prominent pill with clock icon
  * **Widow / Orphan Protection:** Non-breaking space locks on compound numbers and units (`10 seconds`, `4 times`, `8 counts`)

---

## Complete Card Index

| # | Exercise Name | Category | Duration | BMP File |
|---|---|---|---|---|
| **01** | **Physiological Sigh** | `BREATHING RESET` | `1 - 2 MINUTES` | `01_physiological_sigh.bmp` |
| **02** | **Extended Exhale** | `VAGAL PACE` | `2 - 5 MINUTES` | `02_extended_exhale.bmp` |
| **03** | **Morning Body Scan** | `SOMATIC ATTENTION` | `3 - 5 MINUTES` | `03_morning_body_scan.bmp` |
| **04** | **Situational Humming** | `ACOUSTIC VAGUS` | `1 - 2 MINUTES` | `04_situational_humming.bmp` |
| **05** | **Cold Water Reset** | `COLD RESET` | `1 MINUTE` | `05_cold_water_reset.bmp` |
| **06** | **Muscle Relaxation** | `NEUROMUSCULAR` | `5 - 10 MINUTES` | `06_muscle_relaxation.bmp` |
| **07** | **Butterfly Hug** | `BILATERAL STIM` | `2 - 3 MINUTES` | `07_butterfly_hug.bmp` |
| **08** | **Orienting Exercise** | `SPATIAL SAFETY` | `1 - 2 MINUTES` | `08_orienting_exercise.bmp` |
| **09** | **Feet On Ground** | `PHYSICAL ANCHOR` | `1 - 2 MINUTES` | `09_feet_on_ground.bmp` |
| **10** | **Wall Press Reset** | `SOMATIC FORCE` | `2 - 3 MINUTES` | `10_wall_press_reset.bmp` |
| **11** | **Ice Vagus Shock** | `TEMPERATURE SHOCK` | `1 - 2 MINUTES` | `11_ice_vagus_shock.bmp` |
| **12** | **Ladder Breathing** | `STEPPED CADENCE` | `3 - 5 MINUTES` | `12_ladder_breathing.bmp` |
| **13** | **Diaphragm Exhale** | `DIAPHRAGM RELEASE` | `1 - 2 MINUTES` | `13_diaphragm_exhale.bmp` |
| **14** | **Voo Sound Exhale** | `VISCERAL RESONANCE` | `2 - 3 MINUTES` | `14_voo_sound_exhale.bmp` |
| **15** | **Neurogenic Shakeout** | `DISCHARGE ENERGY` | `2 - 3 MINUTES` | `15_neurogenic_shakeout.bmp` |
| **16** | **Jaw & Skull Release** | `CRANIAL RELEASE` | `2 MINUTES` | `16_jaw_skull_release.bmp` |

---

## How to Install on Xteink X3 (CrossPoint Reader)

### 1. Download the BMP Deck
* Download the pre-built release package [`x3_somatic_cards_v1.0.0.zip`](https://github.com/nerveband/xteink-x3-somatic-cards/releases/latest) from the [Releases page](https://github.com/nerveband/xteink-x3-somatic-cards/releases).
* Or grab the files directly from the [`bmp/`](bmp/) directory in this repository.

### 2. Copy Files to MicroSD Card
1. Insert your X3's microSD card into your computer (ensure it is formatted as **FAT32**).
2. Create an `images` or `somatic` folder on the microSD card (e.g. `/images/somatic/` or `/somatic/`).
3. Copy all 16 `.bmp` files into that folder:
   ```
   SD_CARD/
   └── somatic/
       ├── 01_physiological_sigh.bmp
       ├── 02_extended_exhale.bmp
       ├── 03_morning_body_scan.bmp
       ├── ...
       └── 16_jaw_skull_release.bmp
   ```
4. Eject the microSD card safely and insert it back into your Xteink X3.

### 3. Navigation on Device
* Power on the X3 and open CrossPoint Reader.
* Navigate to the **Images / Files** menu.
* Open the `somatic` folder.
* Use the physical side buttons to advance through the cards step by step.

---

## Visual Card Gallery


### 01. Physiological Sigh
* **Category:** `BREATHING RESET`
* **Duration:** `1 - 2 MINUTES`
* **File:** [`bmp/01_physiological_sigh.bmp`](bmp/01_physiological_sigh.bmp)

<p align="center">
  <img src="preview/01_physiological_sigh.jpg" alt="Physiological Sigh" width="400" />
</p>

---


### 02. Extended Exhale
* **Category:** `VAGAL PACE`
* **Duration:** `2 - 5 MINUTES`
* **File:** [`bmp/02_extended_exhale.bmp`](bmp/02_extended_exhale.bmp)

<p align="center">
  <img src="preview/02_extended_exhale.jpg" alt="Extended Exhale" width="400" />
</p>

---


### 03. Morning Body Scan
* **Category:** `SOMATIC ATTENTION`
* **Duration:** `3 - 5 MINUTES`
* **File:** [`bmp/03_morning_body_scan.bmp`](bmp/03_morning_body_scan.bmp)

<p align="center">
  <img src="preview/03_morning_body_scan.jpg" alt="Morning Body Scan" width="400" />
</p>

---


### 04. Situational Humming
* **Category:** `ACOUSTIC VAGUS`
* **Duration:** `1 - 2 MINUTES`
* **File:** [`bmp/04_situational_humming.bmp`](bmp/04_situational_humming.bmp)

<p align="center">
  <img src="preview/04_situational_humming.jpg" alt="Situational Humming" width="400" />
</p>

---


### 05. Cold Water Reset
* **Category:** `COLD RESET`
* **Duration:** `1 MINUTE`
* **File:** [`bmp/05_cold_water_reset.bmp`](bmp/05_cold_water_reset.bmp)

<p align="center">
  <img src="preview/05_cold_water_reset.jpg" alt="Cold Water Reset" width="400" />
</p>

---


### 06. Muscle Relaxation
* **Category:** `NEUROMUSCULAR`
* **Duration:** `5 - 10 MINUTES`
* **File:** [`bmp/06_muscle_relaxation.bmp`](bmp/06_muscle_relaxation.bmp)

<p align="center">
  <img src="preview/06_muscle_relaxation.jpg" alt="Muscle Relaxation" width="400" />
</p>

---


### 07. Butterfly Hug
* **Category:** `BILATERAL STIM`
* **Duration:** `2 - 3 MINUTES`
* **File:** [`bmp/07_butterfly_hug.bmp`](bmp/07_butterfly_hug.bmp)

<p align="center">
  <img src="preview/07_butterfly_hug.jpg" alt="Butterfly Hug" width="400" />
</p>

---


### 08. Orienting Exercise
* **Category:** `SPATIAL SAFETY`
* **Duration:** `1 - 2 MINUTES`
* **File:** [`bmp/08_orienting_exercise.bmp`](bmp/08_orienting_exercise.bmp)

<p align="center">
  <img src="preview/08_orienting_exercise.jpg" alt="Orienting Exercise" width="400" />
</p>

---


### 09. Feet On Ground
* **Category:** `PHYSICAL ANCHOR`
* **Duration:** `1 - 2 MINUTES`
* **File:** [`bmp/09_feet_on_ground.bmp`](bmp/09_feet_on_ground.bmp)

<p align="center">
  <img src="preview/09_feet_on_ground.jpg" alt="Feet On Ground" width="400" />
</p>

---


### 10. Wall Press Reset
* **Category:** `SOMATIC FORCE`
* **Duration:** `2 - 3 MINUTES`
* **File:** [`bmp/10_wall_press_reset.bmp`](bmp/10_wall_press_reset.bmp)

<p align="center">
  <img src="preview/10_wall_press_reset.jpg" alt="Wall Press Reset" width="400" />
</p>

---


### 11. Ice Vagus Shock
* **Category:** `TEMPERATURE SHOCK`
* **Duration:** `1 - 2 MINUTES`
* **File:** [`bmp/11_ice_vagus_shock.bmp`](bmp/11_ice_vagus_shock.bmp)

<p align="center">
  <img src="preview/11_ice_vagus_shock.jpg" alt="Ice Vagus Shock" width="400" />
</p>

---


### 12. Ladder Breathing
* **Category:** `STEPPED CADENCE`
* **Duration:** `3 - 5 MINUTES`
* **File:** [`bmp/12_ladder_breathing.bmp`](bmp/12_ladder_breathing.bmp)

<p align="center">
  <img src="preview/12_ladder_breathing.jpg" alt="Ladder Breathing" width="400" />
</p>

---


### 13. Diaphragm Exhale
* **Category:** `DIAPHRAGM RELEASE`
* **Duration:** `1 - 2 MINUTES`
* **File:** [`bmp/13_diaphragm_exhale.bmp`](bmp/13_diaphragm_exhale.bmp)

<p align="center">
  <img src="preview/13_diaphragm_exhale.jpg" alt="Diaphragm Exhale" width="400" />
</p>

---


### 14. Voo Sound Exhale
* **Category:** `VISCERAL RESONANCE`
* **Duration:** `2 - 3 MINUTES`
* **File:** [`bmp/14_voo_sound_exhale.bmp`](bmp/14_voo_sound_exhale.bmp)

<p align="center">
  <img src="preview/14_voo_sound_exhale.jpg" alt="Voo Sound Exhale" width="400" />
</p>

---


### 15. Neurogenic Shakeout
* **Category:** `DISCHARGE ENERGY`
* **Duration:** `2 - 3 MINUTES`
* **File:** [`bmp/15_neurogenic_shakeout.bmp`](bmp/15_neurogenic_shakeout.bmp)

<p align="center">
  <img src="preview/15_neurogenic_shakeout.jpg" alt="Neurogenic Shakeout" width="400" />
</p>

---


### 16. Jaw & Skull Release
* **Category:** `CRANIAL RELEASE`
* **Duration:** `2 MINUTES`
* **File:** [`bmp/16_jaw_skull_release.bmp`](bmp/16_jaw_skull_release.bmp)

<p align="center">
  <img src="preview/16_jaw_skull_release.jpg" alt="Jaw & Skull Release" width="400" />
</p>

---


---

## Building & Customizing Cards

The repository includes a complete Python + Headless Chrome toolchain to render HTML templates to PNG, JPG previews, and uncompressed 24-bit BMP binaries.

### Prerequisites
* Python 3.9+
* Pillow (`pip install pillow`)
* Google Chrome (used for headless vector/font rasterization)

### Build Commands

```bash
# 1. Build standalone HTML templates in src/
python3 build_cards.py

# 2. Render 24-bit uncompressed BMPs and JPG previews
python3 export_bmp.py

# 3. Run automated visual layout inspection
python3 inspect_cards.py
```

### Local Browser Previewer
To inspect cards in an interactive browser viewer:
```bash
python3 -m http.server 8899 --directory .
# Open http://localhost:8899/viewer/index.html in your browser
```

---

## License

MIT License. Free to share, modify, and distribute.
