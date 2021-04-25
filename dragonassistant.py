#!/usr/bin/env python3
import speech_recognition as sr
import pyttsx3
import os
from colorama import Fore, Back, Style
import time
from difflib import SequenceMatcher
import datetime
from requests import get
import random

#Clear function to clear the terminal screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

#Starting Point
clr()
engine = pyttsx3.init()
engine.setProperty('voice','english-us')
engine.setProperty('rate',160)
engine.say("Hello master, I am Dragon Assistant and I will help you to make your life easier")

print(Fore.BLUE + "======================================\n\nGreetings! Welcome to Dragon Assistant\n", Fore.CYAN,"Version : 0.1",Fore.BLUE,"\n\n======================================")
engine.runAndWait()
        
#The Listener starts here
r = sr.Recognizer()
r.pause_threshold = 1
r.operation_timeout = 5
def listener(wtr=0):
    with sr.Microphone() as source:
        clr()
        if wtr:
            temp = "Say the city you want weather from"
            print(temp)
            engine.say(temp)
            engine.runAndWait()
        else:
            print(Fore.RED,"Give me instructions sir!\n")
            print(Fore.BLUE,"Listening...")
        audio = r.listen(source,phrase_time_limit=5)
        print(Fore.GREEN,"Recognizing...\n\n")
        try:
            heard = r.recognize_google(audio)
            print(Fore.GREEN,"I heard",heard)
            return heard.lower()
        except sr.UnknownValueError:
            engine.say("I didnt understand what u said")
            print(Fore.RED,"You said something that is beyond my understanding master or maybe you didn't say anything.\n")
            engine.runAndWait()
            return 0
        except sr.RequestError:
            engine.say("Please check your internet connection")
            print(Fore.RED,"Please check your internet connection")
            engine.runAndWait()
            return 0
            
def match(orig,a): 
    seq = SequenceMatcher(None, a, orig)
    ratio = seq.ratio()
    if ratio >= 0.75:
        return True
    else:
        return False

def matches(): 
    a = listener()   
    if a:
        if match("start minecraft",a) == True:
            engine.say("Alright I heard you, starting minecraft")
            print(Style.RESET_ALL)
            engine.runAndWait()
            #The scripts which have .sh at the end are FrosT's specific script, as a todo add a env variable which makes FrosT specific features to be true
            os.system("bash $HOME/games/startminecraft.sh ")
            input()
            matches()
        elif match("what is time",a) == True:
            now = datetime.datetime.now()
            timen = now.strftime('%I:%M')
            out = "Current time is" + timen
            engine.say(out)
            print(Fore.YELLOW,"Current time is,",timen)
            engine.runAndWait()
            input()
            matches()
        elif match("what is temperature",a) == True:
            city = listener(wtr=1)
            if city:
                LANG = "english"
                URL = f"http://wttr.in/{city}?lang={LANG}&format=j1"
                result = get(URL).json()
                weather = result["current_condition"][0]
                out = f"The temperature in {city} is" + weather["temp_C"]
                engine.say(out)
                print(Fore.YELLOW,"Current temperature of {0} is,".format(city),weather["temp_C"],"^C")
                engine.runAndWait()
                input()
                matches()
            else:
                print(Fore.RED,"Invalid Input, press enter to restart the assistant")
                input()
                matches()
        elif match("start firefox", a):
            engine.say("Okay master, starting firefox browser")
            engine.runAndWait()
            os.system("firefox") #Firefox and linux are love
            input()
            matches()
        elif match("browse website", a):
            engine.say("Please enter the website you want to visit")
            engine.runAndWait()
            website = input(f"{Fore.CYAN}Please enter the website you want to visit: ")
            os.system(f"firefox {website}")
            input()
            matches()
        elif match("play music", a):
            engine.say("Playing a random music from Musics folder")
            engine.runAndWait()
            HOME = os.environ.get("HOME")
            music_dir = f"{HOME}/Music/fav/"
            songs = os.listdir(music_dir)
            print(Style.RESET_ALL)
            os.system("play {0}{1}".format(music_dir,random.choice(songs)))
            input()
            matches()
        elif match("start telegram", a):
            engine.say("Cool, starting telegram")
            engine.runAndWait()
            print(Fore.YELLOW,"Opening Telegram")
            os.system("bash $HOME/Desktop/Telegram.sh") 
            input()
            matches()  
        elif match("reboot", a):
            a = input(f"{Fore.RED}Are you sure about that? (Y/n)(Case sensitive): ")
            if a == "Y":
                engine.say("Okay master, rebooting the system")
                print(Fore.RED,"Okay master, rebooting the system")
                engine.runAndWait()
                print(Style.RESET_ALL)
                os.system("reboot") #This only works on linux btw, if you are a windows user find the command urself or ditch windows :p
            else:
                print(Fore.YELLOW,"Skipped Rebooting, starting bot again in 1s")
                time.sleep(1)
                matches()
        elif match("dragon help", a):
            out = "\n\nHello there, this is dragon assistant speaking to you. I am here to help you with with a lot of things, check matches function of this python code to know what are the commands available. You can even modify that function to add your own custom commands. I am owned by Yash Patil or FrosT"
            print(Fore.GREEN, out)
            engine.say(out)
            engine.runAndWait()
            input()
            matches()   
        elif match("dragon quit", a):
            engine.say("Alright master, hope to see you soon. Thanks for using me")
            print(Fore.RED,"Exiting...")
            engine.runAndWait()
            print(Style.RESET_ALL)       
            exit()
        else:
            engine.say("Looks like you said something that is not known to me")
            print(Fore.RED,"I didnt understand what u just said, please try again by pressing enter")
            engine.runAndWait()
            input()
            matches()
    else:
        print(Fore.RED,"I didnt understand what you just said. Press enter to try again")
        input()
        matches()

try: 
    matches()
except KeyboardInterrupt:
    print(Fore.GREEN,"\n\nGot Signal to Exit, Thank You for using Dragon Assistant")
    engine.say("Exiting, Thank you master see you soon")
    print(Style.RESET_ALL)
    engine.runAndWait()

