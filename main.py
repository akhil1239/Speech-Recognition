import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            # if 'google' in command:
                # command = command.replace("google", "")
                # talk(command)
            print(command)
            
    except:
        pass
    return command

def run():
    
    command = take_command()
    # print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "open youtube" in command:
        talk("opening youtube")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(time)
    elif "thank" in command:
        talk("its my pleasure to help you sir")
    elif "born" in command:
        # p = command.replace("who is", "")
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    elif "joke" in command:
        a= (pyjokes.get_joke())
        print(a)
        talk(a)
    elif "quit" in command:
        global x
        x= False
        print("Terminated...")

wish = int(datetime.datetime.now().hour)
if wish>=0 and wish<12:
    talk("Good Morning Sir, what can i do for you")
else:
    talk("Good evening sir, what can i do for you")

x=True
while x:
    run()