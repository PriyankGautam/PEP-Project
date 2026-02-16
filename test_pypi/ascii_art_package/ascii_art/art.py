from colorama import Fore, Style, init

init(autoreset=True)

colors = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE
}

def get_color(color_name):
    return colors.get(color_name.lower(), Fore.YELLOW)


def cat(color="yellow"):
    c = get_color(color)
    return c + r"""
 /\_/\  
( o.o ) 
 > ^ <
""" + Style.RESET_ALL


def panda(color="white"):
    c = get_color(color)
    return c + r"""
  ⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀
  ⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣦
  ⠀⠀⣾⣿⠿⠛⠉⠉⠛⠿⣿⣷
  ⠀⣾⣿⣇⠀⣾⣿⣷⠀⣾⣿⣇⣿⣷
  ⠀⣿⣿⣿⣷⣤⣤⣤⣷⣿⣿⣿
  ⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⠀⠀⠉⠛⠿⣿⣿⣿⠿⠛⠉
""" + Style.RESET_ALL


def smiley(color="cyan"):
    c = get_color(color)
    return c + r"""
  _______
 /       \
|  O   O  |
|    ^    |
|  \___/  |
 \_______/
""" + Style.RESET_ALL


def hello():
    return Fore.MAGENTA + "Hello from ASCII Art Package! 🎨🐼😺" + Style.RESET_ALL
