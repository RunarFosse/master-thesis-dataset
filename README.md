# SADTP Dataset

This repository contains the SADTP *(Small Automatic Drum Transcription Performance)* dataset, a dataset suited for learning DTM *(Drum Transcription in the Presence of Melodic Instruments)* tasks.

### Composition

The dataset is composed of **1.08 hours** of music over **16 tracks**.
For each track there exist both a playback mixture waveform audio file, as well as a respective annotation in MIDI.

### Annotation

Each track has been annotated automatically by piping and recording the MIDI output of a Roland TD-11 electric drumset into Apple's Garageband, live while playing with each track on playback.

Minimal post-processing has been done, other than exporting the annotation as a standalone MIDI file.

### Performance

Each of the annotations represent a performance of the original track. While each performance is an attempt to be consistent with the original track's drumset performance, slight inconsistencies might appear and manifest as noise in the data. These might include slight timing variations or incorrect labeling.

However, these inconsistencies are human-induced and one stands to argue that this could provide a more realistic measure of performances in a real-world scenario.