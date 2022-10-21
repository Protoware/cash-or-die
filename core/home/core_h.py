from colorama import Fore, init
init()

def home(name: str, tokens: int, bread: int, cash: int, storage: int) -> str:
    top = Fore.LIGHTMAGENTA_EX + """
    Welcome, {}
    """.format(name) + Fore.RESET

    main = Fore.YELLOW + "Tokens: {}".format(tokens) + Fore.RESET + Fore.WHITE + "   Bread: {}".format(bread) + Fore.RESET + Fore.LIGHTGREEN_EX + "   Cash: {}/{}".format(cash, storage) + Fore.RESET
    
    option = """

    Commands
    1 - Info
    2 - Shop
    3 - Mark's Casino
    4 - Belly's Store
    """

    final = top + main + option
    print(final)

