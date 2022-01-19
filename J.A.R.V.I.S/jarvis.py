import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
from gtts import gTTS
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    print("       ")
    print(f" {audio}")
    print("       ")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Boss")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")

    else:
        speak("Good evening boss")

    speak("how may I help you")


def takeCommand():
    # This function takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")


    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourgmail.com","passw")
    server.sendmail("yourgmail.com", to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on input
        if 'wikipedia' in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            n = random.randint(0,5)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            pat1 = "C:\\Users\\SAHIL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(pat1)

        elif 'open pycharm' in query:
            pat2 = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(pat2)

        elif 'email to dad' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "prj144@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print("Sorry sir the email couldn't be sent")

            continue

        elif 'thank you' in query:
            break



