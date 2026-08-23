#!/usr/bin/env python3
"""
Generate and optimize 16 somatic exercise cards for the X3 3.7-inch E-Ink display (528x792 px).
Strict rules implemented:
- Zero widows and orphans (using non-breaking spaces on trailing word pairs and text-wrap: pretty).
- Numbers and units strictly locked together (10 seconds, 4 times, 8 counts, etc.).
- Large 31px font size, 24px duration badges, 44px step badges.
- Clean 450 weight base with bold and underlined action highlights.
- Clear non-colliding vector art callout text.
- 100% zero em dashes.
"""

import os
import subprocess
from PIL import Image

CARDS = [
    {
        "id": "01",
        "category": "BREATHING RESET",
        "title": "Physiological Sigh",
        "duration": "1 - 2 MINUTES",
        "steps": [
            "<strong><u>Inhale deeply</u></strong> through nose to expand&nbsp;lungs.",
            "Take a <strong><u>second sharp sniff</u></strong> on&nbsp;top.",
            "Release with a <strong><u>long, slow sigh</u></strong> out&nbsp;mouth.",
            "Repeat for <strong><u>3&nbsp;to&nbsp;5&nbsp;breath&nbsp;cycles</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <text x="75" y="20" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1.5">1. DEEP IN</text>
            <text x="160" y="30" font-family="'Jost', sans-serif" font-size="11" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">+ SNIFF</text>
            <text x="285" y="20" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1.5">2. LONG SIGH OUT</text>
            
            <path d="M 30 95 C 65 35, 115 35, 140 70" stroke="#000" stroke-width="5.5" stroke-linecap="round"/>
            <path d="M 140 70 C 152 48, 175 48, 188 64" stroke="#000" stroke-width="5.5" stroke-linecap="round"/>
            <circle cx="188" cy="64" r="7.5" fill="#000"/>
            <path d="M 188 64 C 235 120, 305 120, 370 95" stroke="#000" stroke-width="5.5" stroke-linecap="round"/>
            
            <line x1="30" y1="112" x2="370" y2="112" stroke="#000" stroke-width="2.5" stroke-dasharray="5 5"/>
            <circle cx="30" cy="95" r="6" fill="#000"/>
            <circle cx="140" cy="70" r="6" fill="#000"/>
            <circle cx="370" cy="95" r="6" fill="#000"/>
        </svg>
        """
    },
    {
        "id": "02",
        "category": "VAGAL PACE",
        "title": "Extended Exhale",
        "duration": "2 - 5 MINUTES",
        "steps": [
            "<strong><u>Sit tall</u></strong> and relax shoulders and&nbsp;jaw.",
            "<strong><u>Inhale smoothly</u></strong> through nose for <strong><u>4&nbsp;counts</u></strong>.",
            "<strong><u>Exhale slowly</u></strong> through pursed lips for <strong><u>8&nbsp;counts</u></strong>.",
            "Maintain this <strong><u>1:2&nbsp;steady&nbsp;ratio</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="25" y="24" width="110" height="52" rx="26" stroke="#000" stroke-width="4.5" fill="none"/>
            <text x="80" y="58" font-family="'Jost', sans-serif" font-size="22" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">IN 4</text>
            
            <line x1="140" y1="50" x2="170" y2="50" stroke="#000" stroke-width="4" stroke-dasharray="3 4"/>
            <polygon points="168,42 180,50 168,58" fill="#000"/>

            <rect x="180" y="24" width="195" height="52" rx="26" fill="#000"/>
            <text x="277" y="58" font-family="'Jost', sans-serif" font-size="18" font-weight="900" fill="#FFF" text-anchor="middle" letter-spacing="1.5">OUT 8 (EXTENDED)</text>

            <line x1="25" y1="95" x2="375" y2="95" stroke="#000" stroke-width="3"/>
            <line x1="25" y1="87" x2="25" y2="103" stroke="#000" stroke-width="3"/>
            <line x1="135" y1="87" x2="135" y2="103" stroke="#000" stroke-width="3"/>
            <line x1="375" y1="87" x2="375" y2="103" stroke="#000" stroke-width="3"/>
            
            <text x="80" y="122" font-family="'Jost', sans-serif" font-size="13" font-weight="800" fill="#000" text-anchor="middle" letter-spacing="1.5">1X DURATION</text>
            <text x="277" y="122" font-family="'Jost', sans-serif" font-size="13" font-weight="800" fill="#000" text-anchor="middle" letter-spacing="1.5">2X DURATION</text>
        </svg>
        """
    },
    {
        "id": "03",
        "category": "SOMATIC ATTENTION",
        "title": "Morning Body Scan",
        "duration": "3 - 5 MINUTES",
        "steps": [
            "<strong><u>Close your eyes</u></strong> and sit or lie&nbsp;comfortably.",
            "Focus attention on the <strong><u>crown of&nbsp;head</u></strong>.",
            "Slowly <strong><u>sweep awareness down</u></strong> to your&nbsp;feet.",
            "<strong><u>Release held tightness</u></strong> with each&nbsp;out-breath."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <line x1="200" y1="8" x2="200" y2="124" stroke="#000" stroke-width="3.5"/>
            
            <circle cx="200" cy="18" r="13" stroke="#000" stroke-width="3.5" fill="none"/>
            <circle cx="200" cy="18" r="5" fill="#000"/>
            
            <ellipse cx="200" cy="48" rx="55" ry="9" stroke="#000" stroke-width="3" stroke-dasharray="5 5"/>
            <ellipse cx="200" cy="76" rx="85" ry="11" stroke="#000" stroke-width="3.5"/>
            <ellipse cx="200" cy="104" rx="115" ry="13" stroke="#000" stroke-width="3" stroke-dasharray="6 6"/>
            
            <line x1="50" y1="12" x2="50" y2="118" stroke="#000" stroke-width="2.5"/>
            <polygon points="44,118 50,128 56,118" fill="#000"/>
            <text x="36" y="68" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" transform="rotate(-90 36 68)" letter-spacing="1.5">SCAN DOWN</text>

            <line x1="350" y1="12" x2="350" y2="118" stroke="#000" stroke-width="2.5"/>
            <polygon points="344,118 350,128 356,118" fill="#000"/>
            <text x="366" y="68" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" transform="rotate(90 366 68)" letter-spacing="1.5">HEAD TO TOE</text>
        </svg>
        """
    },
    {
        "id": "04",
        "category": "ACOUSTIC VAGUS",
        "title": "Situational Humming",
        "duration": "1 - 2 MINUTES",
        "steps": [
            "<strong><u>Inhale gently</u></strong> into your lower&nbsp;belly.",
            "Exhale making a steady <strong><u>'mmm'&nbsp;hum</u></strong>.",
            "Feel the <strong><u>vibration in throat</u></strong> and&nbsp;chest.",
            "Repeat for <strong><u>6&nbsp;to&nbsp;8&nbsp;slow&nbsp;breaths</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="52" r="22" fill="#000"/>
            <circle cx="200" cy="52" r="11" fill="#FFF"/>
            <circle cx="200" cy="52" r="4" fill="#000"/>
            
            <path d="M 150 24 C 122 38, 122 66, 150 80" stroke="#000" stroke-width="4.5" stroke-linecap="round"/>
            <path d="M 112 12 C 72 36, 72 68, 112 92" stroke="#000" stroke-width="4" stroke-dasharray="5 5" stroke-linecap="round"/>
            <path d="M 72 2 C 25 32, 25 72, 72 102" stroke="#000" stroke-width="3" stroke-linecap="round"/>

            <path d="M 250 24 C 278 38, 278 66, 250 80" stroke="#000" stroke-width="4.5" stroke-linecap="round"/>
            <path d="M 288 12 C 328 36, 328 68, 288 92" stroke="#000" stroke-width="4" stroke-dasharray="5 5" stroke-linecap="round"/>
            <path d="M 328 2 C 375 32, 375 72, 328 102" stroke="#000" stroke-width="3" stroke-linecap="round"/>

            <text x="200" y="125" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">THROAT &amp; CHEST VIBRATION</text>
        </svg>
        """
    },
    {
        "id": "05",
        "category": "COLD RESET",
        "title": "Cold Water Reset",
        "duration": "1 MINUTE",
        "steps": [
            "Splash <strong><u>cold water</u></strong> over eyes and&nbsp;forehead.",
            "Or hold <strong><u>inner wrists</u></strong> under cold&nbsp;tap.",
            "Feel the <strong><u>cooling shock</u></strong> lower heart&nbsp;rate.",
            "Take <strong><u>3&nbsp;slow belly&nbsp;breaths</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M 200 8 C 200 8, 172 44, 172 66 C 172 80, 184 92, 200 92 C 216 92, 228 80, 228 66 C 228 44, 200 8, 200 8 Z" fill="#000"/>
            <circle cx="191" cy="62" r="4.5" fill="#FFF"/>
            
            <ellipse cx="200" cy="85" rx="75" ry="13" stroke="#000" stroke-width="4" fill="none"/>
            <ellipse cx="200" cy="85" rx="130" ry="17" stroke="#000" stroke-width="2.5" stroke-dasharray="6 6" fill="none"/>

            <circle cx="110" cy="42" r="7.5" fill="#000"/>
            <circle cx="138" cy="20" r="4.5" fill="#000"/>
            <circle cx="290" cy="42" r="7.5" fill="#000"/>
            <circle cx="262" cy="20" r="4.5" fill="#000"/>

            <text x="200" y="125" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">DIVE REFLEX ACTIVATION</text>
        </svg>
        """
    },
    {
        "id": "06",
        "category": "NEUROMUSCULAR",
        "title": "Muscle Relaxation",
        "duration": "5 - 10 MINUTES",
        "steps": [
            "<strong><u>Tense feet and toes</u></strong> tightly for <strong><u>5&nbsp;seconds</u></strong>.",
            "<strong><u>Release completely</u></strong>, feeling warm&nbsp;relief.",
            "Progress upward: <strong><u>legs, hands, and&nbsp;jaw</u></strong>.",
            "<strong><u>Hold hard</u></strong>, then let go fully each&nbsp;time."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(50, 10)">
                <rect x="0" y="0" width="75" height="75" fill="#000" rx="9"/>
                <line x1="18" y1="18" x2="57" y2="57" stroke="#FFF" stroke-width="3"/>
                <line x1="57" y1="18" x2="18" y2="57" stroke="#FFF" stroke-width="3"/>
                <circle cx="37.5" cy="37.5" r="9" fill="#FFF"/>
                <text x="37.5" y="102" font-family="'Jost', sans-serif" font-size="14" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">HOLD (5S)</text>
            </g>

            <g transform="translate(180, 38)">
                <line x1="0" y1="10" x2="40" y2="10" stroke="#000" stroke-width="4.5"/>
                <polygon points="40,1 52,10 40,19" fill="#000"/>
                <text x="25" y="-8" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">RELEASE</text>
            </g>

            <g transform="translate(275, 10)">
                <rect x="0" y="0" width="75" height="75" stroke="#000" stroke-width="4" rx="9" fill="none"/>
                <circle cx="37.5" cy="37.5" r="24" stroke="#000" stroke-width="2.5" stroke-dasharray="4 4"/>
                <circle cx="37.5" cy="37.5" r="9" fill="#000"/>
                <text x="37.5" y="102" font-family="'Jost', sans-serif" font-size="14" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">LET GO (10S)</text>
            </g>
        </svg>
        """
    },
    {
        "id": "07",
        "category": "BILATERAL STIM",
        "title": "Butterfly Hug",
        "duration": "2 - 3 MINUTES",
        "steps": [
            "<strong><u>Cross arms</u></strong> over chest, hands on&nbsp;collarbones.",
            "<strong><u>Interlock thumbs</u></strong> to form butterfly&nbsp;wings.",
            "<strong><u>Alternately tap</u></strong> left and right hands&nbsp;rhythmically.",
            "Breathe easy to the <strong><u>slow tapping&nbsp;pace</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M 190 56 C 125 10, 55 28, 68 70 C 78 96, 135 92, 190 68" stroke="#000" stroke-width="4.5" fill="none"/>
            <circle cx="115" cy="54" r="17" stroke="#000" stroke-width="3" stroke-dasharray="4 4"/>
            <text x="115" y="61" font-family="'Jost', sans-serif" font-size="16" font-weight="900" fill="#000" text-anchor="middle">L</text>

            <circle cx="200" cy="64" r="9" fill="#000"/>

            <path d="M 210 56 C 275 10, 345 28, 332 70 C 322 96, 265 92, 210 68" stroke="#000" stroke-width="4.5" fill="none"/>
            <circle cx="285" cy="54" r="17" stroke="#000" stroke-width="3" stroke-dasharray="4 4"/>
            <text x="285" y="61" font-family="'Jost', sans-serif" font-size="16" font-weight="900" fill="#000" text-anchor="middle">R</text>

            <text x="200" y="122" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">SLOW ALTERNATING TAPS</text>
        </svg>
        """
    },
    {
        "id": "08",
        "category": "SPATIAL SAFETY",
        "title": "Orienting Exercise",
        "duration": "1 - 2 MINUTES",
        "steps": [
            "Keep body still and <strong><u>slowly turn head&nbsp;left</u></strong>.",
            "Look around and <strong><u>name 5&nbsp;neutral&nbsp;objects</u></strong>.",
            "<strong><u>Turn head slowly right</u></strong> and&nbsp;repeat.",
            "Let eyes rest on a <strong><u>safe focal&nbsp;point</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <text x="200" y="16" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">360 HORIZON</text>
            
            <path d="M 40 75 C 120 28, 280 28, 360 75" stroke="#000" stroke-width="3" stroke-dasharray="5 5"/>
            
            <circle cx="200" cy="62" r="28" stroke="#000" stroke-width="4" fill="none"/>
            <circle cx="200" cy="62" r="12" fill="#000"/>
            <circle cx="200" cy="62" r="4.5" fill="#FFF"/>

            <line x1="75" y1="70" x2="172" y2="62" stroke="#000" stroke-width="3"/>
            <circle cx="75" cy="70" r="7.5" fill="#000"/>
            <text x="75" y="112" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">SCAN L</text>

            <line x1="325" y1="70" x2="228" y2="62" stroke="#000" stroke-width="3"/>
            <circle cx="325" cy="70" r="7.5" fill="#000"/>
            <text x="325" y="112" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">SCAN R</text>
        </svg>
        """
    },
    {
        "id": "09",
        "category": "PHYSICAL ANCHOR",
        "title": "Feet On Ground",
        "duration": "1 - 2 MINUTES",
        "steps": [
            "Plant <strong><u>both feet flat</u></strong> on the&nbsp;floor.",
            "<strong><u>Push down firmly</u></strong> through heels and&nbsp;toes.",
            "Feel the <strong><u>solid floor</u></strong> holding your&nbsp;weight.",
            "<strong><u>Hold for 10&nbsp;seconds</u></strong>, release, repeat&nbsp;3x."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g transform="translate(105, 10)">
                <rect x="0" y="0" width="46" height="64" rx="23" stroke="#000" stroke-width="4" fill="none"/>
                <line x1="23" y1="16" x2="23" y2="48" stroke="#000" stroke-width="3.5"/>
                <polygon points="17,48 23,58 29,48" fill="#000"/>
            </g>

            <g transform="translate(249, 10)">
                <rect x="0" y="0" width="46" height="64" rx="23" stroke="#000" stroke-width="4" fill="none"/>
                <line x1="23" y1="16" x2="23" y2="48" stroke="#000" stroke-width="3.5"/>
                <polygon points="17,48 23,58 29,48" fill="#000"/>
            </g>

            <line x1="30" y1="84" x2="370" y2="84" stroke="#000" stroke-width="5"/>
            <line x1="50" y1="84" x2="35" y2="98" stroke="#000" stroke-width="2.5"/>
            <line x1="100" y1="84" x2="85" y2="98" stroke="#000" stroke-width="2.5"/>
            <line x1="150" y1="84" x2="135" y2="98" stroke="#000" stroke-width="2.5"/>
            <line x1="200" y1="84" x2="185" y2="98" stroke="#000" stroke-width="2.5"/>
            <line x1="250" y1="84" x2="235" y2="98" stroke="#000" stroke-width="2.5"/>
            <line x1="300" y1="84" x2="285" y2="98" stroke="#000" stroke-width="2.5"/>
            <line x1="350" y1="84" x2="335" y2="98" stroke="#000" stroke-width="2.5"/>

            <text x="200" y="124" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">SOLID GROUND BASE</text>
        </svg>
        """
    },
    {
        "id": "10",
        "category": "SOMATIC FORCE",
        "title": "Wall Press Reset",
        "duration": "2 - 3 MINUTES",
        "steps": [
            "Face a solid wall at <strong><u>arm-length&nbsp;distance</u></strong>.",
            "Place <strong><u>palms flat</u></strong> at chest&nbsp;height.",
            "<strong><u>Push hard (80%&nbsp;force)</u></strong> for <strong><u>10&nbsp;seconds</u></strong>.",
            "<strong><u>Drop arms and rest 15s</u></strong>. Repeat <strong><u>3&nbsp;times</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="295" y="10" width="22" height="96" fill="#000"/>
            <line x1="322" y1="18" x2="342" y2="38" stroke="#000" stroke-width="3"/>
            <line x1="322" y1="46" x2="342" y2="66" stroke="#000" stroke-width="3"/>
            <line x1="322" y1="74" x2="342" y2="94" stroke="#000" stroke-width="3"/>

            <g transform="translate(45, 20)">
                <line x1="0" y1="16" x2="230" y2="16" stroke="#000" stroke-width="5.5"/>
                <polygon points="230,5 246,16 230,27" fill="#000"/>
                
                <line x1="35" y1="48" x2="230" y2="48" stroke="#000" stroke-width="5.5"/>
                <polygon points="230,37 246,48 230,59" fill="#000"/>

                <circle cx="246" cy="16" r="7" fill="#000"/>
                <circle cx="246" cy="48" r="7" fill="#000"/>
            </g>

            <text x="140" y="124" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">MAX ISOMETRIC PUSH</text>
            <text x="335" y="124" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="1">WALL</text>
        </svg>
        """
    },
    {
        "id": "11",
        "category": "TEMPERATURE SHOCK",
        "title": "Ice Vagus Shock",
        "duration": "1 - 2 MINUTES",
        "steps": [
            "Press <strong><u>ice or cold roller</u></strong> to inner&nbsp;wrists.",
            "Glide slowly along the <strong><u>side of your&nbsp;neck</u></strong>.",
            "Rest ice on your <strong><u>chest center for 15s</u></strong>.",
            "Take <strong><u>3&nbsp;deep grounding&nbsp;breaths</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <polygon points="200,12 240,34 240,78 200,100 160,78 160,34" stroke="#000" stroke-width="4.5" fill="none"/>
            <polygon points="200,24 226,38 226,72 200,86 174,72 174,38" fill="#000"/>
            
            <line x1="160" y1="34" x2="105" y2="12" stroke="#000" stroke-width="3"/>
            <line x1="160" y1="56" x2="90" y2="56" stroke="#000" stroke-width="3.5"/>
            <line x1="160" y1="78" x2="105" y2="100" stroke="#000" stroke-width="3"/>
            <circle cx="90" cy="56" r="6" fill="#000"/>

            <line x1="240" y1="34" x2="295" y2="12" stroke="#000" stroke-width="3"/>
            <line x1="240" y1="56" x2="310" y2="56" stroke="#000" stroke-width="3.5"/>
            <line x1="240" y1="78" x2="295" y2="100" stroke="#000" stroke-width="3"/>
            <circle cx="310" cy="56" r="6" fill="#000"/>

            <text x="200" y="125" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">CERVICAL VAGUS PATH</text>
        </svg>
        """
    },
    {
        "id": "12",
        "category": "STEPPED CADENCE",
        "title": "Ladder Breathing",
        "duration": "3 - 5 MINUTES",
        "steps": [
            "<strong><u>Inhale 2s, exhale 4s</u></strong> (repeat&nbsp;2x).",
            "<strong><u>Inhale 3s, exhale 6s</u></strong> (repeat&nbsp;2x).",
            "<strong><u>Inhale 4s, exhale 8s</u></strong> (repeat&nbsp;2x).",
            "Climb to <strong><u>5&nbsp;in&nbsp;/&nbsp;10&nbsp;out</u></strong>, then step&nbsp;down."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="40" y="58" width="55" height="30" stroke="#000" stroke-width="3" fill="none"/>
            <text x="67" y="79" font-family="'Jost', sans-serif" font-size="14" font-weight="900" fill="#000" text-anchor="middle">2:4</text>

            <rect x="115" y="40" width="65" height="48" stroke="#000" stroke-width="3" fill="none"/>
            <text x="147" y="70" font-family="'Jost', sans-serif" font-size="15" font-weight="900" fill="#000" text-anchor="middle">3:6</text>

            <rect x="200" y="20" width="75" height="68" stroke="#000" stroke-width="3" fill="none"/>
            <text x="237" y="60" font-family="'Jost', sans-serif" font-size="15" font-weight="900" fill="#000" text-anchor="middle">4:8</text>

            <rect x="295" y="4" width="85" height="84" fill="#000" rx="4"/>
            <text x="337" y="50" font-family="'Jost', sans-serif" font-size="17" font-weight="900" fill="#FFF" text-anchor="middle">5:10</text>

            <line x1="30" y1="88" x2="385" y2="88" stroke="#000" stroke-width="3"/>
            
            <text x="200" y="122" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">PROGRESSIVE RATIO ASCENT</text>
        </svg>
        """
    },
    {
        "id": "13",
        "category": "DIAPHRAGM RELEASE",
        "title": "Diaphragm Exhale",
        "duration": "1 - 2 MINUTES",
        "steps": [
            "<strong><u>Inhale gently</u></strong> through nose into&nbsp;ribs.",
            "<strong><u>Exhale completely</u></strong> through&nbsp;mouth.",
            "<strong><u>Squeeze lower abs</u></strong> to empty all&nbsp;air.",
            "<strong><u>Pause 2&nbsp;seconds</u></strong> in silence before&nbsp;refilling."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <text x="200" y="18" font-family="'Jost', sans-serif" font-size="12" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">FULL CAPACITY</text>

            <path d="M 45 30 C 130 30, 170 78, 195 88" stroke="#000" stroke-width="4.5" stroke-linecap="round" fill="none"/>
            <path d="M 355 30 C 270 30, 230 78, 205 88" stroke="#000" stroke-width="4.5" stroke-linecap="round" fill="none"/>
            
            <circle cx="200" cy="90" r="9" fill="#000"/>
            <circle cx="200" cy="90" r="18" stroke="#000" stroke-width="2.5" stroke-dasharray="4 4"/>

            <line x1="135" y1="64" x2="180" y2="80" stroke="#000" stroke-width="3"/>
            <polygon points="180,72 190,83 177,86" fill="#000"/>

            <line x1="265" y1="64" x2="220" y2="80" stroke="#000" stroke-width="3"/>
            <polygon points="223,86 210,83 220,72" fill="#000"/>

            <text x="200" y="126" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">COMPLETE BASAL EMPTYING</text>
        </svg>
        """
    },
    {
        "id": "14",
        "category": "VISCERAL RESONANCE",
        "title": "Voo Sound Exhale",
        "duration": "2 - 3 MINUTES",
        "steps": [
            "Take a <strong><u>soft, easy breath</u></strong> into&nbsp;belly.",
            "Exhale making a <strong><u>deep, low 'Voooo'&nbsp;tone</u></strong>.",
            "Feel the <strong><u>rumble in gut and&nbsp;pelvis</u></strong>.",
            "Empty breath fully and <strong><u>repeat 4&nbsp;times</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M 30 52 Q 75 10, 120 52 T 210 52 T 300 52 T 370 52" stroke="#000" stroke-width="5.5" fill="none"/>
            
            <circle cx="75" cy="31" r="7.5" fill="#000"/>
            <circle cx="165" cy="73" r="7.5" fill="#000"/>
            <circle cx="255" cy="31" r="7.5" fill="#000"/>
            <circle cx="345" cy="73" r="7.5" fill="#000"/>

            <line x1="30" y1="12" x2="370" y2="12" stroke="#000" stroke-width="2" stroke-dasharray="5 5"/>
            <line x1="30" y1="92" x2="370" y2="92" stroke="#000" stroke-width="2" stroke-dasharray="5 5"/>

            <text x="200" y="124" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">LOW FREQUENCY RESONANCE</text>
        </svg>
        """
    },
    {
        "id": "15",
        "category": "DISCHARGE ENERGY",
        "title": "Neurogenic Shakeout",
        "duration": "2 - 3 MINUTES",
        "steps": [
            "Stand with <strong><u>loose knees and soft&nbsp;joints</u></strong>.",
            "<strong><u>Shake hands and wrists</u></strong>&nbsp;vigorously.",
            "Let <strong><u>vibration spread</u></strong> to arms and&nbsp;legs.",
            "<strong><u>Bounce on heels</u></strong>, then stand completely&nbsp;still."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M 30 54 L 60 16 L 85 86 L 110 24 L 135 82 L 160 30 L 185 78 L 210 30 L 235 78 L 260 24 L 285 82 L 310 30 L 335 74 L 370 54" stroke="#000" stroke-width="4.5" stroke-linejoin="round" fill="none"/>
            
            <circle cx="60" cy="10" r="4" fill="#000"/>
            <circle cx="110" cy="16" r="5" fill="#000"/>
            <circle cx="210" cy="20" r="4" fill="#000"/>
            <circle cx="260" cy="16" r="5" fill="#000"/>

            <circle cx="85" cy="94" r="4" fill="#000"/>
            <circle cx="135" cy="90" r="5" fill="#000"/>
            <circle cx="235" cy="86" r="4" fill="#000"/>
            <circle cx="285" cy="90" r="5" fill="#000"/>

            <text x="200" y="124" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">KINETIC TENSION DISCHARGE</text>
        </svg>
        """
    },
    {
        "id": "16",
        "category": "CRANIAL RELEASE",
        "title": "Jaw & Skull Release",
        "duration": "2 MINUTES",
        "steps": [
            "Place <strong><u>fingertips on jaw joints</u></strong> in front of&nbsp;ears.",
            "<strong><u>Open mouth slowly</u></strong> into a wide, gentle&nbsp;yawn.",
            "<strong><u>Massage cheek muscles</u></strong> in slow&nbsp;circles.",
            "Let your <strong><u>lower jaw hang loose and&nbsp;heavy</u></strong>."
        ],
        "svg": """
        <svg viewBox="0 0 400 135" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M 105 28 C 150 6, 250 6, 295 28" stroke="#000" stroke-width="5" stroke-linecap="round" fill="none"/>
            
            <circle cx="105" cy="28" r="8" fill="#000"/>
            <circle cx="295" cy="28" r="8" fill="#000"/>
            
            <path d="M 105 28 C 130 84, 270 84, 295 28" stroke="#000" stroke-width="4.5" stroke-linecap="round" fill="none"/>
            
            <line x1="200" y1="32" x2="200" y2="72" stroke="#000" stroke-width="3.5"/>
            <polygon points="192,72 200,84 208,72" fill="#000"/>

            <circle cx="145" cy="54" r="11" stroke="#000" stroke-width="2.5" stroke-dasharray="3 4"/>
            <circle cx="255" cy="54" r="11" stroke="#000" stroke-width="2.5" stroke-dasharray="3 4"/>

            <text x="200" y="122" font-family="'Jost', sans-serif" font-size="13" font-weight="900" fill="#000" text-anchor="middle" letter-spacing="2">MASSETER GRAVITY RELEASE</text>
        </svg>
        """
    }
]

def generate_card_html(card):
    steps_html = ""
    for idx, step in enumerate(card["steps"], start=1):
        steps_html += f"""
        <div class="step-row">
            <div class="step-num">{idx}</div>
            <div class="step-text">{step}</div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=528, height=792, initial-scale=1.0">
    <title>{card['title']} - X3 E-Ink</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700;800;900&family=Roboto+Slab:wght@700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-font-smoothing: antialiased;
        }}
        body {{
            width: 528px;
            height: 792px;
            overflow: hidden;
            background-color: #FFFFFF;
            color: #000000;
            font-family: 'Brandon Grotesque', 'Jost', -apple-system, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .card-container {{
            width: 528px;
            height: 792px;
            padding: 20px 22px 20px 22px;
            background: #FFFFFF;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            position: relative;
            border: 4px solid #000000;
        }}
        
        /* Top Category Pill */
        .category-row {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 8px;
        }}
        .category-pill {{
            background: #000000;
            color: #FFFFFF;
            padding: 3px 12px;
            font-size: 16px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
            border-radius: 3px;
        }}
        .category-line {{
            flex: 1;
            height: 2.5px;
            background: #000000;
        }}

        /* Title Area: Large Slab Serif strictly 1 line */
        .title-block {{
            margin-bottom: 4px;
        }}
        .title-text {{
            font-family: 'Roboto Slab', 'Rockwell', serif;
            font-weight: 900;
            font-size: 37px;
            line-height: 1.12;
            color: #000000;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            letter-spacing: -0.3px;
        }}
        
        /* Duration Badge: 1.5x Larger, Spaced Kerning */
        .duration-badge {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-top: 5px;
            background: #FFFFFF;
            color: #000000;
            border: 2.5px solid #000000;
            padding: 4px 16px;
            border-radius: 28px;
            font-size: 24px;
            font-weight: 900;
            letter-spacing: 2px;
            text-transform: uppercase;
        }}
        .duration-badge svg {{
            width: 20px;
            height: 20px;
            fill: #000000;
        }}

        /* Vector Art Box */
        .art-box {{
            width: 100%;
            height: 142px;
            margin: 10px 0 10px 0;
            border: 2.5px solid #000000;
            background: #FFFFFF;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 6px;
        }}
        .art-box svg {{
            width: 100%;
            height: 100%;
        }}

        /* Section Subhead */
        .how-header {{
            font-size: 16px;
            font-weight: 900;
            letter-spacing: 2.5px;
            text-transform: uppercase;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .how-header::after {{
            content: "";
            flex: 1;
            height: 2px;
            background: #000000;
        }}

        /* Step-by-Step List (1.5x Larger: 31px, Spaced Kerning, 450 weight, Balanced Text Wrap) */
        .steps-container {{
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        .step-row {{
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }}
        .step-num {{
            min-width: 44px;
            height: 44px;
            border: 3px solid #000000;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            font-weight: 900;
            line-height: 1;
            margin-top: 2px;
            background: #000000;
            color: #FFFFFF;
        }}
        .step-text {{
            font-size: 31px;
            line-height: 1.28;
            font-weight: 450;
            color: #000000;
            letter-spacing: 0.4px;
            text-wrap: pretty;
        }}
        .step-text strong {{
            font-weight: 800;
            color: #000000;
        }}
        .step-text u {{
            text-decoration: none;
            border-bottom: 2.5px solid #000000;
            padding-bottom: 1px;
        }}
    </style>
</head>
<body>
    <div class="card-container">
        <!-- Top Category -->
        <div class="category-row">
            <span class="category-pill">{card['category']}</span>
            <div class="category-line"></div>
        </div>

        <!-- Title & Duration -->
        <div class="title-block">
            <div class="title-text">{card['title']}</div>
            <div class="duration-badge">
                <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" stroke="#000" stroke-width="2.5" fill="none"/><path d="M12 6v6l4 2" stroke="#000" stroke-width="2.5" stroke-linecap="round"/></svg>
                <span>{card['duration']}</span>
            </div>
        </div>

        <!-- Abstract Vector Art (With Clean, Non-Colliding Labels) -->
        <div class="art-box">
            {card['svg']}
        </div>

        <!-- How Step-by-Step -->
        <div>
            <div class="how-header">PRACTICE STEPS</div>
            <div class="steps-container">
                {steps_html}
            </div>
        </div>
    </div>
</body>
</html>
"""
    return html

def main():
    os.makedirs("x3_somatic_cards", exist_ok=True)
    for card in CARDS:
        filename = f"x3_somatic_cards/card_{card['id']}.html"
        with open(filename, "w") as f:
            f.write(generate_card_html(card))
        print(f"Generated {filename}")

if __name__ == "__main__":
    main()
