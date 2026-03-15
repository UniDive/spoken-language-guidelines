---
layout: base
title:  'Treebank structure'
udver: '2'
---


# Treebank structure

## Problem identification
While token- and sentence-level information should remain encoded directly in the CoNLL-U files (in the MISC column for tokens and in # comment lines for sentences), we propose storing document-level and speaker-level metadata, such as detailed information on speech events and speakers, in an external metadata file to avoid redundancy, improve readability, and enable consistent maintenance.

Concretely, this takes the form of a `metadata.json` file placed in a designated folder, containing entries indexed by stable identifiers (e.g. `document_id` and `speaker_id`) that are referenced in the CoNLL-U files through those identifiers, as in the examples below.

Another issue relates to the storage of treebanks in CoNLL-U files, which are organised in a way that is consistent with a document-level structure, as discussed in the [Github issue #1146](https://github.com/UniversalDependencies/docs/issues/1146). This problem is also addressed in the proposal below.

> if there is a general template generated for a new treebank, the creation of metadata.json could be a default feature -- to discuss with Dan Zeman

## Proposal overview
We propose two major optional evolutions for the storage of corpora in Universal Dependencies and related projects.

1. A more flexible organisation of the corpus into individual files, in order to be able to keep original split into "document" when such split exists in the original data.
2. A shared storage of some metadata. When some specific metadata is shared among several sentences, we want to avoid to copy it on each sentence.

Note that the two proposals can be used independently, but in practice, it is interesting to use both together, because keeping the original split into sub documents (1) may allow for a better sharing in (2).

The proposal (1) was already discussed in [Github issue #1146](https://github.com/UniversalDependencies/docs/issues/1146). In order to prevent problems reported there, we propose to make the new organisation available in a specific subfolder and to keep the existing UD requirements (i.e. test, dev, train split) at the root of each repository.

> To discuss: in which folder shall we put the new organisation?
> - `original_split`
> 	- ✅ more visible and available in official data releases 
> 	- ❌ need to change the UD infrastructure 
> 		- allowing the new folder
> 		- check at validation time consistency of data in `.` and in `original_split` (a script is available for this)
> - `not-to-release/original_split`
> 	- ✅ no change in UD infrastructure
> 	- ❌ less visible and requires users to go to github if they want to use it
> 
> **Note** For now, we chose the second option (in this document, scripts and examples) for a better intergration into UD infrastructure, but we would like the first one to be chosen.

## Flexible organisation

We propose (as an optional feature) to store a user defined organisation of the corpus into subfiles in the folder `not-to-release/original_split`.
If this option is chosen, the folder must also contain a file `merge.json` which describes how to build the UD final files to be stored at the root folder.

### JSON file encoding 

The file `merge.json` stores a dictionary describing each file for the final UD split into dev/test/train. The description can be document-based (one whole document goes in one UD file) or sentence-based (when a document is split across different UD files). Document-based and sentence-based can be mixed.
Technically, in  `merge.json` main dictionary, each UD file is described as a list of *sections*, a *section* being a JSON object with one key (either `document_ids` or `sent_ids`) associated with a list of strings.

### Example 
Below here shortened example of the `merge.json`  for the corpus `UD_French-Rhapsodie` with a mixed description (the document `Rhap_M0001` is partially used in `dev` and in `test`).

```json
{ "fr_rhapsodie-ud-dev": [
    { "document_ids": [
		"Rhap_M0024",
		…
		"Rhap_M1003"
	]},
	{ "sent_ids": [
		"Rhap_M0001-1",
		…
		"Rhap_M0001-8"
	]}
],

  "fr_rhapsodie-ud-test": [
	{ "sent_ids": [
		"Rhap_M0001-9",
		…
		"Rhap_M0001-14"
	]},
	{ "document_ids": [
		"Rhap_D2011",
		…
		"Rhap_D1001"
	]}
],

  "fr_rhapsodie-ud-train": [
	{ "document_ids": [
		"Rhap_M0016",
		…
		"Rhap_M0018"
	]}
]}
```

See below for a python script using `merge.json` to produce the final UD files.

## Metadata sharing

This question was discussed in [Github issue #1135](https://github.com/UniversalDependencies/docs/issues/1135). The current proposal borrows idea from this discussion but relies on a explicit sharing through an external file instead of encoding it in specific metadata such as `meta::author`

In this context, we require that all metadata are encoded as: `# <key> = <value>`. Even if it is not a strict requirement in UD, it is a largely used in pratice.

The metadata sharing mechanism is based on the fact that there are many cases where one metadata is dependent of another. Formally, the metadata `key_B` depends on `key_A` (written `key_A -> key_B`), if for each value of `key_A`, in all the treebank, there is only one possible value for `key_B`. In such a case, we can store this association (values of `key_A` -> values to `key_B` globally, in a dictionary, instead of copying it each time or relying on a implicit mechanism).

### Examples of dependencies
In spoken data treebank, it is common to have speaker related information and to use of the meta `speaker_id` as a treebank level identifier. In this case, we have the following dependencies:
 - `speaker_id -> speaker_age`
 - `speaker_id -> speaker_sex`
 - …

We also consider that each sentence has an implicit metadata `document_id` which corresponds to the base name or the CoNLL-U file (for instance, each sentence in the file `Rhap_M0018.conllu` as an implicit metadata `document_id = Rhap_M0018`). Again in case of spoken data, it is common to have an audio file associated to each recording. If each recording is a file, the following dependency can be used:
 - `document_id -> sound_url`. This example explain why it is useful to use both mechanisms (flexible document splitting and metadata sharing) at the same time.

### JSON encoding of values dependencies

Shared metadata are stored in a JSON file `metadata.json` (in the folder `not-to-release/original_split`) with nested objects following the structure (when the metadata `key_B` depends on `key_A`):
```json
{ "key_A": 
  { "value_A":
	{ "key_B": "value_B" }  
  }
}
```
This is interpreted as "all sentences with meta `key_A = value_A` also carry meta `key_B = value_B`"

### Examples

This is a (shortened) example of possible metadata sharing in the corpus `UD_Naijs-NSC`:

```json
{
  "document_id": {
    "ENU_13_School-Life_DG": {
      "sound_url": "https://naijasyncor.huma-num.fr/carte/mp3/ENU_13_School-Life_DG.mp3"
    }
  },
  "speaker_id": {
    "Sp87": {
      "speaker_age": "16-30",
      "speaker_birthplace": "Enugu",
      "speaker_education": "Tertiary",
      "speaker_naija_competency": "Moderate",
      "speaker_primary_other_language": "Igbo",
      "speaker_residence": "Enugu",
      "speaker_sex": "F"
    },
    "Sp86": {
      "speaker_age": "16-30",
      "speaker_birthplace": "Enugu",
      "speaker_education": "Tertiary",
      "speaker_naija_competency": "High",
      "speaker_primary_other_language": "English",
      "speaker_residence": "Enugu",
      "speaker_sex": "F"
    }
  }
}
```


## Examples of treebanks implementing the proposed solution

The above proposal is currently being implemented in three treebanks:
 - **UD_French-Sequoia**: only the flexible organisation is used
 - **UD_French-ParisStories**: metadata sharing is used for `sound_url` storage
 - **UD_French-Rhapsodie**: metadata sharing is used extensively for a variety of metadata

The table below provides access to the relevant GitHub folders and files.

| treebank | base folder | original_split folder | merge JSON file | metadata JSON file |
|----------|:----------:|:----------:|:----------:|:----------:|
| **UD_French-Sequoia** | [dev](https://github.com/UniversalDependencies/UD_French-Sequoia/tree/dev) | [dev](https://github.com/UniversalDependencies/UD_French-Sequoia/tree/dev/not-to-release/original_split) | [merge.json](https://github.com/UniversalDependencies/UD_French-Sequoia/blob/dev/not-to-release/original_split/merge.json) | Unused |
| **UD_French-ParisStories** | [dev](https://github.com/UniversalDependencies/UD_French-ParisStories/tree/dev) | [dev](https://github.com/UniversalDependencies/UD_French-ParisStories/tree/dev/not-to-release/original_split) | [merge.json](https://github.com/UniversalDependencies/UD_French-ParisStories/blob/dev/not-to-release/original_split/merge.json) | [metadata.json](https://github.com/UniversalDependencies/UD_French-ParisStories/blob/dev/not-to-release/original_split/metadata.json) |
| **UD_French-Rhapsodie** | [dev](https://github.com/UniversalDependencies/UD_French-Rhapsodie/tree/dev) | [dev](https://github.com/UniversalDependencies/UD_French-Rhapsodie/tree/dev/not-to-release/original_split) | [merge.json](https://github.com/UniversalDependencies/UD_French-Rhapsodie/blob/dev/not-to-release/original_split/merge.json) | [metadata.json](https://github.com/UniversalDependencies/UD_French-Rhapsodie/blob/dev/not-to-release/original_split/metadata.json) |



## Python tools

The scripts described below are available in [https://github.com/UniDive/SpLAn-UD](https://github.com/UniDive/SpLAn-UD) (folder `metadata-encoding`).

These scripts use the [conllup](https://pypi.org/project/conllup/) library. It would be easy to switch to a different CoNLL Python library if better integration with the UD infrastructure is required.

### Merge and unshare

We provide a Python script [`merge_and_unshare.py`](https://github.com/UniDive/SpLAn-UD/blob/main/metadata-encoding/merge_and_unshare.py) which takes the base folder `<BASE>` (where dev/test/train `conllu` files are expected) as an argument.
From the folder `<BASE>/not-to-release/original_split`, the script reads documents (all files with the `.conllu` extension), as well as the files `merge.json` and, if present, `metadata.json`.

Running the script poduces files in the folder `<BASE>` according to the description in the `merge.json` file.
If a file `metadata.json` is present the `<BASE>/not-to-release/original_split` folder, the script will also take care of unsharing when producing the final UD files (with repetition of metadata on each sentence where it holds).

### Build the shared metadata version from the full version (with repetitions)

The script [`metadata_share.py`](https://github.com/UniDive/SpLAn-UD/blob/main/metadata-encoding/metadata_share.py) is available. It can be used to produce both the `metadata.json` files and the new version of the `conllu` files without the shared metadata.
The metadata to share must be given explicitly.
Please refer to `--help` options of the script for usage detail.

### Discover the metadata dependencies in a treebank

The script [`metadata_detect_sharable.py`](https://github.com/UniDive/SpLAn-UD/blob/main/metadata-encoding/metadata_detect_sharable.py) reads a all the documents in a given folder (i.e. all files with the `.conllu` extension) and prints diagnostics on the dependencies between the metadata used in the treebank. It can be used to help build an explicit metadata set to share with the script `metadata_share.py`.

**Note**: the output of the script must be manually processed because we may observe:
 - spurious dependencies between metadata that we do not want to exploit
 - missing expected dependencies due to errors in the metadata treebank (as occurred in [Rhapsodie](https://github.com/surfacesyntacticud/SUD_French-Rhapsodie/commit/23ee4055ad82a20b603db0df5513582e135b1cb7)])
 - when two metadata are mutually dependent (for instance `document_id` and `sound_url`), we have to choose the meaniful one
