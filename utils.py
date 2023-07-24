from sys import platform

def is_windows():
    return platform == "win32"


def is_osx():
    return platform == "darwin"


def is_linux():
    return platform in ("linux", "linux2")
