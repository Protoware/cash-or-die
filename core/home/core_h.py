from colorama import Fore, init, Style
import colorama
init()

def home(name: str, tokens: int, bread: int, cash: int, storage: int) -> str:
    top = Style.DIM + Fore.LIGHTMAGENTA_EX + """
    Welcome, {}
    """.format(name) + Fore.RESET + Style.RESET_ALL

    main = Style.BRIGHT + Fore.YELLOW + "Tokens: {}".format(tokens) + Fore.RESET + Fore.WHITE + "   Bread: {}".format(bread) + Fore.RESET + Fore.LIGHTGREEN_EX + "   Cash: {}/{}\n".format(cash, storage) + Fore.RESET + Style.RESET_ALL
    
    option = Style.DIM + Fore.CYAN + "\n\n    Commands" + Fore.RESET + Style.RESET_ALL
    option2 = """
    1 - Shop
    2 - Mark's Casino
    3 - Belly's Store
    """
    option3 = Style.BRIGHT + Fore.RED + "4 - Quit game" + Fore.RESET + "\n" + Style.RESET_ALL

    final = top + main + option + option2 + option3
    print(final)
