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

```
             50       100      150      200      300      400      500      600      700      800      850      900      950
Base      #F2F0E5  #E6E4D9  #DAD8CE  #CECDC3  #B7B5AC  #9F9D96  #878580  #6F6E69  #575653  #403E3C  #343331  #282726  #1C1B1A
Red       #FFE1D5  #FFCABB  #FDB2A2  #F89A8A  #E8705F  #D14D41  #C03E35  #AF3029  #942822  #6C201C  #551B18  #3E1715  #261312
Orange    #FFE7CE  #FED3AF  #FCC192  #F9AE77  #EC8B49  #DA702C  #CB6120  #BC5215  #9D4310  #71320D  #59290D  #40200D  #27180E
Yellow    #FAEEC6  #F6E2A0  #F1D67E  #ECCB60  #DFB431  #D0A215  #BE9207  #AD8301  #8E6B01  #664D01  #503D02  #3A2D04  #241E08
Green     #EDEECF  #DDE2B2  #CDD597  #BEC97E  #A0AF54  #879A39  #768D21  #66800B  #536907  #3D4C07  #313D07  #252D09  #1A1E0C
Cyan      #DDF1E4  #BFE8D9  #A2DECE  #87D3C3  #5ABDAC  #3AA99F  #2F968D  #24837B  #1C6C66  #164F4A  #143F3C  #122F2C  #101F1D
Blue      #E1ECEB  #C6DDE8  #ABCFE2  #92BFDB  #66A0C8  #4385BE  #3171B2  #205EA6  #1A4F8C  #163B66  #133051  #12253B  #101A24
Purple    #F0EAEC  #E2D9E9  #D3CAE6  #C4B9E0  #A699D0  #8B7EC8  #735EB5  #5E409D  #4F3685  #3C2A62  #31234E  #261C39  #1A1623
Magenta   #FEE4E5  #FCCFDA  #F9B9CF  #F4A4C2  #E47DA8  #CE5D97  #B74583  #A02F6F  #87285E  #641F46  #4F1B39  #39172B  #24131D
```

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
