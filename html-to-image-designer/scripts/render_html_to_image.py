#!/usr/bin/env python3
"""Render a local HTML file to PNG/JPG using Playwright.

Example:
  python scripts/render_html_to_image.py \
    --html index.html \
    --output poster.png \
    --width 1200 --height 630
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render local HTML into an image")
    parser.add_argument("--html", required=True, help="Path to input HTML file")
    parser.add_argument("--output", required=True, help="Output image path (.png/.jpg/.jpeg)")
    parser.add_argument("--width", type=int, default=1200, help="Viewport width")
    parser.add_argument("--height", type=int, default=630, help="Viewport height")
    parser.add_argument("--selector", default="body", help="CSS selector to capture")
    parser.add_argument("--full-page", action="store_true", help="Capture full page instead of selector")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    html_path = Path(args.html).resolve()
    output_path = Path(args.output).resolve()

    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError(
            "Playwright is required. Install with `pip install playwright` and run `playwright install chromium`."
        ) from exc

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": args.width, "height": args.height})
        page.goto(html_path.as_uri(), wait_until="networkidle")

        if args.full_page:
            page.screenshot(path=str(output_path), full_page=True)
        else:
            locator = page.locator(args.selector)
            if locator.count() == 0:
                raise ValueError(f"Selector not found: {args.selector}")
            locator.first.screenshot(path=str(output_path))

        browser.close()

    print(f"Saved screenshot to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
