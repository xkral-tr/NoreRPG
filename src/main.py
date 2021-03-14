import os
from colorama import Fore, Back, Style
# import playsound
import struct
from typings import typing
from load_sprite import load_sprite
from load_script import load_script, load_yaml
from pyfiglet import Figlet

os.system("cls")
font = Figlet(font="slant")

typing(font.renderText("NoreRPG"), speed=0.001, color=Fore.LIGHTBLUE_EX)

typing("Welcome friend!")
typing("Your adventure is starting but before that...")
typing("You need to learn commands")
typing("If you forgot the commands")
typing("Dont worry just type 'help'")

typing("Commands:")
typing("- shop")
typing("- quit")
typing("- info")

running = True

while running:
    user_input = input(Fore.YELLOW + ">> " + Style.RESET_ALL)
    print(user_input)
    os.system("cls")

    if user_input == "quit":
        typing("Goodbye!")
        running = False
    elif user_input == "info":
        pass
    elif user_input == "shop":
        load_script(load_yaml("shop"))
