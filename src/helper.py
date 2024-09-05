import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()

GOOGLE_API_KEY = os.getenv("Google_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def voice_input():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
        
    try:
        text= r.recognize_google(audio)
        print("you said: ",text)
        return text
    except sr.UnKnownValueError:
        print("sorry could not understand the audio")
    except sr.RequestError as e:
        print("could not request from google speech recognization service: {0}".format(e))    
            
    

def llm_model(user_text):
    genai.configure(api_key = GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_text)
    result=response.text
    return result

def text_to_speech(text):
    tts = gTTS(text=text,lang="en")
    
    tts.save("speech.mp3")