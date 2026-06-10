# omarchy-port

Generate a Hudu `theme.css` from an [omarchy](https://omarchy.org) theme's palette.

```bash
python3 tools/omarchy-port/port.py --dark catppuccin-mocha --light catppuccin-latte --name catppuccin
```

Writes `themes/<name>/theme.css`, ready to paste into Hudu **Admin → Design → Custom CSS**.

## How it works

- `template.css` is the [Flexoki theme](../../themes/flexoki/) with every palette hex replaced by a `{{token}}` placeholder (73 tokens). Regenerate it after editing the Flexoki theme: `python3 tools/omarchy-port/extract_template.py`.
- `port.py` reads the omarchy palette (`colors.toml` or `alacritty.toml`), pins the tokens the palette defines directly (backgrounds, foregrounds, ANSI accents), and synthesizes the rest by OKLab interpolation. Interpolation fractions are calibrated at runtime against Flexoki's published 50–950 ramps. `verify_roundtrip.py` checks the round trip: pinned tokens reproduce exactly, derived intermediates stay within perceptual tolerance.
- ANSI normal colors become light-mode accents (600-level), bright become dark-mode accents (400-level). When a paired `--light` theme carries its own accent values, those win for light mode.
- Orange and purple have no ANSI slots; they're blends of red+yellow and blue+magenta.

## Caveats

- omarchy themes are single-mode. Without `--light`, the light half is synthesized from the dark palette — fine for a preview, mediocre for daily light-mode use.
- Generated themes are ~85% there. The hand-tuned Hudu fixes carry over (they're palette-independent), but expect to eyeball callouts, badges, and derived orange/purple before shipping a theme to the repo.
