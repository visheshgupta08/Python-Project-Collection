import pyttsx3
import time

names = ["vishesh"]
long_speech = ""

for name in names:
    long_speech += f"please drink a water {name}"

while True:
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    engine.setProperty('rate',125)
    engine.say(long_speech)
    engine.runAndWait()
    engine.stop()

    del engine
    time.sleep(10)