---
layout: base
title: 'Issue draft: Skolt_Sami Giellagas'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Skolt_Sami Giellagas](../treebanks/UD_Skolt_Sami-Giellagas.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Skolt_Sami-Giellagas](https://github.com/UniversalDependencies/UD_Skolt_Sami-Giellagas)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Skolt_Sami-Giellagas`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material, and it turns out this aligns exactly with the file split:

**Finding:** Per the README, the corpus "originally consists of twenty translated sentences ... made by Hilkka Fofonoff from the Finnish texts", with all subsequent sentences from the Giellagas Corpus of Spoken Saami Languages. This matches the data exactly: `sms_giellagas-ud-train.conllu` contains exactly those 20 sentences (`sent_id` prefix `FofonoffHilkka_brat_2018`) - written, translated from Finnish. `sms_giellagas-ud-test.conllu` contains the remaining 241 sentences - spoken, drawn from field recordings (`sent_id` prefixes like `11308_1a::<timestamp>`, `NA2_00635_1az::<timestamp>`) and published transcriptions of recorded speech (`kotus-skak2010-*`).

**Suggestion:** Add `# modality = written` to `train` sentences and `# modality = spoken` to `test` sentences. One caveat: a handful of `test` sentences (`SK2020-*`, `SKKV2020:*`) are grammar-book examples rather than recordings - could you confirm whether these should also count as spoken?

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `document_id` exists, but it can be derived from the source-identifier prefix of `sent_id` (the part before the timestamp/counter suffix), e.g. `11308_1a` and `NA2_00635_1az` (recordings), `kotus-skak2010-1-1` (published transcription), `SK2020`, `SKKV2020`, `Juutinen2023`, `FofonoffHilkka_brat_2018` (other sources). The exact delimiter varies by source (`::` before timestamps, `:`/`-` before a numeric counter otherwise) - please confirm the intended document granularity.

| Field | Suggestion                                                       |
| ----- | ---------------------------------------------------------------- |
| —     | derive `# document_id` from the `sent_id` source-identifier prefix |

### 3. Sentence-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#sentence-level))

`aannotation` (likely a typo for "annotation") packs three XML-style attributes into one comment line: `# aannotation="yes" begintime="0:39:13" endtime="0:09:18"` (`endtime` is sometimes empty). `sound_alignment_begin`/`sound_alignment_end` are specified in milliseconds, so `begintime`/`endtime` (currently `H:MM:SS`) need converting, not just copying.

| Field                       | Suggestion                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aannotation` (`begintime`) | convert `H:MM:SS` to milliseconds, split into `sound_alignment_begin`                                                                             |
| `aannotation` (`endtime`)   | convert `H:MM:SS` to milliseconds, split into `sound_alignment_end` (when present); derive `duration` (ms) from begin/end when both are available |
| `text_fi`                   | OK (ISO 639-1 two-letter code)                                                                                  |
| `text_en`                   | OK (ISO 639-1 two-letter code)                                                                                  |
| `text_olo`                  | unsure - could you clarify what this field represents?                                                                                            |
| `text_mdf`                  | unsure - could you clarify what this field represents?                                                                                            |

### Implementation notes

**Quick search & replace**
- `text_fi` and `text_en` already use ISO 639-1 two-letter codes - no rename needed.

**Needs a small script**
- `# modality` tagging by file (`train` = written, `test` = spoken): a two-line shell loop is enough (`harmonize_metadata.py` has no per-file constant-value mode, since this isn't derived from a field) - e.g. insert `# modality = written` after every `# sent_id` in `*-train.conllu` and `# modality = spoken` in `*-test.conllu`. Simple, but hold off on the `test` file until the grammar-book-example caveat below is resolved.
- `aannotation` → split + convert: confirmed format is `# aannotation="yes" begintime="0:39:13" endtime="0:01:36"` (XML-style, `endtime` sometimes empty) - not a plain `key = value` comment, so neither `split-field` nor `rename-comment` apply. Needs a ~15-line custom script: regex-match `begintime="(?P<b>[\d:]+)"\s+endtime="(?P<e>[\d:]*)"`, convert `H:MM:SS` → milliseconds, emit `# sound_alignment_begin = <ms>` and (when `endtime` is non-empty) `# sound_alignment_end = <ms>` + computed `# duration = <ms>`.
- `# document_id` derivation from the `sent_id` source prefix: mechanically similar to `derive-document-id`, but the delimiter differs by source (`::` before a timestamp for recordings, e.g. `11308_1a::0:01:32-0:01:36` → doc `11308_1a`; `-`/`:` before a numeric counter for other sources) - a single regex won't cleanly cover both, so this needs a small script with 2-3 source-specific patterns rather than one `derive-document-id --pattern` call. Confirm document granularity first (see below).

**Needs manual input from maintainers**
- Whether `SK2020-*`/`SKKV2020:*` grammar-book examples (in the `test` file) should count as `modality = spoken` alongside the real recordings.
- The intended document granularity/delimiter convention for deriving `document_id` (varies by source, as above).
- `text_olo`, `text_mdf` - unclear fields, need clarification before any rename.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
