#!/usr/bin/env python3
"""Bulk-import omarchytheme.com registry themes as Hudu themes.

Reads the site's themes-data.json (palettes embedded as colors_json),
generates themes/<slug>/theme.css + README.md for every portable dark
theme, pairs light variants by naming convention, and writes a catalog
at themes/README.md.

Usage:
    import_registry.py --data /path/to/themes-data.json [--limit N]

Skips: slugs already present in themes/, light-only themes (they become
pairs, not standalone ports), and entries without a complete palette.
Existing per-theme READMEs are never overwritten.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from port import (build_accent_ramps, build_base_ramp, calibrate,
                  enforce_text_floors, is_dark, render, render_readme,
                  synth_light_bg)

REPO = Path(__file__).resolve().parents[2]
LIGHT_SUFFIXES = ["-light", "-latte", "-day", "-dawn"]
REQUIRED = ["background", "foreground"] + [f"color{i}" for i in range(1, 7)]


def load_registry(path):
    out = {}
    for t in json.load(open(path)):
        cj = t.get("colors_json")
        if not cj:
            continue
        try:
            pal = json.loads(cj)
        except json.JSONDecodeError:
            continue
        if any(k not in pal for k in REQUIRED):
            continue
        out[t["slug"]] = {"pal": pal, "meta": t}
    return out


def find_light_pair(slug, registry):
    for suffix in LIGHT_SUFFIXES:
        cand = slug + suffix
        if cand in registry and not is_dark(registry[cand]["pal"]):
            return cand
    return None


def credit_line(meta):
    owner, repo = meta.get("github_owner"), meta.get("github_repo")
    url = meta.get("github_url")
    if owner and url:
        return (f"Palette from [{owner}/{repo}]({url}) — listed on "
                f"[omarchytheme.com](https://omarchytheme.com/themes/{meta['slug']}/).")
    return f"Palette listed on [omarchytheme.com](https://omarchytheme.com/themes/{meta['slug']}/)."


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", required=True)
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()

    registry = load_registry(args.data)
    cal = calibrate()
    done, skipped_existing, lights, failed = [], [], [], []

    darks = {s: e for s, e in registry.items() if is_dark(e["pal"])}
    lights = [s for s in registry if s not in darks]

    count = 0
    for slug, entry in sorted(darks.items()):
        out_dir = REPO / "themes" / slug
        if out_dir.exists():
            skipped_existing.append(slug)
            continue
        if args.limit and count >= args.limit:
            break
        pal, meta = entry["pal"], entry["meta"]
        light_slug = find_light_pair(slug, registry)
        light_pal = registry[light_slug]["pal"] if light_slug else None
        try:
            black = pal["background"]
            paper = light_pal["background"] if light_pal else synth_light_bg(black)
            tokens = build_base_ramp(paper, black, pal, light_pal)
            enforce_text_floors(tokens, paper, black)
            tokens.update(build_accent_ramps(pal, paper, black, cal, light_pal))
            css = render(tokens, slug, slug, light_slug)
            md = render_readme(tokens, slug, slug, light_slug,
                               light_pinned_300=bool(light_pal and "color7" in light_pal))
            md = md.replace("<!-- TODO: add upstream palette credit + link -->", credit_line(meta))
        except SystemExit as e:
            failed.append((slug, str(e)))
            continue
        out_dir.mkdir(parents=True)
        (out_dir / "theme.css").write_text(css)
        if not (out_dir / "README.md").exists():
            (out_dir / "README.md").write_text(md)
        done.append((slug, light_slug))
        count += 1

    write_catalog()
    print(f"imported: {len(done)} (paired light: {sum(1 for _, l in done if l)})")
    print(f"skipped existing: {len(skipped_existing)}; light-only registry entries: {len(lights)}")
    for slug, err in failed:
        print(f"FAILED {slug}: {err}")


def write_catalog():
    rows = []
    for d in sorted((REPO / "themes").iterdir()):
        if not (d / "theme.css").is_dir() and (d / "theme.css").exists():
            header = (d / "theme.css").read_text(encoding="utf-8", errors="replace")[:400]
            modes = "Light + dark" if "light palette: synthesized" not in header else "Dark (+ synthesized light)"
            if d.name == "flexoki":
                modes = "Light + dark"
            rows.append(f"| [{d.name}]({d.name}/) | {modes} | [`theme.css`]({d.name}/theme.css) |")
    catalog = (
        "# Theme catalog\n\n"
        f"{len(rows)} themes. Hand-made: [flexoki](flexoki/). The rest are generated from "
        "[omarchy](https://omarchy.org) palettes — most sourced from the "
        "[omarchytheme.com](https://omarchytheme.com) registry — via "
        "[`tools/omarchy-port`](../tools/omarchy-port/). "
        "Each theme's README documents its palette and provenance.\n\n"
        "| Theme | Modes | Source |\n|-------|-------|--------|\n"
        + "\n".join(rows) + "\n"
    )
    (REPO / "themes" / "README.md").write_text(catalog)
    print(f"catalog: themes/README.md ({len(rows)} themes)")


if __name__ == "__main__":
    main()
