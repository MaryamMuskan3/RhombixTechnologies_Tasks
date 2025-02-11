import os
import time
import pygame
import speech_recognition as sr
import webbrowser
import pywhatkit as kit
import pyautogui
from gtts import gTTS
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def speak(text):
    filename = "newaudio.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    pygame.mixer.quit()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(f"You said: {said}")
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()


def launch_application(app_name):
    speak(f"Opening {app_name}")
    if "notepad" in app_name:
        os.system("notepad")
    elif "chrome" in app_name:
        os.system("start chrome")
    elif "calculator" in app_name:
        os.system("calc")
    else:
        print("Sorry, I can't open that application.")


def play_youtube(song_name):
    speak(f"Playing {song_name}")
    url = f"https://www.youtube.com/results?search_query={song_name}"
    webbrowser.open(url)


def search_google(query):
    speak(f"Searching {query}")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def search_gemini(query):
    speak("Searching with Gemini")
    response = model.generate_content(query)
    if response and response.text:
        gemini_response = response.text
        print("Gemini: ", gemini_response)
        
        lines = gemini_response.split("\n")[:5]
        short_response = " ".join(lines)
        
        speak(short_response)
    else:
        print("Sorry, I couldn't find an answer.")
        speak("Sorry, I couldn't find an answer.")


def send_whatsapp_message():
    speak("Please say the contact number.")
    number = get_audio().replace(" ", "")
    if not number.startswith("+"):
        number = "+92" + number.lstrip("0") 
    speak("What message do you want to send?")
    message = get_audio()

    if number and message:
        kit.sendwhatmsg_instantly(number, message)
        time.sleep(15) 
        
        pyautogui.press("enter")
        speak(f"Message sent successfully.")

    else:
        speak("Invalid number or message. Please try again.")

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        text = get_audio()
        
        if "stop" in text:
            speak("Stopping voice assistant. Goodbye!")
            break
        
        elif "open" in text:
            app_name = text.replace("open", "").strip()
            launch_application(app_name)
        
        elif "play" in text:
            song_name = text.replace("play", "").strip()
            play_youtube(song_name)
        
        elif "search" in text:
            query = text.replace("search", "").strip()
            search_google(query)
        
        elif "discuss" in text:
            query = text.replace("discuss", "").strip()
            search_gemini(query)
        
        elif "send message" in text:
            send_whatsapp_message()