import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def introduce():
    speak("Hello I am Suhani. A simple Desktop assistant. Let me do some work for you.")
    speak("Tell me What can I do for you?")


def wish_me():
    speak("Hiiii,... I am Suhani.... How are you Divyanshu? How is your day going?")
    speak("Tell me, What I can do for you?")


def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=3000 , phrase_time_limit=5000)
            print("Recogninzing...")
            query = r.recognize_google(audio, language='en-in')
            return query
        except Exception as e:
            return None


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if query == None:
            speak("Please speak that again...")
            continue
        query = query.lower()
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                print('Searching Wikipedia...')
                query = query.replace('search wikipedia',"")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to Wikipedia...")
                print(results)
                speak(results)
            except:
                speak("Sorry, didn't found anything about that")
        elif 'introduce' in query:
            introduce()
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'how are you' or 'hello' in query:
            speak("Hello Divyanshu. I am Good.")
            speak("How are you?")
            speak("Tell me what can i do for you")
        elif 'play music' in query:
            music_dir = "D:\\On The Go Music List"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[[0]]))
        elif 'exit' or 'take rest' in query:
            print('Exiting The Program')
            speak('Hope, I helped you with your tasks. Have a good day.')
            speak('Or wait. Have a day you deserve.')
            break
        else:
            speak("I didn't got what you said.")
            speak("Tell me, what I can do for you?")
