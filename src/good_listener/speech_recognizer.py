import speech_recognition as sr
from pathlib import Path

spooky_file = 'src/good_listener/data/SpookyHalloween.wav'
speech_recognizer = sr.Recognizer()

spooky_halloween = sr.AudioFile(spooky_file)

with spooky_halloween as source:
    beer = speech_recognizer.record(source, duration=60)
    zombies = speech_recognizer.record(source, duration=60)
    nice = speech_recognizer.record(source, duration=60)

spooks = [beer, zombies, nice]

for s_idx, spook in enumerate(spooks):
    try:
        print(
            f"spook{s_idx} - {speech_recognizer.recognize_google(spook)} \n\n\n"
        )
    except sr.UnknownValueError:  # speech is unintelligible
        print("Could not understand audio")
