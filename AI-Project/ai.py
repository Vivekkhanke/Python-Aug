import datetime
import os
import requests
import smtplib
import speech_recognition as sr
import threading
import time
import tkinter as tk
import urllib.request
import webbrowser
from email.message import EmailMessage
from translate import Translator
import pyttsx3
import wikipedia
from rapidfuzz import process, fuzz  # Used for flexible/adjustable matching

# --- Configuration & Global Data ---
ASSISTANCE_NAME = "Jarvis"
USERNAME = "Vivek"

# Flexible Knowledge Base (Local Dictionary)
QUESTIONS = {
    'who are you': 'I am Jarvis, your voice assistant upgraded with dynamic AI features.',
    'who is your father': 'I don\'t have a father, but technically I was built by Vivek.',
    'who is your mother': 'I do not have a mother.',
    'how are you': 'I am doing excellent, thank you! Ready to help you.',
    'what is your name': 'My name is Jarvis.',
    'you are single': 'Yes, I am a digital entity, so relationships aren\'t really my thing.',
    'where are you from': 'I live right here inside your computer system.',
    'what you love': 'I love automating tasks and helping you manage things smoothly.',
    'Thanks' : 'You are welcome!',
    'thank you' : 'You are welcome!',
    'what is your date of birth': 'My baseline system was initiated on August 27, 2021.',
    'what is your ability': 'I can run automation scripts, open applications, manage local files, track reminders, and speak directly with online AI brains.',
}

APP_PATHS = {
    'chrome': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    'msword': r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE'
}

EMAILS = {
    'vivek': 'test@gmail.com',
}

# --- Hybrid AI Routing & Adjustability Logic ---

def get_ai_response(prompt):
    """
    Fallback Free AI generation using a public serverless Transformer endpoint.
    If the question isn't in your local dictionary, it gets answered by a generative AI model.
    """
    print(f"🧠 Routing query to cloud AI brain: '{prompt}'")
    try:
        # Free serverless chatbot model pipeline hosted by HuggingFace
        api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
        headers = {} 
        
        payload = {"inputs": prompt}
        response = requests.post(api_url, headers=headers, json=payload, timeout=8)
        
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                return data[0].get('generated_text', "I processed your request but can't think of a response.")
            elif isinstance(data, dict):
                return data.get('generated_text', "Let me think about that for a second.")
        return "My cloud network module is slightly lagging. Could you repeat that or ask a different question?"
    except Exception as e:
        print(f"AI Connection Error: {e}")
        return "I encountered a minor network glitch connecting to my extended neural networks."


def smart_find_answer(user_query):
    """
    Adjustable matching logic. Uses fuzzy matching to see if user input looks like 
    a dictionary key. If it matches over 70%, it serves your custom answer.
    Otherwise, it hands it off to true generative AI.
    """
    query_clean = user_query.lower().strip()
    
    # Extract the best matching key from the dictionary keys list
    match = process.extractOne(query_clean, QUESTIONS.keys(), scorer=fuzz.token_set_ratio)
    
    if match:
        best_key, score, _ = match
        print(f"🎯 Match verification | Best Key: '{best_key}' | Confidence: {round(score, 1)}%")
        # If the phrase is reasonably close, return your custom hardcoded response
        if score >= 70:
            return QUESTIONS[best_key]
            
    # If the user asks something completely arbitrary, the actual AI handles it
    return get_ai_response(user_query)


# --- Core Speech & System Operations ---

def speak(text):
    """Converts text to speech cleanly via pyttsx3."""
    if not text:
        return
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
    engine.say(text)
    engine.runAndWait()


