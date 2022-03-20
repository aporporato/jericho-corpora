# JERICHO CORPORA

## Introduction

Corpora of actions and transcripts of Interactive Fiction made possible by [**Jericho**](https://github.com/microsoft/jericho).

### Jericho Actions

The file `actions_stripped_set_sorted_aug-ann.txt` contains the set of all action in the walkthrough of games supported by Jericho, extracted from `actions_stripped_set_sorted_aug.txt` (create in `jericho_actions.ipynb`) and manually annotated with the aid of [NLTK](https://www.nltk.org/) in `common_actions_wn_vn_fn.ipynb`.

Each row reports one step of the walkthrough, [WordNet](https://wordnet.princeton.edu/) synset of the sense of its verb, its offset ID, the sense(s) of the verb's troponym in [VerbNet](https://verbs.colorado.edu/verbnet/), the frame(s) suitable for the action expressed by the verb in [FrameNet](https://framenet.icsi.berkeley.edu/fndrupal/), and a number that states if the action is accomplished by the player (0) or an NPC (1); for each of these, a void label is a valid option, as for some of these, multiple label can be assigned to a certain examples.

### Common Commands

The same annotation described above has been applied to common Interactive Fiction commands, as described [here](http://pr-if.org/doc/play-if-card/) (the image is available for reference as a PDF file). The result is available in `common_commands.csv`.

### ELECTRA for IF

The dataset has been used to finetune a small [ELECTRA](https://github.com/google-research/electra) discriminator for action classification.

Each dataset has been constructed from the four different annotation described above; then every label that do not have a correspondence in the common commands dataset and has less than 5 example has been filtered out. The code is available in the `electra-if` directory.

For the results, visit https://github.com/aporporato/electra.

### Jericho Transcript

The file `jericho_transcript.ipynb` can be used to generate the transcript of all the supported games while following their walkthrough. A (redacted for clarity) example can be found in `script.txt`.
