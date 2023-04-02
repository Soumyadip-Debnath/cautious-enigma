import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=4 and hour< 12:
        speak("Good Morning sir")
    elif hour>= 12 and hour< 18:
        speak("Good Afternoon Sir")
    elif hour>= 18 and hour< 20:
        speak("Good Evening sir")    
    else:
        speak("Good Night sir")
        
    speak("I am Friday, Please tell me how may I help you")  
    
    
            


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try: 
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in') 
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Say that again please....")  
        return "None"
    return query
  
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        
        if 'friday quit' in query:
            speak("Thank you sir for your time")
            break
        
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir , the time is {strTime}")
            
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open('https://www.youtube.com/') 
               
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open('https://www.google.com/')
            
        elif 'open chat' in query:
            speak("opening ChatGPT")
            webbrowser.open('https://chat.openai.com/chat')    
            
        elif 'open Matlab' in query:
            speak("Opening matlab")
            codePath = "C:\\Program Files\\MATLAB\\R2022b\\bin\\matlab.exe"   
            os.startfile(codePath) 
           
        elif 'open code' in query:
            speak("Opening VsCode")
            codePath = "C:\\Users\\SOUMYADIP DEBNATH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            

         
                
                    
            
        