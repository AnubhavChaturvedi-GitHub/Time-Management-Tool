import os
import time
import threading
from Notify_me import Alert
from Speak import speak
from offline_speak import Ospeak
from online_check import is_Online
from test import intro
import threading
from input_take import input_manage
from os import getcwd

def load_schedule(file_path):
    schedule = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if '=' in line:
                    line_time, activity = line.strip().split(' = ')
                    schedule[line_time.strip()] = activity.strip()
    except Exception as e:
        print(f"Error loading schedule: {e}")
    return schedule

def check_schedule(file_path):
    last_modified = 0
    while True:
        current_time = time.strftime("%I:%M%p")
        try:
            # Check file modification time
            modified = os.path.getmtime(file_path)
            if modified != last_modified:
                last_modified = modified
                schedule = load_schedule(file_path)
            
            if current_time in schedule:
                text = schedule[current_time]
                if is_Online():
                    t1 = threading.Thread(target=Alert, args=(text,))
                    t2 = threading.Thread(target=speak, args=(text,))
                else:
                    t1 = threading.Thread(target=Alert, args=(text,))
                    t2 = threading.Thread(target=Ospeak, args=(text,))
                
                t1.start()
                t2.start()
                t1.join()
                t2.join()
        
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(60)


intro("TMA - Tool")
if  is_Online():
    print("Welcome To the Time Management Assistant Tool")
    speak("Welcome To the Time Management Assistant Tool")
    print("@Cradit:Anubhav Chaturvedi")
else:
    print("Welcome To the Time Management Assistant Tool")
    Ospeak("Welcome To the Time Management Assistant Tool")
    print("©️Cradit: Anubhav Chaturvedi")
# Example usage:
file_path = fr'{getcwd()}\schedule.txt'

def Modifier():
    while True:
        pass_key = input()
        if "show" in pass_key:
            os.startfile(file_path)
        elif pass_key.startswith("tell me"):
            input_manage(pass_key)
        else:
            if is_Online():
                speak("Invalid Command")
                print('''
                      ______ Available commands _____
                      1. show - to show the Schedule file
                      2. tell me - try like "tell me to sleep at 09:00pm"
                      ''')
            else:
                Ospeak("Invalid Input")

t1 = threading.Thread(target=check_schedule,args=(file_path,))
t2 = threading.Thread(target=Modifier)
t1.start()
t2.start()
t1.join()
