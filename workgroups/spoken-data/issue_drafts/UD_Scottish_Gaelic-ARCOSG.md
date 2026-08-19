---
layout: base
title: 'Issue draft: Scottish_Gaelic ARCOSG'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Scottish_Gaelic ARCOSG](../treebanks/UD_Scottish_Gaelic-ARCOSG.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG](https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Scottish_Gaelic-ARCOSG`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. The README is explicit about this, though:

**Finding:** The 8 subcorpora are identifiable via the letter prefix of `document_id` (`<letters><digits>`, e.g. `c03`, `f08`, `fp09`, `n02`, `ns06`): `c` (Conversation - interview transcripts), `s` (Sport - radio commentary), `n` (Oral narrative), `ns` (News scripts, radio), `p` (Public interview/discussion, radio) are spoken; `f` (Fiction), `fp` (Formal prose), `pw` (Popular writing/newspaper columns) are written.

**Suggestion:** Add `# modality = spoken` to documents whose `document_id` prefix is `c`, `s`, `n`, `ns`, or `p`; `# modality = written` for `f`, `fp`, `pw`.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

Per the README, each spoken subcorpus also has a fairly clear genre and interaction profile:

| `document_id` prefix | Subcorpus                                                                  | `# genre`                                                 | Interaction parameters                                                                                                                                     |
| ------------------ | -------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `c`                | Conversation (interviews, Western Isles, 1998-2000)                        | `interview`                                               | `degree_of_spontaneity = unplanned`, `number_of_participants = dialogic`, `context = private`, `setting = face-to-face`, `symmetry = asymmetric`           |
| `s`                | Sport (*Radio nan Gàidheal* match commentary)                              | `commentary`                                              | `degree_of_spontaneity = unplanned`, `number_of_participants = monologic`, `context = public`, `setting = broadcast`                                       |
| `n`                | Oral narrative (traditional stories)                                       | `narrative`                                               | `degree_of_spontaneity = planned`, `number_of_participants = monologic`, `context = public`, `setting = face-to-face`                                      |
| `ns`               | News scripts (*Radio nan Gàidheal*, early 1990s)                           | `radio show` (or `speech`)                                | `degree_of_spontaneity = planned` (scripted), `number_of_participants = monologic`, `context = public`, `setting = broadcast`                              |
| `p`                | Public interview/discussion (radio programmes, incl. political discussion) | `interview` (or `discussion` for the political programme) | `degree_of_spontaneity = unplanned`, `number_of_participants = dialogic`/`multi-party`, `context = public`, `setting = broadcast`, `symmetry = asymmetric` |

Please confirm these against your own understanding - especially `number_of_participants`/`symmetry` for `p` documents, which vary between two-person interviews and a multi-party political discussion programme (`p06`, *Bonn Comhraidh*).

### 3. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion             |
| --------- | ---------------------- |
| `speaker` | change to `speaker_id` |

### Implementation notes

**Quick search & replace**
- `speaker` → `speaker_id`: `python3 workgroups/spoken-data/scripts/harmonize_metadata.py rename-comment DIR --map speaker=speaker_id --write` (values like `[1]`, `[2]` confirmed in the real data - purely a key rename, no reformatting needed).

**Needs a small script**
- `# modality` tagging from `document_id` prefix (`# document_id` already exists in the released files, e.g. `c02`, `f01`): `python3 workgroups/spoken-data/scripts/harmonize_metadata.py tag-modality DIR --spoken-if '^(c|s|n|ns|p)[0-9]' --written-if '^(f|fp|pw)[0-9]' --write` — note `n` vs `ns` and `f` vs `fp` need the digit boundary in the regex (as above) so `n02` doesn't also match the `ns` written/spoken split incorrectly; double-check against the full prefix list before running with `--write`.
- The per-subcorpus `# genre` and interaction-parameter block (table above) is a fixed lookup by `document_id` prefix - once confirmed, a ~20-line script keyed on the same prefix regexes as `tag-modality` can insert all of `genre`, `degree_of_spontaneity`, `number_of_participants`, `context`, `setting`, `symmetry` in one pass (not covered by the current subcommands, which only handle a single field at a time).

**Needs manual input from maintainers**
- `number_of_participants`/`symmetry` for `p` documents specifically (mixed two-person interviews and one multi-party programme, `p06`) - needs per-document review, not a blanket prefix rule.
- Confirm the full genre/interaction-parameter table before running the script above.

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
