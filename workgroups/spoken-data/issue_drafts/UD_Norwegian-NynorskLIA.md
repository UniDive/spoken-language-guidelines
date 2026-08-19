---
layout: base
title: 'Issue draft: Norwegian NynorskLIA'
udver: '2'
---

# Metadata harmonisation: align spoken-data fields with UniDive naming conventions

[Back to Norwegian NynorskLIA](../treebanks/UD_Norwegian-NynorskLIA.html) &middot; [Back to index](../ud_spoken_treebanks.html)

**Repo:** [https://github.com/UniversalDependencies/UD_Norwegian-NynorskLIA](https://github.com/UniversalDependencies/UD_Norwegian-NynorskLIA)

Cross-posting from the UniDive WG1 T1.5 (spoken language guidelines) metadata harmonisation review. We compared `UD_Norwegian-NynorskLIA`'s current CoNLL-U metadata against the [proposed naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html) (see also the full [treebank status table](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)). This is a suggestion for maintainers to review - feel free to push back on anything that doesn't fit the corpus. The comparison was carried out semi-automatically with the help of Claude (Anthropic); errors or misunderstandings are possible, so please double-check anything unclear.

### 1. Speaker-level ([naming conventions](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/metadata.html#speaker-level))

| Field     | Suggestion                                                                                                                       |
| --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `dialect` | OK as corpus-specific field, but `speaker_id` is currently embedded within it - please split `speaker_id` out into its own field |

### Implementation notes

**Needs a small script**
- `dialect` isn't a standard `# key = value` comment - it packs two labels into one non-standard line, e.g. `# dialect: eidsberg speakerid: eidsberg_uio_03`. The existing `split-field` subcommand only splits the *value* of a single `key = value` comment, so it doesn't apply here directly (11 distinct `speakerid` values confirmed in the corpus). A short custom script is needed:
  ```python
  import re, pathlib
  pat = re.compile(r"^# dialect:\s*(?P<dialect>\S+)\s+speakerid:\s*(?P<speakerid>\S+)\s*$")
  for path in pathlib.Path("DIR").rglob("*.conllu"):
      lines = path.read_text().splitlines(keepends=True)
      for i, line in enumerate(lines):
          m = pat.match(line.rstrip("\n"))
          if m:
              lines[i] = f"# dialect = {m['dialect']}\n# speaker_id = {m['speakerid']}\n"
      path.write_text("".join(lines))
  ```
  (~10 lines; not worth adding as a generic subcommand to `harmonize_metadata.py` since this comment syntax is corpus-specific to NynorskLIA.)

---
This issue was prepared as part of the UniDive WG1 T1.5 spoken language guidelines effort. Happy to help implement these changes ourselves if that's easier than doing it on your end - just let us know.
