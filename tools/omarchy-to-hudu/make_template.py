#!/usr/bin/env python3
"""Regenerate template.css from themes/flexoki/theme.css.

Replaces every Flexoki palette hex (case-insensitive) with a {{token}}
placeholder. Hudu's stock-color attribute matchers (e.g. [style*="#300c83"])
are not palette colors, so they pass through literally.

Run from the repo root whenever theme.css changes:
    python3 tools/omarchy-to-hudu/make_template.py
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from flexoki_palette import hex_to_token

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "themes/flexoki/theme.css"
DST = Path(__file__).parent / "template.css"


def main() -> None:
    css = SRC.read_text()
    tokens = hex_to_token()
    # Drop the Flexoki palette-reference header; the generated theme gets
    # its own header from port_theme.py.
    marker = "======================================== */\n"
    body = css.split(marker, 1)[1]

    replaced = set()

    def sub(m: re.Match) -> str:
        h = m.group(0).upper()
        if h in tokens:
            replaced.add(tokens[h])
            return "{{" + tokens[h] + "}}"
        return m.group(0)

    out = re.sub(r"#[0-9a-fA-F]{6}\b", sub, body)
    # Comments narrate the source theme by name; generated themes should not
    # introduce themselves as Flexoki (users copy these files into Hudu).
    out = out.replace("FLEXOKI", "PALETTE").replace("Flexoki", "palette").replace("flexoki", "palette")
    # The dashboard chart is a canvas painted in a server-baked Tailwind blue;
    # the hand-made theme uses a hand-tuned static filter. Generated themes get
    # a per-palette filter computed by port_theme.py.
    out = out.replace("filter: saturate(0.55) brightness(0.62) !important;",
                      "filter: {{chart-filter}} !important;")
    DST.write_text(out)

    leftover = sorted({h.upper() for h in re.findall(r"#[0-9a-fA-F]{6}\b", out)})
    print(f"template.css written: {len(replaced)} distinct tokens")
    print(f"literal hexes kept (Hudu stock matchers + comments): {len(leftover)}")
    for h in leftover:
        print(f"  {h}")


if __name__ == "__main__":
    main()
