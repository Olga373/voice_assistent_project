import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)


def speaker(text):
    engine.say(text)
    engine.runAndWait()
