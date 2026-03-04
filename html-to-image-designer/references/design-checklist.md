# Design Checklist (HTML before Image Export)

## 1) Composition
- One clear focal point.
- Visual hierarchy is obvious in 3 seconds.
- Balanced whitespace (no edge crowding).

## 2) Typography
- Max 2 font families.
- Headline weight and size clearly dominant.
- Body text line-height around 1.4–1.7.

## 3) Color
- Primary + accent colors are consistent.
- Sufficient contrast for readability.
- Background texture/gradients do not reduce legibility.

## 4) Layout Safety
- Keep key text inside 6–8% safe margins.
- Explicit export dimensions match target platform.
- No clipping at common aspect ratios.

## 5) Screenshot Stability
- Capture root has fixed width and height.
- `overflow: hidden` on capture container.
- Avoid random/clock-based visuals if deterministic output is needed.

## 6) Final Validation
- Open generated image and inspect at 100% zoom.
- Check spelling and punctuation.
- Confirm branding and language constraints.
