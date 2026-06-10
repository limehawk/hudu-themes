#!/usr/bin/env python3
"""Port an omarchy theme to a Hudu theme.css.

Reads the palette from an omarchy theme dir (colors.toml or alacritty.toml),
synthesizes the full token ramp the Hudu template needs, and renders
template.css into a paste-ready theme.css.

Usage:
    port_theme.py --dark <theme> [--light <theme>] --name <output-name>

<theme> is an omarchy theme name (resolved against ~/.config/omarchy/themes
and ~/.local/share/omarchy/themes) or a path to a theme directory.

Without --light, the light half is synthesized from the dark palette
(a near-white tint of the background hue) — usable, but a paired light
theme always looks better.

Ramp synthesis is calibrated against the Flexoki extended palette: the
interpolation fractions that reproduce Flexoki's published 50-950 ramps
from its own anchor colors are computed at runtime and applied to the
target theme's anchors. Tokens the source palette defines directly
(bg, fg, ANSI colors) are pinned exactly; everything else interpolates
between pins in OKLab space.
"""

import argparse
import re
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from flexoki_palette import RAMPS, STEPS, ANCHORS, token_to_hex

THEME_DIRS = [
    Path.home() / ".config/omarchy/themes",
    Path.home() / ".local/share/omarchy/themes",
]

# ---------------------------------------------------------------- color math

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{round(max(0, min(1, c)) * 255):02X}" for c in rgb)


