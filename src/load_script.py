import yaml
from typings import typing
from load_sprite import load_sprite
import os
from colorama import Fore, Style

SCRIPTS_PATH = "scripts"
SPRITES_PATH = "assets"


def make_input():
    return input(Fore.YELLOW + ">> " + Style.RESET_ALL)


def load_yaml(path):
    file = open(f"{SCRIPTS_PATH}/{path}.yml")
    return yaml.safe_load(file.read())


def load_script(data):
    for step in data:
        # Load Sprite
        if "load_sprite" in step:
            sprite_name = step["load_sprite"]
            load_sprite(f"{SPRITES_PATH}/{sprite_name}")

        # Load Multiple Sprites
        if "load_sprites" in step:
            for sprite in step["load_sprites"]:
                load_sprite(f"{SPRITES_PATH}/{sprite}")

        # Clear
        if "clear" in step:
            os.system("cls")

        # Texts
        if "text" in step:
            typing(step["text"])

        # Input
        if "input" in step:
            input_section = step["input"]
            selected_option = make_input()
            for option in input_section:
                if selected_option == option:
                    load_script(input_section[option])
