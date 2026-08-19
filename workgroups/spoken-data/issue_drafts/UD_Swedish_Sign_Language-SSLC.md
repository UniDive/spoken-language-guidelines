---
layout: base
title: 'Issue draft: Swedish_Sign_Language SSLC'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Swedish_Sign_Language SSLC](../treebanks/UD_Swedish_Sign_Language-SSLC.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Swedish_Sign_Language-SSLC](https://github.com/UniversalDependencies/UD_Swedish_Sign_Language-SSLC)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Swedish_Sign_Language-SSLC`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

No `document_id` exists, but it can be derived directly from the `sent_id` prefix: `sent_id` follows `<doc-id>:<start>:<end>` (e.g. `SSLC01_104:1:2`), with 6 distinct document ids (`SSLC01_104`, `SSLC01_320`, `SSLC01_391`, `SSLC02_331`, `SSLC02_332`, `SSLC02_409`).

| Field | Suggestion                                                                       |
| ----- | -------------------------------------------------------------------------------- |
| —     | derive `# document_id` from the `sent_id` prefix (everything before the first `:`) |

### Implementation notes

- **Needs a small script:** derive `# document_id` from the `sent_id` prefix using the already-written helper script `workgroups/spoken-data/scripts/harmonize_metadata.py`:
  ```
  python3 workgroups/spoken-data/scripts/harmonize_metadata.py derive-document-id \
      UD_Swedish_Sign_Language-SSLC --pattern '^(?P<doc>[^:]+):.*$' --write
  ```
  Verified against the local clone (`swl_sslc-ud-test.conllu`, dry-run): correctly derives all 6 documents (`SSLC01_104`, `SSLC01_320`, `SSLC01_391`, `SSLC02_331`, `SSLC02_332`, `SSLC02_409`) with no unmatched `sent_id`s.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
