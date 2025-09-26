import speech_recognition as sr
import pyttsx4
import os
import webbrowser
from dotenv import load_dotenv
import time
import musiclibrary
import requests
from openai import OpenAI

load_dotenv()


api_opK = os.getenv("OPENAI_API_KEY")
newsapi = os.getenv("NEWSAPI_KEY")

#recognize google :- for listening of the ai
spotify = "https://open.spotify.com/album/0Rkv5iqjF2uenfL0OVB8hg?flow_ctx=7f3a8bd2-2e95-470f-a4a6-2c56a4bcf2e0%3A1758756060#login"


recognizer = sr.Recognizer()
engine = pyttsx4.init()
# Set female voice (usually index 1 on Windows)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty('rate', 150)


def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("TTS error:", e)
        
def aiProcess(command):
    client = OpenAI(
    api_key = api_opK
)
    response = client.chat.completions.create(
        model="gpt-4.1-mini",   # or gpt-4.1, gpt-4o-mini, etc.
        messages=[
            {"role": "system", "content": "you are a AI named Alina skilled in task like Alexa and Google Assistant give short responses"},
            {"role": "user", "content": command}
        ]
    )

    return response.choices[0].message.content

    
def processcmnd(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open rana ji ki profile" in c.lower():
        webbrowser.open("https://github.com/rana-ji0001")
    elif "play music on spotify" in c.lower():
        webbrowser.open(spotify)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            for article in articles:
                title = article.get("title", "No title available")
                print(title)
                speak(title)    
    else:
        #let openAI handle the request
        output = aiProcess(command)
        speak(output)
    
        
        


if __name__ == "__main__":
    speak("Initializing Elina...")
    # listen for the wake word EVE
    # this will obtain audio from the microphone
    
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
                
            word = r.recognize_google(audio)
            
            if "alina" in word.lower():
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Elina Active---")
                    audio = r.listen(source)
                
                
                command = r.recognize_google(audio)
                print(command)
                processcmnd(command)
                speak("Done")
        except Exception as e:
            print("Error; {0}".format(e))
