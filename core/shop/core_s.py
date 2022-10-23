from colorama import Fore, init, Style
import colorama
init()

def shop(tokens: int, bread: int, cash: int, storage: int) -> str:

    items = [
        "Storage upgrade"
    ]

    title = Fore.LIGHTMAGENTA_EX + "\n\r    Belly's Store" + Fore.RESET
    top = Fore.BLUE + """
    (° ͜ °) - "hello good sir... welcome"\n
    """ + Fore.RESET
    main = Style.BRIGHT + Fore.YELLOW + "Tokens: {}".format(tokens) + Fore.RESET + Fore.WHITE + "   Bread: {}".format(bread) + Fore.RESET + Fore.LIGHTGREEN_EX + "   Cash: {}/{}\n".format(cash, storage) + Fore.RESET + Style.RESET_ALL

    item1 = ""

    final = title + top + main
    print(final)

shop(30, 40, 20, 300)
