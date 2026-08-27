# Maintainer email draft

Subject: UniDive spoken-language UD guidelines — status of treebanks and next steps

Dear maintainer,

We're writing on behalf of the [UniDive Working Group 1, Task 1.5](https://unidive.lisn.upsaclay.fr/doku.php?id=wg1:wg1) (spoken language guidelines), a group that has spent the past months working on harmonising how spoken data is represented in Universal Dependencies.

A few things we wanted to share:

1. **What we've done.** As part of UniDive, we've been drafting guidelines covering several aspects of spoken-language annotation: how to segment spoken data into maximal units, tokenization and morphological annotation strategies specific to speech (numbers, acronyms, onomatopoeias, pauses, non-verbal behaviours, etc.), syntactic annotation of co-constructions and other spoken-specific constructions (parataxis, tag questions, feedback/backchannels), and standardized naming conventions for speech-related metadata, together with a proposal for how to structure larger corpora and share repeated metadata without duplicating it on every sentence.

2. **Thank you for participating in our survey.** Since late September 2024, we've been running a survey on how spoken data is currently annotated in UD/SUD treebanks (transcription, metadata, annotation practices). If you or someone from your team filled it in, thank you — we've had 27 treebanks responding, and your answers directly informed the guidelines and the treebank-by-treebank comparison described below.

3. **Becoming a stable working group.** We'd like to turn this from a UniDive task into an ongoing effort: a group that meets at least around every official UD release to keep working together on spoken-data annotation standards, review new treebanks, and revisit open questions as the guidelines evolve. To that end, we've set up a mailing list — to join, please sign up [here](TBA).

4. **Open issues on the UD docs repo.** Several related discussions are already open on the [UniversalDependencies/docs](https://github.com/UniversalDependencies/docs) issue tracker, and we'd really encourage you to weigh in on any that are relevant to your treebank:
   - [#1273](https://github.com/UniversalDependencies/docs/issues/1273) — Maximal unit segmentation in spoken data
   - [#1289](https://github.com/UniversalDependencies/docs/issues/1289) — Tokenization and morphological annotation strategies in spoken language treebanks
   - [#1280](https://github.com/UniversalDependencies/docs/issues/1280) — Annotation of co-constructions in spoken language treebanks
   - [#1290](https://github.com/UniversalDependencies/docs/issues/1290) — Specific constructions (parataxis, tag questions, feedback) in spoken language
   - [#1282](https://github.com/UniversalDependencies/docs/issues/1282) — Treebank structure and metadata sharing (follows on from the earlier [#1135](https://github.com/UniversalDependencies/docs/issues/1135) and [#1146](https://github.com/UniversalDependencies/docs/issues/1146))
   - [#1300](https://github.com/UniversalDependencies/docs/issues/1300) - Metadata standardization

   These decisions affect how spoken treebanks like yours will be structured and annotated going forward, so your experience and opinions are genuinely useful there.

5. **Everything is documented in a dedicated repo:** [UniDive/spoken-language-guidelines](https://github.com/UniDive/spoken-language-guidelines) (rendered at [grew.fr/spoken-language-guidelines](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/)). It covers maximal unit segmentation, tokenization and morphological annotation, syntax (including co-constructions and other spoken-specific constructions), the metadata conventions, the treebank-structure/metadata-sharing proposal, and the full survey below.

6. **A survey of all spoken/mixed treebanks.** We went through every spoken and mixed-modality treebank currently in UD and checked how its metadata compares to the proposed conventions, to see what could realistically be brought in line with minimal effort. The full table is here: [ud_spoken_treebanks.html](https://grew.fr/spoken-language-guidelines/workgroups/spoken-data/ud_spoken_treebanks.html)

   For each treebank, we've drafted a concrete, treebank-specific suggestion. Please treat it as a starting point rather than a final verdict — the comparison was carried out semi-automatically with the help of Claude (Anthropic), so it's possible we misread something about your corpus, and we'd welcome any corrections or pushback.

We'd love to have you (and anyone else on your team) involved as this becomes a standing group — whether that's commenting on the docs issues, reacting to the treebank-specific suggestion, or just joining future discussions/meetings.

Thanks for your work on resources, and looking forward to hearing from you.

Best,
Ludovica Pannitto, Kaja Dobrovoljic, Sylvain Kahane, Bruno Guillaume,
on behalf of the UniDive WG1 T1.5 — Spoken Language Guidelines
