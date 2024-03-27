import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('volumne', 1.5)
engine.setProperty('rate', 150)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    speak('Hi, im Reema. How can i help you?')
    print('Hi, im Reema. How can i help you?')