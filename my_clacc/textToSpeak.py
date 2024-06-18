from gtts import gTTS
import os


class Speaker():
    text = ''

    def __init__(self, text):
        self.text = text

    def speak(self):
        tts = gTTS(self.text, lang="ru")
        tts.save("output.mp3")
        os.system("start output.mp3")
