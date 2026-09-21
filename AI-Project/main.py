import time
import pyttsx3      # for text to speech convert
import speech_recognition as sr     # for speech recog..
import datetime         # for date
import webbrowser       # for open browser
import urllib.request
import wikipedia        # for wiki search
import os
import requests, json
import cgi
import smtplib
from email.message import EmailMessage
import tkinter as tk
import threading
from translate import Translator
assitanceName = "Vivek"
def weather(CITY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY="5ea9269ece0f0c287803a5b69fca4d80"
    if(API_KEY!=""):
        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        if response.status_code == 200:
        # getting data in the json format
           data = response.json()
           # getting the main dict block
           cal = data['main']['temp']-272.15
           return cal
    else:
        return "Sorry API key is not available"

def gettask():
    # TAKING INPUT FROM USER FOR TASK
    my_mic = sr.Microphone()  # set up microphone
    r = sr.Recognizer()  # to recognize input from microphone
    try:
        with my_mic as source:
            print("listing....")
            r.pause_threshold = 0.7
            audio = r.listen(source)
        res = r.recognize_google(audio, language="en-in, hi-in")
        if isinstance(res, (list, tuple)):
            res = " ".join(res)
        return str(res).lower()
    except:
        speak("i cant understand please say again")
        my_mic = sr.Microphone()  # set up microphone
        r = sr.Recognizer()  # to recognize input from microphone
        try:
            with my_mic as source:
                print("listing....")
                r.pause_threshold = 0.7
                audio = r.listen(source)
            res = r.recognize_google(audio, language="en-in, hi-in")
            if isinstance(res, (list, tuple)):
                res = " ".join(res)
            return str(res).lower()
        except:
            speak("see you later")
            return None

def speak(task):
    # TEXT TO SPEECH
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # FOR VOICE CHANGING 0 FOR MALE 1 FOR FEMALE
    engine.say(task)
    engine.runAndWait()

username = "Vivek"
def set_username():
    global username
    speak("hey what is your name?")
    username = gettask()
    return f"welcome {username}"
def my_day():
    return datetime.date.today()
def greed_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        speak(username)
    elif hour>=12 and hour<18:
        speak("good Afternoon")
        speak(username)
    else:
        speak("good evening ")
        speak(username)
    speak("what can i help u %s" %username)
def connect():
    try:
        urllib.request.urlopen("https://google.com")
        return True
    except:
        return False
def wakeup():
    task=gettask()
    return task
def add_email():
    speak("add sender id")

def addreminder():
    speak("Date of Event")
    date=gettask()
    speak("what is the event")
    event = gettask()
    try:
        with open('reminderfile', 'a', encoding='utf-8') as f:
            f.write(f"{date},{event}\n")
        return "event saved successfully"
    except Exception:
        return "failed to save event"
def chekcreminder():
    today=time.strftime('%d %B %Y').lower()
    try:
        with open('reminderfile','r', encoding='utf-8') as f:
            for line in f:
                if today in line:
                    parts = line.split(',')
                    return "Todays Event is " + (parts[1].strip() if len(parts) > 1 else "")
        return "no event found"
    except FileNotFoundError:
        return "no event found"
def translate_lang():
    try:
        speak("in which language you want to tanslate")
        lang=gettask()
        speak("what is the content")
        cont=gettask()
        trans=Translator(to_lang=lang)
        return trans.translate(cont)
    except:
        return "not able to translate to this lang"
def filework():
    speak("what is the file name")
    fileName = gettask()
    speak("what you want to do read or write")
    if not fileName:
        return "no file name provided"
    action = gettask()
    if action == "read":
        try:
            with open(fileName, "r", encoding='utf-8') as f:
                return f.read()
        except Exception:
            return "file not available"
    elif action in ('write', 'create new'):
        try:
            with open(fileName, "a", encoding='utf-8') as f:
                speak("what is the file content")
                content = gettask() or ""
                f.write(content)
            return "data save successfully"
        except Exception:
            return "failed to write file"
    else:
        return "file function are read and write"
if __name__ == '__main__':
    def Activate():
        S_cond = True
        if not connect():
            speak("please check network connectivity")
        else:
            greed_me()
            Email={
                'Vivek Khanke':{'email_id':'beginnertoproplus@gamil.com'},
                
            }
            que={
                'who are you':'i am your voice assistant jarvis',
                'who is your father':'i dont have father but technically its my team',
                'who is your mother':'i dont have mother',
                'how are you':'i am fine',
                'what is your name':'i am jarvis',
                'you are single':'yes i am',
                'where are you from':'i am from Amravati',
                'what is your brother name':'i dont have brother',
                'what is your sister name':'i dont have sister',
                'you have brother':'no',
                'you have sister': 'no',
                'what you love':'i love to assist you',
                'what is your date of birth':'my birthday is on 27 Aug 2021',
                'what is your birth date': '27 dec 1999',
                'what is your ability':'my ability is to assist you and your computer',
            }
            path_app={
                'chrome': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                'msword': r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
            }
            com_app = {}
            task=""
            S_cond=True
            while S_cond:
                   task = gettask()
                   if task != None:
                        temp = task.split(" ")
                        print(temp)
                        # searching started
                        if "weather" in task:
                            task=task.replace("weather","")
                            speak(task)
                            speak("weather is")
                            speak(weather(task))
                            speak("degree celcius")
                        elif task in que:
                            speak(que[task])
                        elif "translate" in task:
                            speak(translate_lang())
                        elif "open file" == task:
                           speak(filework())
                        elif "set reminder"== task:
                            speak(addreminder())
                        elif "what is the today reminder" == task:
                            speak(chekcreminder())
                        elif "set username"== task:
                            speak(set_username())
                        elif str(task).startswith("open"):       # OPENING SOMETHING
                            task=task.removeprefix("open ")
                            if "youtube" in task:
                                speak("opening youtube")
                                webbrowser.open('youtube.com')
                            elif "google" in task:
                                speak("opening Google")
                                webbrowser.open('google.com')
                            elif "map" in task:
                                webbrowser.open('map.com')
                            elif 'facebook' in task:
                                webbrowser.open('facebook.com')
                            elif task in path_app:
                                speak("opening")
                                speak(task)
                                os.startfile(path_app[task])
                            elif task in com_app:
                                 speak("opening")
                                 speak(task)
                                 os.system(task)
                            else:
                                speak("Please repeat")
                        elif 'time' in task:
                            strTime = datetime.datetime.now().strftime("%H:%M:%S")
                            speak("current time is")
                            speak(strTime)
                        elif "today's date" in task:
                            speak(datetime.datetime.now().date())
                        elif "today's day" in task:
                            speak("todays day is")
                            speak(datetime.datetime.now().strftime("%A"))
                        elif "send mail" in task:
                            add_email()
                        elif "wikipedia" in task:
                            speak("searching....")
                            results = wikipedia.summary(task, sentences=2)
                            speak("according to wikipedia")
                            speak(results)
                        elif "search" in task:
                            task=task.replace("search","")
                            webbrowser.open(task)
                        elif "stop jarvis" == task:
                            speak("ok bye bye")
                            S_cond=False
                        else:
                            speak("Sorry i don't know about that")
                   else:
                        speak("whenever you free tell me")
                        S_cond = False
        if S_cond==False:
            main.destroy()

# Initialize main window
main = tk.Tk()

main.geometry("500x600")

main.title("JARVIS")

main.configure(background='black')
logo = None
if os.path.exists("logo.png"):
    try:
        logo = tk.PhotoImage(file="logo.png")
        main.iconphoto(False, logo)
    except Exception:
        logo = None
photoL = tk.Canvas(main, bg="blue", height=50, width=300)
# filename = PhotoImage(file="mic2.png")
# background_label = Label(main, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
photoL.pack()
photofile = None
photo = None
if os.path.exists("mic1.png"):
    try:
        photofile = tk.PhotoImage(file="mic1.png")
        photo = photofile.subsample(1,1)
    except Exception:
        photo = None

if photo:
    btn = tk.Button(main, image=photo, font=("Verdana", 20),
                   command=lambda: threading.Thread(target=Activate).start())
else:
    btn = tk.Button(main, text="Start", font=("Verdana", 20),
                   command=lambda: threading.Thread(target=Activate).start())
btn.pack(side="bottom")

photoL.pack(pady=5)
main.mainloop()
