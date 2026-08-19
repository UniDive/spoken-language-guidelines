---
layout: base
title: 'Issue draft: Bororo BDT'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Bororo BDT](../treebanks/UD_Bororo-BDT.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Bororo-BDT](https://github.com/UniversalDependencies/UD_Bororo-BDT)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Bororo-BDT`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?
This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (a weak signal):

**Finding:** Possibly identifiable via a naming pattern in `document_id`.

**Evidence:** Only `document_id`, `sent_id`, and `text` exist - no genre, source, or modality field at all. Of the 43 `document_id` values, ~17 match biblical book names (`samuel_1_2`, `reis_1_2` = Kings, `esdras_2` = Ezra, `oseias_2` = Hosea, `genesis_2`, `levitico_2`, `daniel_2`, `novo_testamento_ochoa`, etc.) - almost certainly translated scripture, i.e. written; the remaining ~26 look like oral narratives/rituals (`oieigo_*`, `coqueiro01`-`coqueiro09`, `historia_mitica_bor`, `rituais_bororo`, `bokodori_ecerae`, `juko_ro`) - plausibly spoken fieldwork material, matching the README's description of "mythological narratives, fieldwork material (elicited and spontaneous discourse)".

**Suggestion:** Add `# modality = written` to the ~17 biblical documents and `# modality = spoken` to the narrative/ritual ones - please confirm, since this was inferred from document naming rather than an explicit tag.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

We found a data-quality issue while checking `document_id`: 4 of the 43 values are not real identifiers - they're leaked local Windows file paths (e.g. `G:\Mi unidad\hiwi\tasks_materials\...\ipare_ereru_(...)-udpipe.txt`, with corrupted/mojibake characters in 2 of them). Two of these duplicate a document that also exists under a clean id (`ipare_ereru`, `oieigo_de_danca_2`) - could you confirm whether the same document is present twice under two different ids, and clean up the leaked file paths?

### Implementation notes

**Quick search & replace**
- None - all items here are inferences from document naming or data-quality issues, not confirmed mappings.

**Needs a small script**
- Once the spoken/written split is confirmed (see below), tagging is a one-line run:
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality DIR \
      --spoken-if '(oieigo|coqueiro|historia_mitica_bor|rituais_bororo|bokodori_ecerae|juko_ro)' \
      --written-if '.' --write
  ```
  Dry-running the "obvious" biblical-name pattern (`samuel|reis|esdras|oseias|genesis|levitico|daniel|novo_testamento`) against the real `train` split leaves several more `document_id`s unmatched that are *also* clearly biblical books (`naum_e_habacuc_2`, `ageu_2`, `baruc_2`, `jeremias_2`, `judite_e_ester_2`, `deuteronomio_2`, `jonas_2`) - a catch-all `--written-if '.'` (default-to-written) as above is safer than trying to enumerate every book name, but confirm with maintainers first since this is exactly the inference the draft flags as unconfirmed.

**Needs manual input from maintainers**
- Confirm the spoken/written split inferred from `document_id` naming (see above) before running `tag-modality --write`.
- The leaked Windows file-path `document_id`s (4 of 43, e.g. `G:\Mi unidad\hiwi\...\ipare_ereru_(...)-udpipe.txt`) and the 2 duplicate documents they may represent (`ipare_ereru`, `oieigo_de_danca_2`) need maintainer confirmation before any cleanup script touches them - deleting/merging documents isn't something to automate without sign-off. There's also one further unmatched, non-obviously-biblical id (`boe_readodae`) worth asking about explicitly.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
