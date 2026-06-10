# Omarchy → Hudu theme porter

Generate Hudu themes from [omarchy](https://omarchy.org) theme palettes.

## Tools

| File | Role |
|------|------|
| [`port_theme.py`](port_theme.py) | Port one omarchy theme -> `themes/<name>/{theme.css,README.md}` |
| [`import_registry.py`](import_registry.py) | Bulk-import the omarchytheme.com registry (`themes-data.json`) |
| [`make_template.py`](make_template.py) | Regenerate `template.css` from the hand-made Flexoki theme |
| [`check_roundtrip.py`](check_roundtrip.py) | Sanity check: flexoki round-trip must reproduce the hand-made theme |
| [`flexoki_palette.py`](flexoki_palette.py) | Flexoki extended-palette reference data (shared by the above) |
| [`template.css`](template.css) | The Flexoki theme with its 73 palette hexes tokenized (committed artifact) |

## Usage

```bash
# one theme (pair a light variant when one exists)
python3 tools/omarchy-to-hudu/port_theme.py --dark catppuccin-mocha --light catppuccin-latte --name catppuccin

# bulk registry sync (community data -- slugs/URLs are validated before use)
python3 tools/omarchy-to-hudu/import_registry.py --data path/to/themes-data.json [--force-css]

# after editing themes/flexoki/theme.css
python3 tools/omarchy-to-hudu/make_template.py && python3 tools/omarchy-to-hudu/check_roundtrip.py
```

## How it works

- `template.css` is the Flexoki theme with every palette hex replaced by a `{{token}}` placeholder; Hudu's stock-color attribute matchers stay literal, and Flexoki-specific comment wording is neutralized so generated themes don't narrate as Flexoki.
- `port_theme.py` reads the omarchy palette (`colors.toml` or `alacritty.toml`), pins tokens the palette defines directly (bg/fg -> anchors and text tiers, ANSI normal/bright -> 600/400 accent levels), and synthesizes the remaining 50-950 ramp steps by OKLab interpolation, with fractions calibrated at runtime against Flexoki's published ramps. A paired `--light` theme supplies light-mode accents and faint-text tones when it carries distinct values; orange and purple have no ANSI slots and are blended from red+yellow / blue+magenta.
- Readability floors guard text tokens: anything below `min(0.85 x Flexoki reference contrast, WCAG cap)` is re-derived by pure anchor interpolation (caps: 7:1 primary, 4.5:1 muted).
- Each port also emits a palette README (swatch tables, pinned-vs-derived markers) with a credit TODO -- fill in the upstream palette author/link before committing. Existing READMEs are never overwritten.
- `check_roundtrip.py` guards the calibration: porting flexoki-dark + flexoki-light must reproduce the hand-made theme -- pinned tokens exactly, derived intermediates within dE 6.

## Caveats

- omarchy themes are single-mode; without `--light` the light half is synthesized from the dark palette -- fine for previews, mediocre for daily light-mode use.
- Generated themes are ~85% there: the hand-tuned Hudu fixes carry over (palette-independent), but eyeball callouts, badges, and the derived orange/purple before shipping.
