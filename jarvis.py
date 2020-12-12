import datetime
import os
import smtplib
import webbrowser
import pyaudio
import pyttsx3
import speech_recognition as s
import wikipedia
import random

engine = pyttsx3.init('sapi5') #microsoft api spai5
voices = engine.getProperty('voices') #two types of voices are available in our pc
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Pepper Sir. Please tell me how may i help you")
        
def takeCommand():
    #it takes microphone input from the user and return string output.   
    
    r = s.Recognizer()
    with s.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "none"
    
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com' , 587) 
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', 'password') 
    server.sendmail('abc@gmail.com' , to, content)
    server.close()
        
if __name__ == "__main__":
    wishMe()
    #while True:(to continue listning loop)
    if 1:
        query = takeCommand().lower()
    #logic for executing tasks based on query
    
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")
            
        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")
            
            
        elif 'open udemy' in query:
            webbrowser.open("udemy.com")
        
        
        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[6]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)
            
        elif 'open vscode' in query:
            codePath = "C:\\Users\\kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to sonu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abc@gmail.com@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Sir Your Email has not been sent Please try  again!")
