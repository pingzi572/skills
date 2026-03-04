---
name: html-to-image-designer
description: Generate a polished single-file HTML page from a natural-language description and export it as an image. Use this skill when users want prompt-to-visual workflows, landing-page mockups, posters, social cards, or marketing visuals converted from HTML into PNG/JPG screenshots.
---

# HTML to Image Designer

## Overview

Use this skill when the user wants to: (1) describe a visual idea in text, (2) get a beautiful HTML design, and (3) convert the rendered page to an image.

## Workflow

1. **Clarify output intent**
   - Capture target image size (e.g., `1200x630`, `1080x1920`, `1920x1080`).
   - Confirm style direction (minimal, neon, glassmorphism, editorial, brand colors).
   - Confirm content constraints (language, headline, CTA, logos, no external assets).

2. **Generate a single-file HTML deliverable**
   - Produce one self-contained HTML file with embedded CSS and (if needed) inline SVG.
   - Prefer system fonts or well-known fallbacks (`Inter, Segoe UI, Roboto, Arial, sans-serif`).
   - Avoid remote JS frameworks unless requested.
   - Make layout deterministic for screenshotting:
     - Set explicit canvas/container dimensions.
     - Disable scrollbars (`overflow: hidden`) for the capture area.
     - Keep animations subtle or paused for consistent exports.

3. **Quality-pass the design before export**
   - Validate hierarchy: headline → supporting text → CTA.
   - Validate contrast and spacing.
   - Ensure safe margins so text is not cropped.
   - Use the checklist in `references/design-checklist.md` for final review.

4. **Render HTML into image**
   - Preferred: use `scripts/render_html_to_image.py` to capture PNG/JPG from local HTML.
   - If screenshot tooling is unavailable, provide the HTML and exact command for local execution.

## Output contract

When completing user requests, return:

- `index.html` (or requested filename)
- Export command used
- Output image path(s)
- Optional variants (light/dark or size variants)

## Files in this skill

- `scripts/render_html_to_image.py`: deterministic HTML-to-image renderer via Playwright.
- `references/design-checklist.md`: visual quality and export checks.
- `references/prompt-template.md`: reusable prompt structure for turning ideas into design-ready specs.
