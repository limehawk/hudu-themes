# Contributing a theme

Every theme is a directory: `themes/<slug>/` containing `theme.css` (the paste-ready stylesheet) and `README.md` (palette tables + credits). One theme per PR.

## 1. Fork and branch

```bash
gh repo fork limehawk/hudu-themes --clone && cd hudu-themes
git switch -c theme/<slug>
```

Slug rules: lowercase letters, digits, hyphens (`^[a-z0-9][a-z0-9-]{0,63}$`). Pick something that doesn't collide with the [existing catalog](themes/README.md).

## 2. Create the theme

**Porting an [omarchy](https://omarchy.org) theme** (the easy path — generates CSS, palette README, and contrast-checked ramps):

```bash
python3 tools/omarchy-to-hudu/port_theme.py --dark <omarchy-theme> [--light <light-variant>] --name <slug>
```

Pass `--light` when a paired light variant exists (e.g. `catppuccin-mocha` + `catppuccin-latte`) — synthesized light mode is serviceable, a real one is better. Python 3.11+, stdlib only.

**Hand-making a theme:** start from [`themes/flexoki/theme.css`](themes/flexoki/theme.css) as the reference for which Hudu variables and selectors need covering. Prefer overriding Hudu's CSS variables; DOM-targeting selectors only where variables can't reach — Hudu refactors its frontend without warning.

## 3. Before opening the PR

- [ ] **Fill the credit.** Generated READMEs contain `<!-- TODO: add upstream palette credit + link -->` — replace it with the upstream palette's author, link, and license. Don't guess: verify the link. Uncredited palettes won't be merged.
- [ ] **Test on a real Hudu instance** if you can: paste `theme.css` into **Admin → Design → Custom CSS**, check both modes (profile menu → Enable light/dark mode). Look at: card backgrounds, muted/faint text readability, callouts in KB articles, the admin page tiles.
- [ ] **No regressions to the porter?** If you touched anything under `tools/omarchy-to-hudu/`, run:
  ```bash
  python3 tools/omarchy-to-hudu/check_roundtrip.py
  ```
  It must print `PASS`.
- [ ] Keep the diff to your theme's directory (plus tools changes if that's what your PR is about). Don't edit other themes or regenerate the catalog — it's rebuilt on registry syncs.

## 4. Open the PR

```bash
git push -u origin theme/<slug>
gh pr create --title "Add <name> theme" --body "Palette source + license, light variant used (if any), and whether you tested on a live instance."
```

PRs are rebase-merged. Once merged, the theme appears in the repo catalog and on [huduthemes.limehawk.io](https://huduthemes.limehawk.io) at the next site rebuild.

## Reporting problems

Theme looks broken on a Hudu version? Open an issue with a screenshot, the theme slug, light or dark mode, and the page where it breaks. If a Hudu frontend change broke a selector, say which element — the fix usually lands in `themes/flexoki/theme.css` and propagates to all generated themes via `make_template.py` + a registry re-sync.
