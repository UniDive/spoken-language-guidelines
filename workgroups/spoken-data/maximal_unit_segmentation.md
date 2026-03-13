---
layout: base
title:  'Maximal Unit Segmentation'
udver: '2'
---

- [Maximal Unit Segmentation](#maximal-unit-segmentation)
	- [Speaker view vs. Dependency view](#speaker-view-vs-dependency-view)
	- [What to do](#what-to-do)


# Maximal Unit Segmentation

Not all currently available spoken treebanks take the same approach at maximal unit segmentation. More specifically, there is a tension between a prosodic and a syntactic view of sentence completion.
The prosodic approach goes for minimal boundaries, segmenting sentences at prosodic termination. The drawback is that these can be hard to find (i.e., subjective interpretation of the annotator, difficult to come up with a clear test), and the resulting unit doesn't always correspond to what we intuitively think of as a sentence.
The syntactic approach can lead to a more "maximal" segmentation. The drawback is that it might lead to arbitrarily long sentences as the boundary between discourse functions and syntactic functions is blended.

Examples from current works:

* KiParla: standard for segment completion is "If you can link (syntactically), link". This allows us to cross intonation boundaries only if the annotator can link a new syntactic unit back to an exact token in the previous syntactic unit. If not, terminate.
* Hausa: a new sentence is indicated by a new semantic frame, topic, etc. Which is usually indicated by a discourse marker (and, but, so, therefore, allora, então, etc.)
* Rhapsodie: if two main verbs are at the same level, we cut, even if there is a coordinating conjunction between them. Exceptions: shared subject (she came and asked a question -> “asked a question” is not autonomous)

The general principle that we want to enforce is **"if you can link, link"**

This doesn't necessarily need to be applied in a strict way. You may have a discourse marker that is a connective that could technically link back, but shouldn't because there is a very long pause, for example.
Language-specific hints that may help us identify the presence of a link.

TODO: explicit reference to `rectional unit` (Kahane&Pietrandrea) @sylvainkahane

This means that segmentation has to be performed on the basis of various criteria: syntactic, prosodic and semantic at once.

## Speaker view vs. Dependency view

TODO: @bguil

## What to do

In cases of:

* dislocation
  * HOW TO: code the explicit relation even when explicit syntactic markers (not only connectives, even things like tense which you wouldn't find in a clause alone) are not there, if prosody allows for it
* reported speech
  * feature Reported=Yes (on the root of subtree) : it is important because a reported speech is not necessary introduced are marked by a specific construction;
  * When a reported speech is introduced by a speech verb or any other construction, only the first sentence is attached to it: she said please don’t do that // we need it //
* parataxis: generally speaking if two clauses are linked by generic parataxis (juxtaposed sentences) than they should be split into two different maximal units. Exceptions are:
  * `parataxis:parenth` for parenthetical sentences
  * `paratataxis:insert` for inserts in reported speech
  * if a sentence is a verbal dislocated unit, than it is tagged as `dislocated`
* false starts: are kept into the sentence if possible. Examples `you you we have to do that` or `we should we must do that` are single maximal units.