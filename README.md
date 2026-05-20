<div align="center">

# hudu-themes

*Custom CSS themes for [Hudu](https://www.hudu.com)*

[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

[Themes](#themes) • [Install](#install) • [Uninstall](#uninstall) • [Contributing a theme](#contributing-a-theme)

</div>

---

Drop-in CSS skins for Hudu's documentation platform. Each theme is a single `theme.css` file you paste into Hudu's custom CSS field — no build step, no JS, no Hudu admin gymnastics.

## Themes

| Theme | Palette | Modes | Source |
|-------|---------|-------|--------|
| [Flexoki](themes/flexoki/) | Warm paper tones by [Steph Ango](https://stephango.com/flexoki) | Light + dark | [`theme.css`](themes/flexoki/theme.css) |

## Install

1. Open Hudu as an admin.
2. Navigate to **Admin → Settings → Customize Branding** (the **Custom CSS** field).
3. Open the theme's `theme.css` from this repo, copy the entire file.
4. Paste into the Custom CSS field and save.
5. Hard-refresh (`Ctrl+Shift+R` / `Cmd+Shift+R`) to clear cached styles.

> [!NOTE]
> Hudu's Custom CSS field is global — the theme applies to every user on your instance, not just you.

> [!TIP]
> Back up your existing custom CSS before pasting a theme over it. There's no undo.

## Uninstall

Clear the Custom CSS field, save, hard-refresh.

## Contributing a theme

1. Create `themes/<your-theme>/theme.css`.
2. Add a per-theme `README.md` next to it (palette source, credits, screenshots if you have them).
3. Add a row to the [Themes](#themes) table.
4. Open a PR.

> [!IMPORTANT]
> Themes must override Hudu's CSS variables only — no DOM-targeting selectors that depend on Hudu's internal class names. Hudu refactors its frontend without warning; variable overrides survive, brittle selectors don't.
