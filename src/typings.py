from pyfiglet import Figlet
import os
import sys
import time
from colorama import Fore, Style

typing_speed = 0.06
font = Figlet(font="slant")


def typing(text, is_input=False, speed=typing_speed, color=Fore.LIGHTCYAN_EX):

    sys.stdout.write(color)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

    time.sleep(speed)
    sys.stdout.write("\n")
    sys.stdout.flush()
    sys.stdout.write(Style.RESET_ALL)
