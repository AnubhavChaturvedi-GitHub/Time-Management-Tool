import time
import colorama
from colorama import Fore, Back, Style
from pyfiglet import Figlet
import os
import threading
from playsound import playsound
from os import getcwd

# Initialize colorama
colorama.init()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print a styled message
def print_styled_message(message, font="starwars"):
    clear_screen()
    figlet = Figlet(font=font)
    styled_text = figlet.renderText(message)
    for char in styled_text.rstrip('\n'):
        print(Fore.BLUE + char, end='', flush=True)
        time.sleep(0.009)  # Adjust the speed of animation here (in seconds)
    print(Style.RESET_ALL)


def intro(text):
    t1 = threading.Thread(target=print_styled_message,args=(text,))
    t2 = threading.Thread(target=playsound,args=(fr"{getcwd()}\clock-alarm-8761.mp3",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
