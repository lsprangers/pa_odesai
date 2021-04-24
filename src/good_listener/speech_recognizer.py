import speech_recognition as sr


class SpookyJam:
    def __init__(self):
        self.default_spook_path = 'src/good_listener/data/SpookyHalloween.wav'
        self.speech_recognizer = sr.Recognizer()
        self.spooky_halloween = sr.AudioFile(self.default_spook_path)

    def jam(self):
        with self.spooky_halloween as source:
            beer = self.speech_recognizer.record(source, duration=60)
            zombies = self.speech_recognizer.record(source, duration=60)
            nice = self.speech_recognizer.record(source, duration=60)

        records = [beer, zombies, nice]

        for r_idx, r in enumerate(records):
            try:
                print(
                    f"\nrecord {r_idx} - {self.speech_recognizer.recognize_google(r)} \n"
                )
            except sr.UnknownValueError:  # speech is unintelligible...Mickey...
                print("Could not understand the pure essence of this")


if __name__ == '__main__':
    def_jam = SpookyJam()
    def_jam.jam()

""" 
Output:
    record 0 - it's songs about ghosts holding ghost Halloween's around let's get spooky and drink beer 
    
    
    record 1 - the zombies will come right 
    
    Could not understand the pure essence of this
"""