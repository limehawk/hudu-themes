<div align="center">

# hudu-themes

*Custom CSS themes for [Hudu](https://www.hudu.com)*

[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Themes](https://img.shields.io/badge/Themes-261-green?style=flat-square)](themes/README.md)

**[Browse them all at huduthemes.com →](https://huduthemes.com)**

[Themes](#themes) • [Install](#install) • [Uninstall](#uninstall) • [Contributing a theme](#contributing-a-theme)

</div>

---

Drop-in CSS skins for Hudu's documentation platform. Each theme is a single `theme.css` file you paste into Hudu's custom CSS field — no build step, no JS, no Hudu admin gymnastics. Preview every theme in light and dark at **[huduthemes.com](https://huduthemes.com)**, with one-click copy.

## Themes

| Theme | Palette | Modes | Source |
|-------|---------|-------|--------|
| [Flexoki](themes/flexoki/) | Inky, minimalist palette by [Steph Ango](https://stephango.com/flexoki) — calibrated for legibility & perceptual balance across light/dark | Light + dark | [`theme.css`](themes/flexoki/theme.css) |
| [Catppuccin](themes/catppuccin/) | Soothing pastels by the [Catppuccin](https://github.com/catppuccin/catppuccin) community — Mocha (dark) + Latte (light) | Light + dark | [`theme.css`](themes/catppuccin/theme.css) |
| [Tokyo Night](themes/tokyo-night/) | Neon-on-dark by [enkia](https://github.com/enkia/tokyo-night-vscode-theme), inspired by Tokyo at night | Dark (+ synthesized light) | [`theme.css`](themes/tokyo-night/theme.css) |
| [Gruvbox](themes/gruvbox/) | Retro groove, warm earthy tones by [morhetz](https://github.com/morhetz/gruvbox) | Dark (+ synthesized light) | [`theme.css`](themes/gruvbox/theme.css) |
| [Nord](themes/nord/) | Arctic, north-bluish palette by [Sven Greb](https://www.nordtheme.com/) | Dark (+ synthesized light) | [`theme.css`](themes/nord/theme.css) |
| [Everforest](themes/everforest/) | Green-based, warm and soft on the eyes, by [sainnhe](https://github.com/sainnhe/everforest) | Dark (+ synthesized light) | [`theme.css`](themes/everforest/theme.css) |
| [Kanagawa](themes/kanagawa/) | Inspired by Hokusai's Great Wave, by [rebelot](https://github.com/rebelot/kanagawa.nvim) | Dark (+ synthesized light) | [`theme.css`](themes/kanagawa/theme.css) |

> The table above is the featured set. Browse the full catalog — **[261 themes on the website](https://huduthemes.com/themes/)** or [in this repo](themes/README.md) — bulk-imported from the [omarchytheme.com](https://omarchytheme.com) registry and generated from [omarchy](https://omarchy.org) palettes via [`tools/omarchy-to-hudu`](tools/omarchy-to-hudu/). Each theme's README documents its palette and provenance.

> [!INFO]
> **Flexoki** is designed for reading and writing on digital screens, inspired by analog inks and warm shades of paper. Learn about its design philosophy, extended palette (50–950 ramps), and mappings at [stephango.com/flexoki](https://stephango.com/flexoki). The full palette reference is documented in the theme's CSS header.

## Install

1. Open Hudu as an admin.
2. Navigate to **Admin → Design** (the **Custom CSS** field).
3. Copy the theme's CSS — one click on its [huduthemes.com](https://huduthemes.com) page, or open `theme.css` here and copy the file.
4. Paste into the Custom CSS field and save.
5. Hard-refresh (`Ctrl+Shift+R` / `Cmd+Shift+R`) to clear cached styles.

> [!NOTE]
> Hudu's Custom CSS field is global — the theme applies to every user on your instance, not just you.

> [!TIP]
> Back up your existing custom CSS before pasting a theme over it. There's no undo.

## Uninstall

Clear the Custom CSS field, save, hard-refresh.

## Contributing a theme

**Porting an [omarchy](https://omarchy.org) theme?** Use the generator — it produces the CSS, palette README, and contrast-checked ramps for you (see [`tools/omarchy-to-hudu/`](tools/omarchy-to-hudu/)):

```bash
python3 tools/omarchy-to-hudu/port_theme.py --dark <omarchy-theme> [--light <light-variant>] --name <name>
```

Fill in the upstream credit TODO in the generated README, then open a PR.

**Hand-making a theme?** Create `themes/<your-theme>/{theme.css,README.md}` (palette source, credits, swatch tables) using [`themes/flexoki/`](themes/flexoki/) as the reference.

**Either way:** see [CONTRIBUTING.md](CONTRIBUTING.md) for the full PR checklist — branch naming, credit requirements, how to test on a live instance, and what reviewers look for.

> [!IMPORTANT]
> Prefer overriding Hudu's CSS variables; DOM-targeting selectors are used sparingly and only where variables can't reach. Hudu refactors its frontend without warning — variable overrides survive, brittle selectors don't.
