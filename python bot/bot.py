import urllib.request
import urllib.parse
import re
from gtts import gTTS
#import pyttsx3 #pip install pyttsx3
import speech_recognition  as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
from pprint import pprint
import calendar

#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
# print(voices[1].id)
#engine.setProperty('voice', voices[0].id)

def textToSpeech(text):
 mytext = str(text)
 tts = gTTS(text=mytext, lang='en-in', slow=False)
 tts.save("sound.mp3")
 os.system("xdg-open sound.mp3")

def #speak(audio):
 engine.say(audio)
 engine.runAndWait()


def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
   ##speak("Good Morning!")
   #textToSpeech("Good Morning")

  elif hour>=12 and hour<18:
   ##speak("Good Afternoon!")   
   #textToSpeech("Good Afternoon")

  else:
   #speak("Good Evening!")  
   #textToSpeech("Good Evening")

   #speak("Please tell me how may I help you")       #I am Jarvis Sir. 
   #textToSpeech("Please tell me how may I help you")

def takeCommand():
 #It takes microphone input from the user and returns string output

 r = sr.Recognizer()
 with sr.Microphone() as source:
  print("Listening...")
  r.pause_threshold = 1
  audio = r.listen(source)

  try:
   print("Recognizing...")    
   query = r.recognize_google(audio, language='en-in')
   #print({query})
   #print(f"User said: {query}\n")

  except Exception as e:
   # print(e)    
   print("Say that again please...")  
   return "None"
  return query

def sendEmail(to, content):
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.ehlo()
 server.starttls()
 server.login('youremail@gmail.com', 'your-password')
 server.sendmail('youremail@gmail.com', to, content)
 server.close()

if __name__ == "__main__":
 wishMe()
 while True:
 # if 1:
  query = takeCommand().lower()

  # Logic for executing tasks based on query
  if 'wikipedia' in query:
   #speak('Searching Wikipedia...')
   #textToSpeech("Searching Wikipedia...")
   query = query.replace("wikipedia", "")
   results = wikipedia.summary(query, sentences=2)
   #speak("According to Wikipedia")
   print(results)
   #speak(results)

  elif 'open youtube' in query:
   #webbrowser.open("youtube.com")
   os.system("xdg-open http://youtube.com")

  elif 'open google' in query:
   #webbrowser.open("google.com")
   os.system("xdg-open http://google.com")

  elif 'open gmail' in query:
   #webbrowser.open("google.com")
   os.system("xdg-open https://mail.google.com/mail/u/0/")

  elif 'open facebook' in query:
   #webbrowser.open("google.com")
   os.system("xdg-open https://facebook.com")

  elif 'open twitter' in query:
   #webbrowser.open("google.com")
   os.system("xdg-open https://twitter.com")

  elif 'open stackoverflow' in query:
   #webbrowser.open("stackoverflow.com") 
   os.system("xdg-open http://stackoverflow.com")  


  elif 'play music' in query:
   music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
   songs = os.listdir(music_dir)
   print(songs)    
   os.startfile(os.path.join(music_dir, songs[0]))

  elif 'the time' in query:
   strTime = datetime.datetime.now().strftime("%H:%M:%S") 
   #speak(strTime)
   ##speak("hi")

  elif 'open code' in query:
   codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
   os.startfile(codePath)

  elif 'email to harry' in query:
   try:
    #speak("What should I say?")
    content = takeCommand()
    to = "harryyourEmail@gmail.com"    
    sendEmail(to, content)
    #speak("Email has been sent!")
   except Exception as e:
    print(e)
    #speak("Sorry my friend harry bhai. I am not able to send this email")  

  elif 'google search' in query:
   query = input("search any thing : ")
   for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
   	print(j)

  elif 'play video' in query:
   query_string = urllib.parse.urlencode({"search_query" : input("Enter video name")})
   html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
   search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
   print("http://www.youtube.com/watch?v=" + search_results[0])
   os.system("xdg-open http://www.youtube.com/watch?v=" + search_results[0])

  elif 'weather' in query:
   city = input('Enter your city : ')
   url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=4536f44834d9934ac8c56cdb48040857&units=metric'.format(city)
   res = requests.get(url)
   data = res.json()
   temp = data['main']['temp']
   wind_speed = data['wind']['speed']
   latitude = data['coord']['lat']
   longitude = data['coord']['lon']
   description = data['weather'][0]['description']
   print('Temperature : {} degree celcius'.format(temp))
   #speak('Temperature : {} degree celcius'.format(temp))
   print('Wind Speed : {} m/s'.format(wind_speed)) 
   #speak('Wind Speed : {} m/s'.format(wind_speed))
   print('Latitude : {}'.format(latitude))
   #speak('Latitude : {}'.format(latitude))
   print('Longitude : {}'.format(longitude))
   #speak('Longitude : {}'.format(longitude))
   print('Description : {}'.format(description))
   #speak('Description : {}'.format(description))

  elif 'change wallpaper' in query:
  	os.system("python3 data/wallpaper.py")

  elif 'take a selfi' in query:
  	os.system("python3 data/opencv.py")
  	print("saved in data")

  elif 'timer' in query:
  	os.system("python3 data/timer.py")
  elif 'news' in query:
  	os.system("news bbc-news")

  elif 'calendar' in query:
   yy = 2019
   mm = 9
   # display the calendar 
   print(calendar.month(yy, mm)) 
