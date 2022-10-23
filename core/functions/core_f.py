from os import name, system
from colorama import Fore, init, Style

def clear():
    if name == "nt":
        s = system("cls")
    else:
        s = system("clear")

def reset_c():
    print(Fore.RESET)

def get_input():
    i = input(Fore.LIGHTBLUE_EX + "$ ")
    return i

def exit_check(inp):
    if inp == "4":
        print(Fore.YELLOW + "Are you sure..? y/n" + Fore.RESET)
        c = get_input()
        if c == "y":
            print(Fore.WHITE + Style.BRIGHT + "Alright, goodbye!" + Fore.RESET + Style.RESET_ALL)
            exit()
