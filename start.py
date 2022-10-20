# libraries

from sys import exit
from os import name, system
from colorama import Fore, init
init()

# custom libraries

from core.home.core_h import home


# functions

def clear():
    if name == "nt":
        s = system("cls")
    else:
        s = system("clear")
def reset_c():
    print(Fore.RESET)


# main

def main():
    print("Welcome, good sir. What is your name?" + Fore.LIGHTBLUE_EX)
    name = input("$ ")
    reset_c()


if __name__ == "__main__":
    main()

