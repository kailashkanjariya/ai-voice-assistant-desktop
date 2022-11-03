from email.mime import audio
from logging import captureWarnings
from socket import timeout
from time import strftime
import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# text  to speech


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To convert voice into text


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=15, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# To wish


def wish():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I am jarvis sir. Please tell me hoe can i help you")


if __name__ == "__main__":
    wish()
    while True:
        if 1:
            query = takeCommand().lower()

            # logic building for tasks

            if "open notepad" in query:
                npath = "C:\\Windows\\notepad.exe"
                os.startfile(npath)

            elif "play music" in query:
                music_dir = "E:\\songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[79]))

            elif "the time" in query:
                strTime = datetime.datetime.now(),strftime("%H:%M:%S")
                speak(f"sir, the time is {strTime}")
