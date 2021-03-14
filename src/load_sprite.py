from colorama import Fore, Style


def load_sprite(path):
    file = open(path + ".sprite", "r", encoding="utf-8")
    print(Fore.LIGHTBLUE_EX + file.read() + Style.RESET_ALL)
