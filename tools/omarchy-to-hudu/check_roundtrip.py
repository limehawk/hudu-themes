#!/usr/bin/env python3
"""Round-trip sanity check for port_theme.py.

Ports flexoki-dark + flexoki-light and compares against the hand-made
themes/flexoki/theme.css. Pinned tokens (anchors, text tiers, ANSI 400/600
accents) must match exactly; derived intermediates may drift within a
perceptual tolerance (interpolation is calibrated, not copied).

Run from the repo root:
    python3 tools/omarchy-to-hudu/check_roundtrip.py
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from port_theme import delta_e

REPO = Path(__file__).resolve().parents[2]

# Tokens copied verbatim from the source palettes — must survive the trip.
PINNED = {
    "#100F0F", "#FFFCF0", "#CECDC3", "#878580", "#6F6E69", "#B7B5AC",
    "#AF3029", "#D14D41", "#66800B", "#879A39", "#AD8301", "#D0A215",
    "#205EA6", "#4385BE", "#A02F6F", "#CE5D97", "#24837B", "#3AA99F",
}
DERIVED_TOLERANCE = 6.0  # OKLab dE x100; worst observed is purple-600 at 5.8


def hexes(css: str) -> list[str]:
    body = css.split("======================================== */\n", 1)[1]
    return re.findall(r"#[0-9a-fA-F]{6}\b", body)


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            [sys.executable, str(Path(__file__).parent / "port_theme.py"),
             "--dark", "flexoki-dark", "--light", "flexoki-light",
             "--name", "flexoki-roundtrip", "--out", tmp],
            check=True, capture_output=True,
        )
        gen = hexes((Path(tmp) / "theme.css").read_text())
    orig = hexes((REPO / "themes/flexoki/theme.css").read_text())

    if len(orig) != len(gen):
        sys.exit(f"FAIL: structure mismatch ({len(orig)} vs {len(gen)} hex positions)")

    pin_violations, drift_violations, worst = [], [], 0.0
    for a, b in zip(orig, gen):
        d = delta_e(a, b)
        worst = max(worst, d)
        if a.upper() in PINNED and d > 0.01:
            pin_violations.append((a, b))
        elif d > DERIVED_TOLERANCE:
            drift_violations.append((a, b, d))

    if pin_violations or drift_violations:
        for a, b in pin_violations:
            print(f"PINNED token changed: {a} -> {b}")
        for a, b, d in drift_violations:
            print(f"derived token drifted past tolerance: {a} -> {b} (dE {d:.1f})")
        sys.exit("FAIL")
    print(f"PASS: {len(orig)} positions, pinned exact, max derived drift dE {worst:.1f} (tolerance {DERIVED_TOLERANCE})")


if __name__ == "__main__":
    main()
