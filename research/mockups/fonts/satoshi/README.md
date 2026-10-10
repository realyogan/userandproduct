# Satoshi

Typeface by Indian Type Foundry, free under the ITF Free Font License (FFL).

- Source: https://www.fontshare.com/fonts/satoshi (family package from
  https://api.fontshare.com/v2/fonts/download/satoshi, the "Satoshi_Complete" zip)
- Version: 2.000 (font name table: "Version 2.000"; "Copyright 2017-2021 Indian Type Foundry. All rights reserved.")
- Licence: ITF Free Font License, Version 2.0 - 17 Aug 2026, saved here as `FFL.txt`
- Downloaded: 10 October 2026
- Files are exactly as shipped in the package (the licence forbids subsetting or format conversion, so there are
  no Latin-subset copies like the Inter and Fraunces ones).

## What is here

| File | Use |
| --- | --- |
| `Satoshi-Variable.woff2`, `Satoshi-VariableItalic.woff2` | The web files the mockups load (weight axis 300 to 900, so 400, 500, 600, 700 and 900 all come from one file) |
| `Satoshi-Regular/Italic/Medium/MediumItalic/Bold/BoldItalic/Black/BlackItalic.woff2` | Static web files, kept as a fallback option |
| The same eight as `.otf`, plus `Satoshi-Variable.ttf` and `Satoshi-VariableItalic.ttf` | Desktop files for the SVG text-to-path tool and design work |
| `FFL.txt` | The licence text, unchanged |

`option-1/assets/fonts/satoshi/` holds copies of the two variable `.woff2` files and the licence.

## What the licence allows (its own words)

Use, personal and commercial (section 01): "You are hereby granted a non-exclusive, non-assignable,
non-transferable and terminable license to access, download, install, store and use the Font Software for
personal or commercial purposes, free of charge and for an unlimited period of time, subject to the terms of this
License."

Web embedding and self-hosting (section 01): "You may self-host the Font Software on your own servers or
infrastructure for use on your own websites and applications, including through standard webfont technologies
such as CSS @font-face."

Logos (section 01): "You may use the Font Software to create logos, wordmarks, graphic elements, images, vector
files, scalable drawings and other creative works."

No modifying (section 02): "You may not modify, edit, adapt, translate, reverse engineer, decompile, disassemble
or otherwise alter the Font Software or the typeface designs embodied therein, in whole or in part, without the
prior written consent of the Licensor. This includes modifying or replacing glyphs, subsetting, format
conversion, or altering font names, copyright information, ownership information or other metadata."

No selling or redistributing (section 02): "The Font Software may not, beyond the permitted copies and uses
defined herein, be distributed, duplicated, loaned, resold, sublicensed, transferred, donated, given away or
otherwise made available to any other person or entity, whether for free or for a fee. This includes
distributing the Font Software through another font website, font library, marketplace, repository, download
service, application or platform, or by email, removable media, publicly accessible servers, file-sharing
services, peer-to-peer networks or any other means."

No passing the files to contractors (section 02): "You may not provide the Font Software directly to external
designers, agencies, contractors, printers or other service providers. Any third party wishing to use the Font
Software must obtain their own copy directly from Fontshare and be independently bound by this License."

## Git: the files are not committed

The project repository on GitHub is public. The licence names "repository" and "publicly accessible servers" as
forbidden ways of making the files available, so the font files in this folder and in
`option-1/assets/fonts/satoshi/` are listed in `.gitignore`; only this README is tracked. Anyone cloning the repo
gets the files from Fontshare and puts them here. Serving them from our own website through `@font-face` is
allowed (section 01), so the live site can self-host them. The owner decides whether this arrangement changes
(for example by making the repository private).
