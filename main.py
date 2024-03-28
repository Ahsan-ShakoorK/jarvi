import pyttsx3
import speech_recognition as sr

from random import choice
from decouple import config

engine = pyttsx3.init('sapi5')
engine.setProperty('volumne', 1.5)
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER')
host = config('BOT')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    speak(f'Hello {USER}, how can i help you?')
    print(f'Hello {USER}, how can i help you?')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
        if not 'stop' in query or 'exit' in query:
            speak('Goodbye')
            exit()
    except Exception as e:
        print('Say that again please...')
        return 'None'
    return query



if __name__ == '__main__':
    greet()
    while True:
        query = take_command().lower()
        if "hello" in query:
            speak("Yes, how can I help you?")
        else:
            speak('I am sorry, I did not get that')
            print('I am sorry, I did not get that')
    