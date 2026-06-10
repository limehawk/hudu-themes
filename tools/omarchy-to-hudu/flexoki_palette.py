"""Flexoki extended palette reference (Stephan Ango, MIT).

Single source of truth for the hex -> token mapping used by both
make_template.py (template generation) and port_theme.py (ramp-fraction
calibration). Mirrors the palette table in themes/flexoki/theme.css.
"""

STEPS = [50, 100, 150, 200, 300, 400, 500, 600, 700, 800, 850, 900, 950]

RAMPS = {
    "base":    "#F2F0E5 #E6E4D9 #DAD8CE #CECDC3 #B7B5AC #9F9D96 #878580 #6F6E69 #575653 #403E3C #343331 #282726 #1C1B1A",
    "red":     "#FFE1D5 #FFCABB #FDB2A2 #F89A8A #E8705F #D14D41 #C03E35 #AF3029 #942822 #6C201C #551B18 #3E1715 #261312",
    "orange":  "#FFE7CE #FED3AF #FCC192 #F9AE77 #EC8B49 #DA702C #CB6120 #BC5215 #9D4310 #71320D #59290D #40200D #27180E",
    "yellow":  "#FAEEC6 #F6E2A0 #F1D67E #ECCB60 #DFB431 #D0A215 #BE9207 #AD8301 #8E6B01 #664D01 #503D02 #3A2D04 #241E08",
    "green":   "#EDEECF #DDE2B2 #CDD597 #BEC97E #A0AF54 #879A39 #768D21 #66800B #536907 #3D4C07 #313D07 #252D09 #1A1E0C",
    "cyan":    "#DDF1E4 #BFE8D9 #A2DECE #87D3C3 #5ABDAC #3AA99F #2F968D #24837B #1C6C66 #164F4A #143F3C #122F2C #101F1D",
    "blue":    "#E1ECEB #C6DDE8 #ABCFE2 #92BFDB #66A0C8 #4385BE #3171B2 #205EA6 #1A4F8C #163B66 #133051 #12253B #101A24",
    "purple":  "#F0EAEC #E2D9E9 #D3CAE6 #C4B9E0 #A699D0 #8B7EC8 #735EB5 #5E409D #4F3685 #3C2A62 #31234E #261C39 #1A1623",
    "magenta": "#FEE4E5 #FCCFDA #F9B9CF #F4A4C2 #E47DA8 #CE5D97 #B74583 #A02F6F #87285E #641F46 #4F1B39 #39172B #24131D",
}

ANCHORS = {"paper": "#FFFCF0", "black": "#100F0F"}


def hex_to_token() -> dict[str, str]:
    """Uppercase hex -> token name (e.g. '#D14D41' -> 'red-400')."""
    out = {h.upper(): name for name, h in ANCHORS.items()}
    for family, hexes in RAMPS.items():
        for step, h in zip(STEPS, hexes.split()):
            out[h.upper()] = f"{family}-{step}"
    return out


def token_to_hex() -> dict[str, str]:
    return {tok: h for h, tok in hex_to_token().items()}
