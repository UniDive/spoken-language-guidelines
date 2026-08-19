---
layout: base
title: 'Czech PDTC'
udver: '2'
---

# Czech PDTC

[Back to index](../ud_spoken_treebanks.html)

## Overview

| | |
|---|---|
| **type** | mixed |
| **available since** | 1.0 |
| **link** | [https://github.com/UniversalDependencies/UD_Czech-PDTC](https://github.com/UniversalDependencies/UD_Czech-PDTC) |
| **genre** | news reviews nonfiction academic spoken social |
| **contributors** | Zeman, Daniel; Hajič, Jan; Bémová, Alevtina; Buráňová, Eva; Hajičová, Eva; Havelka, Jiří; Hlaváčová, Jaroslava; Kárník, Jiří; Kolářová, Veronika; Kučová, Lucie; Lopatková, Markéta; Mikulová, Marie; Mírovský, Jiří; Nedoluzhko, Anna; Novák, Michal; Pajas, Petr; Panevová, Jarmila; Sgall, Petr; Straka, Milan; Ševčíková, Magda; Štěpánek, Jan; Štěpánková, Barbora; Urešová, Zdeňka; Vidová Hladká, Barbora; Žabokrtský, Zdeněk |
| **sentences** | 213897 |
| **tokens** | 3432078 |

**Issue draft:** [UD_Czech-PDTC](../issue_drafts/UD_Czech-PDTC.html)

## Modality identification

**Is spoken part clearly identifiable?** yes - via the `document_id` prefix `pdtsc` (not "sentences starting with `s`" as mentioned in the README. The actual `document_id`/`sent_id` values spell it out in full, e.g. `pdtsc_jg-27638_04.00`).

**Advise:** add `# modality = spoken` to the 1553 sentences (documents) with `document_id` starting `pdtsc`, and `# modality = written` to the rest.