def _srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _linear_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def rgb_to_oklab(rgb):
    r, g, b = (_srgb_to_linear(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = l ** (1 / 3), m ** (1 / 3), s ** (1 / 3)
    return (
        0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
        1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
        0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
    )


def oklab_to_rgb(lab):
    L, a, b = lab
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return tuple(_linear_to_srgb(c) for c in (r, g, bb))


def mix_hex(h1, h2, t):
    """Interpolate between two hexes in OKLab. t=0 -> h1, t=1 -> h2."""
    a, b = rgb_to_oklab(hex_to_rgb(h1)), rgb_to_oklab(hex_to_rgb(h2))
    return rgb_to_hex(oklab_to_rgb(tuple(x + (y - x) * t for x, y in zip(a, b))))


def best_t(target, h1, h2):
    """Fraction t for which mix(h1, h2, t) is closest to target (projection)."""
    p = rgb_to_oklab(hex_to_rgb(target))
    a, b = rgb_to_oklab(hex_to_rgb(h1)), rgb_to_oklab(hex_to_rgb(h2))
    ab = [y - x for x, y in zip(a, b)]
    ap = [y - x for x, y in zip(a, p)]
    denom = sum(c * c for c in ab)
    return sum(x * y for x, y in zip(ap, ab)) / denom if denom else 0.0


def delta_e(h1, h2):
    """OKLab Euclidean distance x100 (rough perceptual delta)."""
    a, b = rgb_to_oklab(hex_to_rgb(h1)), rgb_to_oklab(hex_to_rgb(h2))
    return 100 * sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5


def contrast(h1, h2):
    """WCAG contrast ratio."""
    def lum(h):
        r, g, b = (_srgb_to_linear(c) for c in hex_to_rgb(h))
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    a, b = lum(h1), lum(h2)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


# ------------------------------------------------------------ palette loading

def resolve_theme(name_or_path):
    p = Path(name_or_path).expanduser()
    if p.is_dir():
        return p
    for base in THEME_DIRS:
        if (base / name_or_path).is_dir():
            return base / name_or_path
    sys.exit(f"theme not found: {name_or_path} (looked in {', '.join(map(str, THEME_DIRS))})")


def load_palette(theme_dir):
    """Return {background, foreground, color0..15} from colors.toml or alacritty.toml."""
    ct = theme_dir / "colors.toml"
    if ct.exists():
        data = tomllib.loads(ct.read_text())
        pal = {k: v for k, v in data.items() if isinstance(v, str) and v.startswith("#")}
        missing = [k for k in ("background", "foreground") if k not in pal]
        if missing:
            sys.exit(f"{ct}: missing keys {missing}")
        return pal
    at = theme_dir / "alacritty.toml"
    if at.exists():
        data = tomllib.loads(at.read_text())
        colors = data.get("colors", {})
        pal = {
            "background": colors["primary"]["background"],
            "foreground": colors["primary"]["foreground"],
        }
        if "dim_foreground" in colors.get("primary", {}):
            pal["dim_foreground"] = colors["primary"]["dim_foreground"]
        names = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        for group, offset in (("normal", 0), ("bright", 8)):
            for i, n in enumerate(names):
                if n in colors.get(group, {}):
                    pal[f"color{offset + i}"] = colors[group][n]
        return pal
    sys.exit(f"{theme_dir}: no colors.toml or alacritty.toml")


def is_dark(pal):
    return rgb_to_oklab(hex_to_rgb(pal["background"]))[0] < rgb_to_oklab(hex_to_rgb(pal["foreground"]))[0]


def synth_light_bg(dark_bg):
    """Near-white tint carrying the dark background's hue."""
    L, a, b = rgb_to_oklab(hex_to_rgb(dark_bg))
    n = (a * a + b * b) ** 0.5 or 1.0
    scale = min(0.012, n) / n
    return rgb_to_hex(oklab_to_rgb((0.978, a * scale, b * scale)))


# ------------------------------------------------------------- ramp synthesis

# ANSI slot -> accent family. Orange/purple have no ANSI slot; derived below.
ANSI_FAMILIES = {"red": 1, "green": 2, "yellow": 3, "blue": 4, "magenta": 5, "cyan": 6}

FLEX = {tok: h for tok, h in token_to_hex().items()}


def flexoki_step_hex(family, step):
    return RAMPS[family].split()[STEPS.index(step)].upper()


def calibrate():
    """Derive interpolation fractions from the Flexoki reference palette."""
    cal = {"accent_low": {}, "accent_high": {}, "accent_mid": 0.0}
    fams = [f for f in RAMPS if f != "base"]
    for step in [50, 100, 150, 200, 300]:
        cal["accent_low"][step] = sum(
            best_t(flexoki_step_hex(f, step), flexoki_step_hex(f, 400), ANCHORS["paper"])
            for f in fams) / len(fams)
    for step in [700, 800, 850, 900, 950]:
        cal["accent_high"][step] = sum(
            best_t(flexoki_step_hex(f, step), flexoki_step_hex(f, 600), ANCHORS["black"])
            for f in fams) / len(fams)
    cal["accent_mid"] = sum(
        best_t(flexoki_step_hex(f, 500), flexoki_step_hex(f, 400), flexoki_step_hex(f, 600))
        for f in fams) / len(fams)
    # orange/purple as blends of their hue neighbours
    cal["orange_t"] = sum(
        best_t(flexoki_step_hex("orange", s), flexoki_step_hex("red", s), flexoki_step_hex("yellow", s))
        for s in (400, 600)) / 2
    cal["purple_t"] = sum(
        best_t(flexoki_step_hex("purple", s), flexoki_step_hex("blue", s), flexoki_step_hex("magenta", s))
        for s in (400, 600)) / 2
    return cal


def build_base_ramp(paper, black, dark_pal, light_pal=None):
    """Base ramp paper..black, pinning tokens the source palettes define.

    Dark palette: fg -> base-200 (dark text), color7 -> base-500 (dark
    muted), color8 -> base-600 (light muted). Light palette: color7 ->
    base-300 (light faint text) — without this pin, base-300 interpolates
    between dark-theme tones and can wash out on light backgrounds.
    (In Flexoki's own colors.toml files these slots hold exactly these
    ramp values, so the pins are identity for the round-trip.)
    """
    pins = {"paper": paper, "black": black}
    if "foreground" in dark_pal:
        pins["base-200"] = dark_pal["foreground"]
    if "color7" in dark_pal:
        pins["base-500"] = dark_pal["color7"]
    if "color8" in dark_pal:
        pins["base-600"] = dark_pal["color8"]
    if light_pal and "color7" in light_pal:
        pins["base-300"] = light_pal["color7"]

    order = ["paper"] + [f"base-{s}" for s in STEPS] + ["black"]
    ref = {"paper": ANCHORS["paper"], "black": ANCHORS["black"]}
    ref.update({f"base-{s}": flexoki_step_hex("base", s) for s in STEPS})

    out = {}
    pin_idx = [i for i, tok in enumerate(order) if tok in pins]
    for a, b in zip(pin_idx, pin_idx[1:]):
        tok_a, tok_b = order[a], order[b]
        out[tok_a], out[tok_b] = pins[tok_a], pins[tok_b]
        for i in range(a + 1, b):
            # position of this step between the two pins, per Flexoki
            t = best_t(ref[order[i]], ref[tok_a], ref[tok_b])
            out[order[i]] = mix_hex(pins[tok_a], pins[tok_b], t)
    return out


def build_accent_ramps(pal, paper, black, cal, light_pal=None):
    """400-level = dark-mode accents (bright ANSI), 600-level = light-mode
    accents. A paired light theme supplies the 600s when it carries its own
    accent values (some light variants, like flexoki-light, just repeat the
    dark theme's bright colors — detected and ignored)."""
    fams = {}
    for fam, slot in ANSI_FAMILIES.items():
        normal, bright = pal.get(f"color{slot}"), pal.get(f"color{slot + 8}")
        if not normal:
            sys.exit(f"palette missing color{slot} ({fam})")
        c400, c600 = bright or normal, normal
        if light_pal:
            lnorm = light_pal.get(f"color{slot}")
            if lnorm and lnorm.upper() != c400.upper():
                c600 = lnorm
        fams[fam] = {"600": c600, "400": c400}
    fams["orange"] = {
        s: mix_hex(fams["red"][s], fams["yellow"][s], cal["orange_t"]) for s in ("400", "600")
    }
    fams["purple"] = {
        s: mix_hex(fams["blue"][s], fams["magenta"][s], cal["purple_t"]) for s in ("400", "600")
    }
    out = {}
    for fam, base in fams.items():
        out[f"{fam}-400"], out[f"{fam}-600"] = base["400"], base["600"]
        out[f"{fam}-500"] = mix_hex(base["400"], base["600"], cal["accent_mid"])
        for step, t in cal["accent_low"].items():
            out[f"{fam}-{step}"] = mix_hex(base["400"], paper, t)
        for step, t in cal["accent_high"].items():
            out[f"{fam}-{step}"] = mix_hex(base["600"], black, t)
    return out


# Text tokens guarded by the readability floor: (token, background token).
# Palette pins can push interpolated text tones too close to their background
# (e.g. a dark theme whose fg AND color7 are both light leaves base-300 —
# light-mode faint text — nearly invisible on synthesized paper). When a
# guarded token contrasts worse than 85% of Flexoki's reference value for the
# same pair, re-derive it by pure anchor interpolation at Flexoki's position.
TEXT_FLOORS = [
    # (token, background token, absolute cap on the floor)
    # Floor = min(0.85 x Flexoki's reference contrast, cap). The cap keeps
    # high-contrast pairs honest in WCAG terms instead of demanding
    # Flexoki-level inkiness from every palette: 7:1 (AAA) for primary text,
    # 4.5:1 (AA) for muted; faint text is judged purely against the
    # reference (Flexoki's faint is ~2:1 by design).
    ("base-300", "paper", None),
    ("base-600", "paper", 4.5),
    ("base-200", "base-950", 7.0),
    ("base-500", "base-950", 4.5),
]


def enforce_text_floors(tokens, paper, black):
    ref = token_to_hex()
    ref["paper"], ref["black"] = ANCHORS["paper"], ANCHORS["black"]
    for tok, bg_tok, cap in TEXT_FLOORS:
        floor = 0.85 * contrast(ref[tok], ref[bg_tok])
        if cap is not None:
            floor = min(floor, cap)
        if contrast(tokens[tok], tokens[bg_tok]) < floor:
            t = best_t(ref[tok], ANCHORS["paper"], ANCHORS["black"])
            tokens[tok] = mix_hex(paper, black, t)


# ------------------------------------------------------------------ rendering

def _swatch(h):
    h = h.upper()
    return f"<img valign='middle' alt='{h}' src='https://readme-swatches.vercel.app/{h.lstrip('#')}'/> `{h}`"


# Role annotations mirror Flexoki's usage mapping (see themes/flexoki/README.md).
BASE_ROLES = [
    ("black", "tx", "bg"), ("base-950", "—", "bg-2"), ("base-900", "—", "ui"),
    ("base-850", "—", "ui-2"), ("base-800", "—", "ui-3"), ("base-700", "—", "tx-3"),
    ("base-600", "tx-2", "—"), ("base-500", "—", "tx-2"), ("base-300", "tx-3", "—"),
    ("base-200", "ui-3", "tx"), ("base-150", "ui-2", "—"), ("base-100", "ui", "—"),
    ("base-50", "bg-2", "—"), ("paper", "bg", "—"),
]
# Tokens pinned verbatim from the source palettes (mirrors build_* pinning rules).
PINNED_BASE = {"black", "base-200", "base-500", "base-600", "paper"}
DERIVED_FAMILIES = {"orange", "purple"}


def render_readme(tokens, name, dark_src, light_src, light_pinned_300):
    title = name.replace("-", " ").title()
    src = f"omarchy `{dark_src}`" + (f" + `{light_src}` palettes" if light_src else " palette (light half synthesized)")
    pinned = set(PINNED_BASE)
    if light_pinned_300:
        pinned.add("base-300")
    if not light_src:
        pinned.discard("paper")
    lines = [
        f"# {title} theme for Hudu",
        "",
        f"Hudu skin generated from the {src} via [`tools/omarchy-port`](../../tools/omarchy-port/). Light + dark mode.",
        "",
        "<!-- TODO: add upstream palette credit + link -->",
        "",
        "## Palette",
        "",
        "**Base** — • marks values taken verbatim from the source palette; the rest are OKLab-interpolated.",
        "",
        "| Token | Hex | Light | Dark |",
        "|-------|-----|-------|------|",
    ]
    for tok, light_role, dark_role in BASE_ROLES:
        mark = " •" if tok in pinned else ""
        lines.append(f"| {tok}{mark} | {_swatch(tokens[tok])} | {light_role} | {dark_role} |")
    lines += [
        "",
        "**Accents** — 600 = light mode, 400 = dark mode. Orange and purple have no ANSI slot in the source palette; they are blends of red+yellow and blue+magenta.",
        "",
        "| Color | 600 (light) | 400 (dark) |",
        "|-------|-------------|------------|",
    ]
    for fam in ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]:
        mark = " (derived)" if fam in DERIVED_FAMILIES else ""
        lines.append(f"| {fam.title()}{mark} | {_swatch(tokens[f'{fam}-600'])} | {_swatch(tokens[f'{fam}-400'])} |")
    lines += [
        "",
        "## Install",
        "",
        "Paste [`theme.css`](theme.css) into Hudu's custom CSS field (Admin → Design → Custom CSS), save, hard-refresh.",
        "",
        "## Source",
        "",
        f"- Generated by [`port_theme.py`](../../tools/omarchy-port/port_theme.py) from the omarchy `{dark_src}` theme"
        + (f" paired with `{light_src}`" if light_src else " (no light variant — light half synthesized)"),
        "- Structure and hand-tuned Hudu fixes inherited from the [Flexoki theme](../flexoki/)",
        "",
    ]
    return "\n".join(lines)


def render(tokens, name, dark_src, light_src):
    template = (Path(__file__).parent / "template.css").read_text()
    unknown = set(re.findall(r"\{\{([a-z0-9-]+)\}\}", template)) - set(tokens)
    if unknown:
        sys.exit(f"template tokens with no value: {sorted(unknown)}")
    body = re.sub(r"\{\{([a-z0-9-]+)\}\}", lambda m: tokens[m.group(1)], template)
    light_note = light_src or "synthesized from dark palette"
    header = (
        "/* ========================================\n"
        f"   {name.upper()} THEME FOR HUDU\n"
        f"   Generated by tools/omarchy-port/port_theme.py\n"
        f"   dark palette: {dark_src} | light palette: {light_note}\n"
        "   ======================================== */\n"
    )
    return header + body


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dark", required=True, help="omarchy theme for the dark half")
    ap.add_argument("--light", help="omarchy theme for the light half")
    ap.add_argument("--name", required=True, help="output theme name")
    ap.add_argument("--out", help="output dir (default themes/<name>/)")
    args = ap.parse_args()

    dark_dir = resolve_theme(args.dark)
    dark = load_palette(dark_dir)
    if not is_dark(dark):
        sys.exit(f"{dark_dir.name} does not look like a dark theme (bg lighter than fg)")

    black = dark["background"]
    if args.light:
        light_dir = resolve_theme(args.light)
        light = load_palette(light_dir)
        if is_dark(light):
            sys.exit(f"{light_dir.name} does not look like a light theme")
        paper = light["background"]
        light_src = light_dir.name
    else:
        light, paper, light_src = None, synth_light_bg(black), None

    cal = calibrate()
    tokens = build_base_ramp(paper, black, dark, light)
    enforce_text_floors(tokens, paper, black)
    tokens.update(build_accent_ramps(dark, paper, black, cal, light))

    out_dir = Path(args.out) if args.out else Path(__file__).resolve().parents[2] / "themes" / args.name
    out_dir.mkdir(parents=True, exist_ok=True)
    css = render(tokens, args.name, dark_dir.name, light_src)
    (out_dir / "theme.css").write_text(css)
    print(f"wrote {out_dir / 'theme.css'} ({len(css.encode())} bytes)")
    readme_path = out_dir / "README.md"
    if readme_path.exists():
        print(f"{readme_path} exists — left untouched (delete it to regenerate)")
    else:
        readme = render_readme(tokens, args.name, dark_dir.name, light_src,
                               light_pinned_300=bool(light and "color7" in light))
        readme_path.write_text(readme)
        print(f"wrote {readme_path} — fill in the upstream palette credit TODO")
    if not args.light:
        print("note: light mode synthesized from the dark palette — pair a real light theme with --light for better results")


if __name__ == "__main__":
    main()
