import speech_recognition as sr
import datetime

import webbrowser

import requests
import json

recognizer = sr.Recognizer()

def recordAudio():
    with sr.Microphone() as source:
        print("Please Speak...")
        audio = recognizer.listen(source)
    return audio

def speechRecognize(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understood, please retry")
        return ""
    except sr.RequestError:
        print("Something wen't wrong, please retry!")
        return ""

def weather(city):
    api_key = "add API KEY there...."
    
    complete_url ="https://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key + "&q=" + city
    res = requests.get(complete_url)
    data = res.json()


    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"] - 273.15
        
        return f"The weather in {city} is {weather_desc} with a temperature of {temp:.2f}°C."
    else:
        return "Not found."

def respond(text):
    if "hello" in text:
        print("Hello! How can I assist you today?")
        
    elif "time" in text:
        now = datetime.datetime.now()
        
        print(f"The current time is {now.strftime('%H:%M:%S')}")
    elif "date" in text:
        today = datetime.date.today()
        
        print(f"Today's date is {today.strftime('%B %d, %Y')}")
    elif "search" in text:
        query = text.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        print(f"Searching for {query}")
        webbrowser.open(url)
    
    elif "weather" in text:
        city = text.replace("weather in", "").strip()
        print(weather(city))
    else:
        print("Sorry, I can only respond to 'Hello', tell the time or date, search the web for information and provide weather updates.")

audio = recordAudio()
command = speechRecognize(audio)
respond(command)
