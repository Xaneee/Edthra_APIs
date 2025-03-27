import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 155)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
