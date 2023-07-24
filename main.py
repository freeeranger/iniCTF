import os
import sys
from sys import platform
from pathlib import Path
import shutil
from colorama import Fore, Style
import select_menu

print(f"Welcome to iniCTF, let the hacking begin >:) (press {Fore.MAGENTA}q{Style.RESET_ALL} to abort)")

config_path = ""

# set config path depending on platform
if platform in ("linux", "linux2"):
    # todo implement this
    pass
elif platform == "darwin":
    config_path = f"{str(Path.home())}/Library/Application Support/inictf"
elif platform == "win32":
    # todo implement this
    pass

if not os.path.exists(config_path):
    os.makedirs(config_path)

# exit on empty config folder
if not os.listdir(config_path):
    print(f"Templates folder is empty. To add templates, go to {config_path}.")
    print("For more information, see the documentation on github.")
    sys.exit()

# category select menu
categories = [f for f in Path(config_path).iterdir() if f.is_dir()]
category = select_menu.select(options=[i.name for i in categories], clear_at_end=True)

if category is None:
    print("IniCTF was aborted.")
else:
    # exit on empty category folder
    if not os.listdir(f"{config_path}/{category}"):
        print(f"The folder {Fore.MAGENTA}{category}{Style.RESET_ALL} contains no templates.")
        print(f"To add templates, go to {config_path}.\nFor more information, see the documentation on github.")
        sys.exit()

    # template select menu
    templates = [f for f in Path(f"{config_path}/{category}").iterdir() if f.is_dir()]
    template = select_menu.select(options=[i.name for i in templates], clear_at_end=True)

    # Copy the template files to the current directory
    if template is not None:
        print(f"Creating {Fore.MAGENTA}{template}{Style.RESET_ALL}...")

        files = list(Path(f'{config_path}/{category}/{template}').iterdir())
        for f in files:
            shutil.copyfile(f"{f}", f"./{f.name}")

        print("Done!")
