from os import name, system
from colorama import Fore, init

def clear():
    if name == "nt":
        s = system("cls")
    else:
        s = system("clear")
def reset_c():
    print(Fore.RESET)

def get_input():
    i = input(Fore.LIGHTBLUE_EX + "$ ")
    if i == "" or " ":
        return "none"
    else:
        return i
