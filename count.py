""" Count the total number of minutes and 400ms sized samples in this dataset """

import pathlib
import torchaudio
from math import ceil

# Store the total duration and number of samples
duration, tracks, samples = 0, 0, 0

# Store entries missing annotations
missing = []

# Iterate the directory
path = pathlib.Path(__file__).resolve().parent
for element in path.iterdir():
    if element.is_dir() and not element.name.startswith("."):
        # Load the audio file
        audio, sr = torchaudio.load(element / "mix.wav")

        # Add duration
        duration += audio.shape[1] / (60 * sr)

        # Count track
        tracks += 1

        # And 400ms samples
        samples += ceil(audio.shape[1] / (4 * sr))

        if not (element / "annotation.mid").exists():
            missing.append(element)


print(f"Total duration: {duration:.2f} minutes     ({(duration / 60):.2f} hours)")
print(f"Number of tracks: {tracks}")
print(f"Number of samples: {samples}")

if missing:
    print(f"\n{len(missing)} missing annotations:")
    for element in missing:
        print(element.name)