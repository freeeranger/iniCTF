from sys import platform
from colorama import Fore

def is_windows():
    return platform == "win32"


def is_osx():
    return platform == "darwin"


def is_linux():
    return platform in ("linux", "linux2")


# Converts color strings to colorama colors
def parse_color(color):
    match color:
        case "light_blue":
            return Fore.LIGHTBLUE_EX
        case "blue":
            return Fore.BLUE
        case "light_green":
            return Fore.LIGHTGREEN_EX
        case "green":
            return Fore.GREEN
        case "light_red":
            return Fore.LIGHTRED_EX
        case "red":
            return Fore.RED
        case "pink":
            return Fore.LIGHTMAGENTA_EX
        case "magenta":
            return Fore.MAGENTA
        case "light_yellow":
            return Fore.LIGHTYELLOW_EX
        case "yellow":
            return Fore.YELLOW
        case "light_cyan":
            return Fore.LIGHTCYAN_EX
        case "cyan":
            return Fore.CYAN
        case "white":
            return Fore.LIGHTWHITE_EX
        case "light_gray":
            return Fore.WHITE
        case "gray":
            return Fore.LIGHTBLACK_EX
        case "black":
            return Fore.BLACK
        case _:
            return Fore.RESET