def get_task(retries=1):
    """Captures audio and interprets it via Google Speech Recognition with safe fallback."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    for attempt in range(retries + 1):
        try:
            with microphone as source:
                print("🎙️ Listening...")
                recognizer.pause_threshold = 0.7
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=7)
            
            print("⚙️ Processing audio speech...")
            res = recognizer.recognize_google(audio, language="en-in, hi-in")
            return str(res).lower().strip()
            
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            if attempt < retries:
                speak("I missed that. Could you please repeat?")
            else:
                speak("Moving along.")
        except Exception as e:
            print(f"Audio System Exception: {e}")
            break
            
    return None


def check_connection():
    """Verifies external connection is active."""
    try:
        urllib.request.urlopen("https://google.com", timeout=2)
        return True
    except Exception:
        return False


def get_weather(city):
    if not city:
        return "City context missing."
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = ""
    try:
        url = f"{base_url}q={city.strip()}&appid={api_key}"
        response = requests.get(url, timeout=4)
        if response.status_code == 200:
            data = response.json()
            temp_celsius = data['main']['temp'] - 273.15 
            return f"{round(temp_celsius, 1)}"
        return "City not found in database."
    except Exception:
        return "Weather API systems currently offline."


def greet_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon {USERNAME}")
    else:
        speak(f"Good Evening {USERNAME}")
    speak("Jarvis interactive systems activated. What can I do for you?")


def set_username():
    global USERNAME
    speak("What should I call you instead?")
    name_input = get_task()
    if name_input:
        USERNAME = name_input.capitalize()
    return f"Done. Welcome {USERNAME}"


def add_reminder():
    speak("What date is the event?")
    date = get_task()
    if not date: return "Action cancelled."
    speak("What is the name of the event?")
    event = get_task()
    if not event: return "Action cancelled."
    try:
        with open('reminderfile.txt', 'a', encoding='utf-8') as f:
            f.write(f"{date},{event}\n")
        return "Event log saved locally."
    except Exception:
        return "Failed to save the reminder."


def check_reminder():
    today = time.strftime('%d %B %Y').lower()
    try:
        with open('reminderfile.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if today in line.lower():
                    parts = line.split(',')
                    return f"Your reminder today is: {parts[1].strip()}" if len(parts) > 1 else "Corrupted line data."
        return "You have clean schedules today."
    except FileNotFoundError:
        return "No reminders file found on disk."


def translate_lang():
    try:
        speak("Which language are we converting to?")
        lang = get_task()
        if not lang: return "Cancelled."
        speak("What phrase would you like me to translate?")
        content = get_task()
        if not content: return "Cancelled."
        
        translator = Translator(to_lang=lang)
        return translator.translate(content)
    except Exception:
        return "Failed to execute machine translation."


def handle_files():
    speak("What is the targeted file name?")
    file_name = get_task()
    if not file_name: return "File interaction dropped."
    if "." not in file_name:
        file_name += ".txt"
        
    speak("Do you want to read or write?")
    action = get_task()
    
    if action == "read":
        try:
            with open(file_name, "r", encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "Target file not found."
    elif action in ('write', 'create new', 'append'):
        try:
            with open(file_name, "a", encoding='utf-8') as f:
                speak("What text should I write?")
                content = get_task() or ""
                f.write(content + "\n")
            return "File updated."
        except Exception:
            return "Write access failed."
    return "Invalid request."


# --- Core Orchestrator Run Cycle ---

def activate_assistant():
    if not check_connection():
        speak("Please check network connectivity before booting Jarvis core engines.")
        return

    greet_me()
    running = True
    
    while running:
        task = get_task()
        if not task:
            continue
            
        print(f"💬 Processed user voice instruction: {task}")
        
        # Hard exit directives
        if task in ("stop jarvis", "exit", "bye", "quit", "shutdown"):
            speak("Thanks" if task in ("ok thanks", "thanks") else f"Deactivating system. Goodbye!")
            running = False
            break
            
        # 1. Weather Automation Routine
        if "weather" in task:
            city = task.replace("weather", "").strip()
            if not city:
                speak("Which city?")
                city = get_task()
            if city:
                result = get_weather(city)
                if result.replace('.', '', 1).isdigit():
                    speak(f"The current temperature in {city} is {result} degrees celsius.")
                else:
                    speak(result)
                    
        # 2. Local File & App Automation
        elif "open file" in task or "file operations" in task:
            speak(handle_files())
        elif "set reminder" in task:
            speak(add_reminder())
        elif "what is the today reminder" in task or "check reminder" in task:
            speak(check_reminder())
        elif "set username" in task:
            speak(set_username())
        elif "translate" in task:
            speak(translate_lang())
            
        elif task.startswith("open "):
            target = task.removeprefix("open ").strip()
            if "youtube" in target:
                webbrowser.open('https://youtube.com')
            elif "google" in target:
                webbrowser.open('https://google.com')
            elif target in APP_PATHS:
                speak(f"Launching {target}")
                os.startfile(APP_PATHS[target])
            else:
                speak(f"Searching web domains for {target}")
                webbrowser.open(f"https://www.google.com/search?q={target}")
                
        # 3. Time, Date & Web Information Scrapers
        elif 'time' in task:
            speak(f"The time is {datetime.datetime.now().strftime('%I:%M %p')}")
        elif "date" in task:
            speak(f"Today is {datetime.datetime.now().date()}")
        elif "day" in task:
            speak(f"Today is {datetime.datetime.now().strftime('%A')}")
        elif "wikipedia" in task:
            try:
                query = task.replace("wikipedia", "").strip()
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia sources:")
                speak(results)
            except Exception:
                speak("Couldn't retrieve Wikipedia data packages.")
        elif "search" in task:
            query = task.replace("search", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            
        # 4. Smart AI + Dynamic Dictionary Matching Engine Fallback
        else:
            ai_answer = smart_find_answer(task)
            speak(ai_answer)
            
    # Terminate GUI application window safely from internal runtime thread
    main.after(0, main.destroy)


# --- GUI Frame Rendering ---

main = tk.Tk()
main.geometry("700x800")
main.title("JARVIS - AI Voice Assistant")
main.configure(background='#0f1419')
main.resizable(False, False)

# Set window icon properties
main.attributes('-alpha', 0.98)  # Slight transparency for modern look

# Center window on screen
main.update_idletasks()
x = (main.winfo_screenwidth() // 2) - (main.winfo_width() // 2)
y = (main.winfo_screenheight() // 2) - (main.winfo_height() // 2)
main.geometry(f"+{x}+{y}")

# --- Top Branding Bar ---
branding_frame = tk.Frame(main, bg='#1a1f2e', height=90)
branding_frame.pack(fill=tk.X)
branding_frame.pack_propagate(False)

# Logo & Title Section
logo_frame = tk.Frame(branding_frame, bg='#1a1f2e')
logo_frame.pack(pady=15)

title_label = tk.Label(logo_frame, text="🤖  JARVIS", font=("Segoe UI", 32, "bold"), 
                       bg="#1a1f2e", fg="#00d4ff")
title_label.pack()

subtitle_label = tk.Label(branding_frame, text="Advanced Voice AI Assistant • Powered by Machine Learning", 
                          font=("Segoe UI", 9), bg="#1a1f2e", fg="#888888")
subtitle_label.pack()

# Separator line
separator = tk.Frame(main, bg='#00d4ff', height=2)
separator.pack(fill=tk.X)

# --- Main Content Area ---
content_frame = tk.Frame(main, bg='#0f1419')
content_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)

# === Features Section ===
features_label = tk.Label(content_frame, text="🌟 FEATURES & CAPABILITIES", font=("Segoe UI", 11, "bold"), 
                          bg="#0f1419", fg="#00d4ff")
features_label.pack(anchor=tk.W, pady=(0, 12))

features_box = tk.Frame(content_frame, bg='#1a1f2e', relief=tk.FLAT, bd=0)
features_box.pack(fill=tk.X, pady=(0, 20))

features_list = [
    ("🎤", "Voice Recognition", "Advanced speech-to-text with noise filtering"),
    ("🌐", "Web Integration", "Real-time weather, search, and browsing"),
    ("🧠", "AI Responses", "Powered by generative AI models"),
    ("📁", "File Management", "Create, read, and manage files seamlessly"),
    ("🌍", "Multi-Language", "Translate text between multiple languages"),
    ("⏰", "Smart Reminders", "Set and track important events")
]

for emoji, title, desc in features_list:
    feature_item = tk.Frame(features_box, bg='#1a1f2e')
    feature_item.pack(fill=tk.X, pady=6)
    
    emoji_label = tk.Label(feature_item, text=emoji, font=("Segoe UI", 12), 
                           bg="#1a1f2e", fg="#00d4ff", width=3)
    emoji_label.pack(side=tk.LEFT, padx=10)
    
    title_label = tk.Label(feature_item, text=title, font=("Segoe UI", 10, "bold"), 
                          bg="#1a1f2e", fg="#ffffff")
    title_label.pack(side=tk.LEFT, padx=(0, 10))
    
    desc_label = tk.Label(feature_item, text=desc, font=("Segoe UI", 8), 
                         bg="#1a1f2e", fg="#aaaaaa")
    desc_label.pack(side=tk.LEFT, padx=(0, 10))

# === Status Panel ===
status_panel = tk.Frame(content_frame, bg='#1a1f2e', relief=tk.FLAT, bd=0)
status_panel.pack(fill=tk.X, pady=(0, 20))

status_header = tk.Label(status_panel, text="📊 SYSTEM STATUS", font=("Segoe UI", 11, "bold"), 
                        bg="#1a1f2e", fg="#00d4ff")
status_header.pack(anchor=tk.W, padx=12, pady=(8, 8))

# Status indicator with dot
status_indicator_frame = tk.Frame(status_panel, bg='#1a1f2e')
status_indicator_frame.pack(anchor=tk.W, padx=12, pady=4)

status_dot = tk.Label(status_indicator_frame, text="●", font=("Arial", 12), 
                     bg="#1a1f2e", fg="#00ff00")
status_dot.pack(side=tk.LEFT, padx=(0, 8))

status_label = tk.Label(status_indicator_frame, text="Ready to assist • Waiting for input", 
                       font=("Segoe UI", 10), bg="#1a1f2e", fg="#ffffff")
status_label.pack(side=tk.LEFT)

connection_label = tk.Label(status_panel, text="✓ Connected • System Online", 
                           font=("Segoe UI", 9), bg="#1a1f2e", fg="#00dd88")
connection_label.pack(anchor=tk.W, padx=12, pady=(0, 8))

# === Action Button ===
button_container = tk.Frame(content_frame, bg='#0f1419')
button_container.pack(fill=tk.BOTH, expand=True, pady=15)

def create_rounded_button():
    """Create button with modern styling"""
    btn = tk.Button(button_container, text="🎤  ACTIVATE VOICE", font=("Segoe UI", 15, "bold"), 
                    bg="#00d4ff", fg="#0f1419", activebackground="#00ffff", 
                    activeforeground="#0a0a0f", command=start_assistant_thread, 
                    padx=40, pady=18, relief=tk.FLAT, bd=0, cursor="hand2",
                    highlightthickness=0)
    btn.pack(side=tk.BOTTOM, pady=10)
    
    # Add hover effect binding
    def on_enter(e):
        btn.config(bg="#00ffff")
    
    def on_leave(e):
        btn.config(bg="#00d4ff")
    
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Threading Instantiation Safe Wrapper
def start_assistant_thread():
    status_dot.config(fg="#ffaa00")
    status_label.config(text="🎙️ Listening... • Processing your voice command", fg="#ffaa00")
    connection_label.config(text="⚡ Active • Receiving audio stream")
    main.update()
    threading.Thread(target=activate_assistant, daemon=True).start()

create_rounded_button()

# === Footer Information Bar ===
footer_frame = tk.Frame(main, bg='#1a1f2e', height=70)
footer_frame.pack(fill=tk.X)
footer_frame.pack_propagate(False)

# Info grid
info_container = tk.Frame(footer_frame, bg='#1a1f2e')
info_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=12)

info_items = [
    ("🔐", "Secure"),
    ("📡", "Local"),
    ("⚡", "Real-Time"),
    ("🛡️", "Protected")
]

for emoji, text in info_items:
    info_col = tk.Frame(info_container, bg='#1a1f2e')
    info_col.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    info_emoji = tk.Label(info_col, text=emoji, font=("Arial", 11), bg="#1a1f2e", fg="#00d4ff")
    info_emoji.pack()
    
    info_text = tk.Label(info_col, text=text, font=("Segoe UI", 8), bg="#1a1f2e", fg="#aaaaaa")
    info_text.pack()

# Bottom copyright/version
version_label = tk.Label(footer_frame, text="JARVIS v2.0 • AI Assistant Platform", 
                        font=("Segoe UI", 7), bg="#1a1f2e", fg="#555555")
version_label.pack(pady=(0, 5))

main.mainloop()