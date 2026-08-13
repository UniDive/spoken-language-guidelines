---
layout: base
title: 'Issue draft: Scottish_Gaelic ARCOSG'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Scottish_Gaelic ARCOSG](../treebanks/UD_Scottish_Gaelic-ARCOSG.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG](https://github.com/UniversalDependencies/UD_Scottish_Gaelic-ARCOSG)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Scottish_Gaelic-ARCOSG`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus.

### 1. Is the spoken portion identifiable?

This treebank mixes spoken and written material but its `.conllu` files don't explicitly mark which sentences are spoken. The README is explicit about this, though:

**Finding:** The 8 subcorpora are identifiable via the letter prefix of `newdoc id` (`<letters><digits>`, e.g. `c03`, `f08`, `fp09`, `n02`, `ns06`): `c` (Conversation - interview transcripts), `s` (Sport - radio commentary), `n` (Oral narrative), `ns` (News scripts, radio), `p` (Public interview/discussion, radio) are spoken; `f` (Fiction), `fp` (Formal prose), `pw` (Popular writing/newspaper columns) are written.

**Suggestion:** Add `# modality = spoken` to documents whose `newdoc id` prefix is `c`, `s`, `n`, `ns`, or `p`; `# modality = written` for `f`, `fp`, `pw`.

### 2. Document-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#document-level))

Per the README, each spoken subcorpus also has a fairly clear genre and interaction profile:

| `newdoc id` prefix | Subcorpus                                                                  | `# genre`                                                 | Interaction parameters                                                                                                                                     |
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

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
