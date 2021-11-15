import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import random
import smtplib
from email.message import EmailMessage
from forecast import forecast

engine = pyttsx3.init()
engine.setProperty('voice', 'english')
# voices = engine.getProperty('voices')
engine.setProperty('rate', 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    """
    Todo: write doc string 
    """
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour <= 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello I am jarvis your personal assistant")

def takeCommand():
    """
    it takes Microphone input from the user and returns text
    """

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source) 
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
        
    try:
        print("Recognising.... ")
        query = r.recognize_google(audio,language='en=in')
        print(f"User said: {query}")
    except Exception as e:
        print("Please speak Again")
        return "None"

    return query

def sendMail(to,content,subject="Babu"):
    """
        this function is used to send email to the recipient
        Params:
        to: The email address of the person who will receive this email
        content: The content is the data that you want to send to the receipient
        subject: Optional subject of the email
    """
    # Get email and password from environment variables
    email = os.environ.get('jheel_addr')
    password = os.environ.get('fakePass')

    # conenct and login to SMTP server
    server = smtplib.SMTP('smtp-mail.outlook.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)

    # create a message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = email
    msg.set_content(content)
    # done creating message
    server.send_message(msg)

    server.close()

def forecast_weather(state):
    """ This function will return a string which contains the forecasts for the particular place
        Params:
        state: it is the name of the state that you want the weather forecast
    """

    weather_state = forecast(state)

    weather_string = f"Weather forecast for {weather_state['place']} on {weather_state['date']} is..."

    weather_string += f"\nThe weather in the day... {weather_state['day']['narrative']}. The temperature will be {weather_state['day']['temperature']} degree celsius, Uv description {weather_state['day']['uv_description']}  "

    return weather_string



if __name__ == "__main__":
    greet()
    # sendMail('jowiha1371@funboxcn.com', "Hello there I am very good")
    
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on queries
        if 'wikipedia' in query:
            speak ("Searching Wikipedia")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = "/home/demon/Music/gintama/"
            songs = os.listdir((music_dir))
            random_song = random.choice(songs)
            subprocess.call(['open',os.path.join(music_dir,random_song)])
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")

        elif 'open code' in query:
            speak("Opening visual studio code")
            subprocess.call(['code'])

        elif 'email to babu' in query:
            try:
                speak("What do you want to send?")
                content = takeCommand()
                to = "jowiha1371@funboxcn.com"
                speak("Sending email")
                sendMail(to, content)
                speak("Sent email")
            except Exception as e:
                print(e)
                speak("sorry I couldn't send that email")
        
        elif 'quit'  in query:
            speak("Okay sir, Byee")
            exit()

        # Search query on google
        elif "google search" in query:
            # Get the second element as it is the query string
            search_query = query.split("google search ")[1]
            speak(f"Searching {search_query}")
            webbrowser.open(f'https://www.google.com/search?q={search_query}')

        elif "weather" in query:
            speak("Which state do you live in?")
            state = takeCommand()
            weather = forecast_weather(state)
 