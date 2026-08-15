---
layout: base
title: 'Issue draft: Czech PDTC'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Czech PDTC](../treebanks/UD_Czech-PDTC.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Czech-PDTC](https://github.com/UniversalDependencies/UD_Czech-PDTC)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Czech-PDTC`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?
This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. We looked for a pattern in the data (fairly confident):

**Finding:** Identifiable via the `newdoc id` prefix `pdtsc`, which names a known spoken sub-corpus.

**Evidence:** `newdoc id` prefixes and counts: `ln` (2906), `wsj` (2312), `pdtsc` (1553), `mf` (1131), `lnd` (712), `cmpr` (372), `vesm` (209), `faust` (60). `pdtsc` is the standard abbreviation for the Prague Dependency Treebank of Spoken Czech (PDT-SC), a known spoken sub-corpus of PDTC; the rest are written-text sources (newspapers, magazines, the Wall Street Journal translation, the Faust MT-testing corpus).

**Suggestion:** Add `# modality = spoken` to all documents whose `newdoc id` starts with `pdtsc`, and `# modality = written` to the rest. Please confirm this reading with the PDTC maintainers, since we inferred it from the corpus name rather than internal documentation.

### 2. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field | Suggestion |
|---|---|
| `global.Entity` | corpus-specific (coreference/entity annotation, project-wide) - keep, not spoken-specific |

### Implementation notes

**Quick search & replace**
- None.

**Needs a small script**
- Once confirmed with maintainers, tagging modality from the `pdtsc` prefix is a single run across the whole repo (confirmed by dry-run: matches 1553 `newdoc id`s starting `pdtsc` across `cs_pdtc-ud-test.conllu`, `cs_pdtc-ud-dev.conllu`, and `cs_pdtc-ud-train-st.conllu`):
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality DIR \
      --spoken-if '^pdtsc' --written-if '.' --write
  ```

**Needs manual input from maintainers**
- Confirm the `pdtsc` → spoken inference with the PDTC maintainers before running `--write` (the draft explicitly flags this as inferred from the corpus name, not documented).
- `global.Entity` is intentionally left as-is (project-wide coreference annotation, not spoken-specific) - no action needed.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
