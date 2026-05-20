# Flexoki theme for Hudu

Hudu skin using the [Flexoki](https://stephango.com/flexoki) palette by Steph Ango — inky, minimalist color scheme designed for reading & writing on digital screens. Inspired by analog inks + warm paper. Light + dark mode.

Oklab-derived, perceptually balanced across devices. See full design philosophy at [stephango.com/flexoki](https://stephango.com/flexoki).

## Palette

**Base** (warm monochrome) — 8 values per theme: 3 text, 3 interface, 2 background.

| Token | Hex | Light | Dark |
|-------|-----|-------|------|
| black | <img valign='middle' alt='#100F0F' src='https://readme-swatches.vercel.app/100F0F'/> `#100F0F` | tx | bg |
| base-950 | <img valign='middle' alt='#1C1B1A' src='https://readme-swatches.vercel.app/1C1B1A'/> `#1C1B1A` | — | bg-2 |
| base-900 | <img valign='middle' alt='#282726' src='https://readme-swatches.vercel.app/282726'/> `#282726` | — | ui |
| base-850 | <img valign='middle' alt='#343331' src='https://readme-swatches.vercel.app/343331'/> `#343331` | — | ui-2 |
| base-800 | <img valign='middle' alt='#403E3C' src='https://readme-swatches.vercel.app/403E3C'/> `#403E3C` | — | ui-3 |
| base-700 | <img valign='middle' alt='#575653' src='https://readme-swatches.vercel.app/575653'/> `#575653` | — | tx-3 |
| base-600 | <img valign='middle' alt='#6F6E69' src='https://readme-swatches.vercel.app/6F6E69'/> `#6F6E69` | tx-2 | — |
| base-500 | <img valign='middle' alt='#878580' src='https://readme-swatches.vercel.app/878580'/> `#878580` | — | tx-2 |
| base-300 | <img valign='middle' alt='#B7B5AC' src='https://readme-swatches.vercel.app/B7B5AC'/> `#B7B5AC` | tx-3 | — |
| base-200 | <img valign='middle' alt='#CECDC3' src='https://readme-swatches.vercel.app/CECDC3'/> `#CECDC3` | ui-3 | tx |
| base-150 | <img valign='middle' alt='#DAD8CE' src='https://readme-swatches.vercel.app/DAD8CE'/> `#DAD8CE` | ui-2 | — |
| base-100 | <img valign='middle' alt='#E6E4D9' src='https://readme-swatches.vercel.app/E6E4D9'/> `#E6E4D9` | ui | — |
| base-50 | <img valign='middle' alt='#F2F0E5' src='https://readme-swatches.vercel.app/F2F0E5'/> `#F2F0E5` | bg-2 | — |
| paper | <img valign='middle' alt='#FFFCF0' src='https://readme-swatches.vercel.app/FFFCF0'/> `#FFFCF0` | bg | — |

**Accents** (light syntax 600, dark syntax 400)

| Color | 600 | Light | 400 | Dark | Var |
|-------|-----|-------|-----|------|-----|
| Red | <img valign='middle' alt='#AF3029' src='https://readme-swatches.vercel.app/AF3029'/> `#AF3029` | re | <img valign='middle' alt='#D14D41' src='https://readme-swatches.vercel.app/D14D41'/> `#D14D41` | re-2 |
| Orange | <img valign='middle' alt='#BC5215' src='https://readme-swatches.vercel.app/BC5215'/> `#BC5215` | or | <img valign='middle' alt='#DA702C' src='https://readme-swatches.vercel.app/DA702C'/> `#DA702C` | or-2 |
| Yellow | <img valign='middle' alt='#AD8301' src='https://readme-swatches.vercel.app/AD8301'/> `#AD8301` | ye | <img valign='middle' alt='#D0A215' src='https://readme-swatches.vercel.app/D0A215'/> `#D0A215` | ye-2 |
| Green | <img valign='middle' alt='#66800B' src='https://readme-swatches.vercel.app/66800B'/> `#66800B` | gr | <img valign='middle' alt='#879A39' src='https://readme-swatches.vercel.app/879A39'/> `#879A39` | gr-2 |
| Cyan | <img valign='middle' alt='#24837B' src='https://readme-swatches.vercel.app/24837B'/> `#24837B` | cy | <img valign='middle' alt='#3AA99F' src='https://readme-swatches.vercel.app/3AA99F'/> `#3AA99F` | cy-2 |
| Blue | <img valign='middle' alt='#205EA6' src='https://readme-swatches.vercel.app/205EA6'/> `#205EA6` | bl | <img valign='middle' alt='#4385BE' src='https://readme-swatches.vercel.app/4385BE'/> `#4385BE` | bl-2 |
| Purple | <img valign='middle' alt='#5E409D' src='https://readme-swatches.vercel.app/5E409D'/> `#5E409D` | pu | <img valign='middle' alt='#8B7EC8' src='https://readme-swatches.vercel.app/8B7EC8'/> `#8B7EC8` | pu-2 |
| Magenta | <img valign='middle' alt='#A02F6F' src='https://readme-swatches.vercel.app/A02F6F'/> `#A02F6F` | ma | <img valign='middle' alt='#CE5D97' src='https://readme-swatches.vercel.app/CE5D97'/> `#CE5D97` | ma-2 |

**Extended palette** (50–950 ramps per color family)

### Base

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#F2F0E5' src='https://readme-swatches.vercel.app/F2F0E5'/> `#F2F0E5` | <img valign='middle' alt='#E6E4D9' src='https://readme-swatches.vercel.app/E6E4D9'/> `#E6E4D9` | <img valign='middle' alt='#DAD8CE' src='https://readme-swatches.vercel.app/DAD8CE'/> `#DAD8CE` | <img valign='middle' alt='#CECDC3' src='https://readme-swatches.vercel.app/CECDC3'/> `#CECDC3` | <img valign='middle' alt='#B7B5AC' src='https://readme-swatches.vercel.app/B7B5AC'/> `#B7B5AC` | <img valign='middle' alt='#9F9D96' src='https://readme-swatches.vercel.app/9F9D96'/> `#9F9D96` | <img valign='middle' alt='#878580' src='https://readme-swatches.vercel.app/878580'/> `#878580` | <img valign='middle' alt='#6F6E69' src='https://readme-swatches.vercel.app/6F6E69'/> `#6F6E69` | <img valign='middle' alt='#575653' src='https://readme-swatches.vercel.app/575653'/> `#575653` | <img valign='middle' alt='#403E3C' src='https://readme-swatches.vercel.app/403E3C'/> `#403E3C` | <img valign='middle' alt='#343331' src='https://readme-swatches.vercel.app/343331'/> `#343331` | <img valign='middle' alt='#282726' src='https://readme-swatches.vercel.app/282726'/> `#282726` | <img valign='middle' alt='#1C1B1A' src='https://readme-swatches.vercel.app/1C1B1A'/> `#1C1B1A` |

### Red

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#FFE1D5' src='https://readme-swatches.vercel.app/FFE1D5'/> `#FFE1D5` | <img valign='middle' alt='#FFCABB' src='https://readme-swatches.vercel.app/FFCABB'/> `#FFCABB` | <img valign='middle' alt='#FDB2A2' src='https://readme-swatches.vercel.app/FDB2A2'/> `#FDB2A2` | <img valign='middle' alt='#F89A8A' src='https://readme-swatches.vercel.app/F89A8A'/> `#F89A8A` | <img valign='middle' alt='#E8705F' src='https://readme-swatches.vercel.app/E8705F'/> `#E8705F` | <img valign='middle' alt='#D14D41' src='https://readme-swatches.vercel.app/D14D41'/> `#D14D41` | <img valign='middle' alt='#C03E35' src='https://readme-swatches.vercel.app/C03E35'/> `#C03E35` | <img valign='middle' alt='#AF3029' src='https://readme-swatches.vercel.app/AF3029'/> `#AF3029` | <img valign='middle' alt='#942822' src='https://readme-swatches.vercel.app/942822'/> `#942822` | <img valign='middle' alt='#6C201C' src='https://readme-swatches.vercel.app/6C201C'/> `#6C201C` | <img valign='middle' alt='#551B18' src='https://readme-swatches.vercel.app/551B18'/> `#551B18` | <img valign='middle' alt='#3E1715' src='https://readme-swatches.vercel.app/3E1715'/> `#3E1715` | <img valign='middle' alt='#261312' src='https://readme-swatches.vercel.app/261312'/> `#261312` |

### Orange

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#FFE7CE' src='https://readme-swatches.vercel.app/FFE7CE'/> `#FFE7CE` | <img valign='middle' alt='#FED3AF' src='https://readme-swatches.vercel.app/FED3AF'/> `#FED3AF` | <img valign='middle' alt='#FCC192' src='https://readme-swatches.vercel.app/FCC192'/> `#FCC192` | <img valign='middle' alt='#F9AE77' src='https://readme-swatches.vercel.app/F9AE77'/> `#F9AE77` | <img valign='middle' alt='#EC8B49' src='https://readme-swatches.vercel.app/EC8B49'/> `#EC8B49` | <img valign='middle' alt='#DA702C' src='https://readme-swatches.vercel.app/DA702C'/> `#DA702C` | <img valign='middle' alt='#CB6120' src='https://readme-swatches.vercel.app/CB6120'/> `#CB6120` | <img valign='middle' alt='#BC5215' src='https://readme-swatches.vercel.app/BC5215'/> `#BC5215` | <img valign='middle' alt='#9D4310' src='https://readme-swatches.vercel.app/9D4310'/> `#9D4310` | <img valign='middle' alt='#71320D' src='https://readme-swatches.vercel.app/71320D'/> `#71320D` | <img valign='middle' alt='#59290D' src='https://readme-swatches.vercel.app/59290D'/> `#59290D` | <img valign='middle' alt='#40200D' src='https://readme-swatches.vercel.app/40200D'/> `#40200D` | <img valign='middle' alt='#27180E' src='https://readme-swatches.vercel.app/27180E'/> `#27180E` |

### Yellow

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#FAEEC6' src='https://readme-swatches.vercel.app/FAEEC6'/> `#FAEEC6` | <img valign='middle' alt='#F6E2A0' src='https://readme-swatches.vercel.app/F6E2A0'/> `#F6E2A0` | <img valign='middle' alt='#F1D67E' src='https://readme-swatches.vercel.app/F1D67E'/> `#F1D67E` | <img valign='middle' alt='#ECCB60' src='https://readme-swatches.vercel.app/ECCB60'/> `#ECCB60` | <img valign='middle' alt='#DFB431' src='https://readme-swatches.vercel.app/DFB431'/> `#DFB431` | <img valign='middle' alt='#D0A215' src='https://readme-swatches.vercel.app/D0A215'/> `#D0A215` | <img valign='middle' alt='#BE9207' src='https://readme-swatches.vercel.app/BE9207'/> `#BE9207` | <img valign='middle' alt='#AD8301' src='https://readme-swatches.vercel.app/AD8301'/> `#AD8301` | <img valign='middle' alt='#8E6B01' src='https://readme-swatches.vercel.app/8E6B01'/> `#8E6B01` | <img valign='middle' alt='#664D01' src='https://readme-swatches.vercel.app/664D01'/> `#664D01` | <img valign='middle' alt='#503D02' src='https://readme-swatches.vercel.app/503D02'/> `#503D02` | <img valign='middle' alt='#3A2D04' src='https://readme-swatches.vercel.app/3A2D04'/> `#3A2D04` | <img valign='middle' alt='#241E08' src='https://readme-swatches.vercel.app/241E08'/> `#241E08` |

### Green

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#EDEECF' src='https://readme-swatches.vercel.app/EDEECF'/> `#EDEECF` | <img valign='middle' alt='#DDE2B2' src='https://readme-swatches.vercel.app/DDE2B2'/> `#DDE2B2` | <img valign='middle' alt='#CDD597' src='https://readme-swatches.vercel.app/CDD597'/> `#CDD597` | <img valign='middle' alt='#BEC97E' src='https://readme-swatches.vercel.app/BEC97E'/> `#BEC97E` | <img valign='middle' alt='#A0AF54' src='https://readme-swatches.vercel.app/A0AF54'/> `#A0AF54` | <img valign='middle' alt='#879A39' src='https://readme-swatches.vercel.app/879A39'/> `#879A39` | <img valign='middle' alt='#768D21' src='https://readme-swatches.vercel.app/768D21'/> `#768D21` | <img valign='middle' alt='#66800B' src='https://readme-swatches.vercel.app/66800B'/> `#66800B` | <img valign='middle' alt='#536907' src='https://readme-swatches.vercel.app/536907'/> `#536907` | <img valign='middle' alt='#3D4C07' src='https://readme-swatches.vercel.app/3D4C07'/> `#3D4C07` | <img valign='middle' alt='#313D07' src='https://readme-swatches.vercel.app/313D07'/> `#313D07` | <img valign='middle' alt='#252D09' src='https://readme-swatches.vercel.app/252D09'/> `#252D09` | <img valign='middle' alt='#1A1E0C' src='https://readme-swatches.vercel.app/1A1E0C'/> `#1A1E0C` |

### Cyan

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#DDF1E4' src='https://readme-swatches.vercel.app/DDF1E4'/> `#DDF1E4` | <img valign='middle' alt='#BFE8D9' src='https://readme-swatches.vercel.app/BFE8D9'/> `#BFE8D9` | <img valign='middle' alt='#A2DECE' src='https://readme-swatches.vercel.app/A2DECE'/> `#A2DECE` | <img valign='middle' alt='#87D3C3' src='https://readme-swatches.vercel.app/87D3C3'/> `#87D3C3` | <img valign='middle' alt='#5ABDAC' src='https://readme-swatches.vercel.app/5ABDAC'/> `#5ABDAC` | <img valign='middle' alt='#3AA99F' src='https://readme-swatches.vercel.app/3AA99F'/> `#3AA99F` | <img valign='middle' alt='#2F968D' src='https://readme-swatches.vercel.app/2F968D'/> `#2F968D` | <img valign='middle' alt='#24837B' src='https://readme-swatches.vercel.app/24837B'/> `#24837B` | <img valign='middle' alt='#1C6C66' src='https://readme-swatches.vercel.app/1C6C66'/> `#1C6C66` | <img valign='middle' alt='#164F4A' src='https://readme-swatches.vercel.app/164F4A'/> `#164F4A` | <img valign='middle' alt='#143F3C' src='https://readme-swatches.vercel.app/143F3C'/> `#143F3C` | <img valign='middle' alt='#122F2C' src='https://readme-swatches.vercel.app/122F2C'/> `#122F2C` | <img valign='middle' alt='#101F1D' src='https://readme-swatches.vercel.app/101F1D'/> `#101F1D` |

### Blue

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#E1ECEB' src='https://readme-swatches.vercel.app/E1ECEB'/> `#E1ECEB` | <img valign='middle' alt='#C6DDE8' src='https://readme-swatches.vercel.app/C6DDE8'/> `#C6DDE8` | <img valign='middle' alt='#ABCFE2' src='https://readme-swatches.vercel.app/ABCFE2'/> `#ABCFE2` | <img valign='middle' alt='#92BFDB' src='https://readme-swatches.vercel.app/92BFDB'/> `#92BFDB` | <img valign='middle' alt='#66A0C8' src='https://readme-swatches.vercel.app/66A0C8'/> `#66A0C8` | <img valign='middle' alt='#4385BE' src='https://readme-swatches.vercel.app/4385BE'/> `#4385BE` | <img valign='middle' alt='#3171B2' src='https://readme-swatches.vercel.app/3171B2'/> `#3171B2` | <img valign='middle' alt='#205EA6' src='https://readme-swatches.vercel.app/205EA6'/> `#205EA6` | <img valign='middle' alt='#1A4F8C' src='https://readme-swatches.vercel.app/1A4F8C'/> `#1A4F8C` | <img valign='middle' alt='#163B66' src='https://readme-swatches.vercel.app/163B66'/> `#163B66` | <img valign='middle' alt='#133051' src='https://readme-swatches.vercel.app/133051'/> `#133051` | <img valign='middle' alt='#12253B' src='https://readme-swatches.vercel.app/12253B'/> `#12253B` | <img valign='middle' alt='#101A24' src='https://readme-swatches.vercel.app/101A24'/> `#101A24` |

### Purple

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#F0EAEC' src='https://readme-swatches.vercel.app/F0EAEC'/> `#F0EAEC` | <img valign='middle' alt='#E2D9E9' src='https://readme-swatches.vercel.app/E2D9E9'/> `#E2D9E9` | <img valign='middle' alt='#D3CAE6' src='https://readme-swatches.vercel.app/D3CAE6'/> `#D3CAE6` | <img valign='middle' alt='#C4B9E0' src='https://readme-swatches.vercel.app/C4B9E0'/> `#C4B9E0` | <img valign='middle' alt='#A699D0' src='https://readme-swatches.vercel.app/A699D0'/> `#A699D0` | <img valign='middle' alt='#8B7EC8' src='https://readme-swatches.vercel.app/8B7EC8'/> `#8B7EC8` | <img valign='middle' alt='#735EB5' src='https://readme-swatches.vercel.app/735EB5'/> `#735EB5` | <img valign='middle' alt='#5E409D' src='https://readme-swatches.vercel.app/5E409D'/> `#5E409D` | <img valign='middle' alt='#4F3685' src='https://readme-swatches.vercel.app/4F3685'/> `#4F3685` | <img valign='middle' alt='#3C2A62' src='https://readme-swatches.vercel.app/3C2A62'/> `#3C2A62` | <img valign='middle' alt='#31234E' src='https://readme-swatches.vercel.app/31234E'/> `#31234E` | <img valign='middle' alt='#261C39' src='https://readme-swatches.vercel.app/261C39'/> `#261C39` | <img valign='middle' alt='#1A1623' src='https://readme-swatches.vercel.app/1A1623'/> `#1A1623` |

### Magenta

| 50 | 100 | 150 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 850 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| <img valign='middle' alt='#FEE4E5' src='https://readme-swatches.vercel.app/FEE4E5'/> `#FEE4E5` | <img valign='middle' alt='#FCCFDA' src='https://readme-swatches.vercel.app/FCCFDA'/> `#FCCFDA` | <img valign='middle' alt='#F9B9CF' src='https://readme-swatches.vercel.app/F9B9CF'/> `#F9B9CF` | <img valign='middle' alt='#F4A4C2' src='https://readme-swatches.vercel.app/F4A4C2'/> `#F4A4C2` | <img valign='middle' alt='#E47DA8' src='https://readme-swatches.vercel.app/E47DA8'/> `#E47DA8` | <img valign='middle' alt='#CE5D97' src='https://readme-swatches.vercel.app/CE5D97'/> `#CE5D97` | <img valign='middle' alt='#B74583' src='https://readme-swatches.vercel.app/B74583'/> `#B74583` | <img valign='middle' alt='#A02F6F' src='https://readme-swatches.vercel.app/A02F6F'/> `#A02F6F` | <img valign='middle' alt='#87285E' src='https://readme-swatches.vercel.app/87285E'/> `#87285E` | <img valign='middle' alt='#641F46' src='https://readme-swatches.vercel.app/641F46'/> `#641F46` | <img valign='middle' alt='#4F1B39' src='https://readme-swatches.vercel.app/4F1B39'/> `#4F1B39` | <img valign='middle' alt='#39172B' src='https://readme-swatches.vercel.app/39172B'/> `#39172B` | <img valign='middle' alt='#24131D' src='https://readme-swatches.vercel.app/24131D'/> `#24131D` |

**Mappings**

| Var | UI role | Syntax |
|-----|---------|--------|
| bg | main background | — |
| bg-2 | secondary background | — |
| ui | borders | — |
| ui-2 | hovered borders | — |
| ui-3 | active borders | — |
| tx-3 | faint text | comments |
| tx-2 | muted text | punctuation, operators |
| tx | primary text | — |
| re | error text | invalid, imports |
| or | warning text | functions |
| ye | — | constants |
| gr | success text | keywords |
| cy | links, active states | strings |
| bl | — | variables, attributes |
| pu | — | numbers |
| ma | — | language features |

## Install

Paste [`theme.css`](theme.css) into Hudu's custom CSS field (admin → Settings → Customize Branding).

## References

- Palette © Steph Ango — [stephango.com/flexoki](https://stephango.com/flexoki) (MIT)
- Full design docs: [GitHub](https://github.com/kepano/flexoki)
- Palette reference in [`theme.css`](theme.css) header
