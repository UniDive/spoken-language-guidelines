---
layout: base
title: 'Bororo BDT'
udver: '2'
---

# Bororo BDT

[Back to index](ud_spoken_treebanks.html)

## Overview

| | |
| --- | --- |
| **type** | mixed |
| **available since** | 2.12 |
| **link** | [https://github.com/UniversalDependencies/UD_Bororo-BDT](https://github.com/UniversalDependencies/UD_Bororo-BDT) |
| **genre** | grammar-examples spoken nonfiction bible |
| **contact** | <fabricio.gerardi@uni-tuebingen.de> |
| **sentences** | 21384 |
| **tokens** | 160356 |

**Issue draft:** [UD_Bororo-BDT](../issue_drafts/UD_Bororo-BDT.html)

## Modality identification

**Is spoken part clearly identifiable?** possibly - via a naming pattern in `newdoc id`: the 43 `newdoc id` values themselves split into two groups: ~17 match biblical book names, the remaining ~26 look like oral narratives/rituals (`oieigo_*`, `coqueiro01`-`coqueiro09`, `historia_mitica_bor`, `rituais_bororo`, `bokodori_ecerae`, `juko_ro`) - plausibly **spoken** fieldwork material, matching the README's description

**Data-quality issue found:** 4 of the 43 `newdoc id` values are not real identifiers - they're leaked local Windows file paths (e.g. `G:\Mi unidad\hiwi\tasks_materials\...\ipare_ereru_(...)-udpipe.txt`).
