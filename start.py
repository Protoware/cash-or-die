# libraries

from sys import exit
from os import name, system
from colorama import Fore, init
init()

from core.home.core_h import home
from core.functions.core_f import clear, get_input, reset_c, exit_check



# Data

storage  =   0
tokens   =   0
bread    =   0
cash     =   0


# main

def main(name: str):
    global storage, tokens, bread, cash
    clear()
    home(name, tokens, bread, cash, storage)
    i = get_input()
    exit_check(i)

    if i == "1":
        return 0

    main(name)


# start

def start():
    global storage, tokens, bread, cash, name
    storage = 300
    cash = 50
    clear()
    print("Welcome, good sir. What is your name?" + Fore.LIGHTBLUE_EX)
    name = input("$ ")
    name = name
    reset_c()

    main(name)

if __name__ == "__main__":
    start()

