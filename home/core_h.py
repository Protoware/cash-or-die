from colorama import Fore, init
init()

def home(name: str, tokens: int, bread: int, cash: int, storage: int) -> str:
    top = Fore.LIGHTMAGENTA_EX + """
    Welcome, {}
    """.format(name) + Fore.RESET

    main = Fore.YELLOW + "\n    Tokens: {}".format(tokens) + Fore.RESET + Fore.WHITE + "   Bread: {}".format(bread) + Fore.RESET + Fore.LIGHTGREEN_EX + "   Cash: {}/{}".format(cash, storage)

    final = top + main
    print(final)


# Testing
home("Ivan", 20, 30, 10, 300)

