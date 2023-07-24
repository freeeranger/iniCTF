import os
import sys
from pathlib import Path
import shutil
from colorama import Style
import select_menu
from config_handler import config_path, accent_color

print(f"Welcome to iniCTF, let the hacking begin >:) (press {accent_color}q{Style.RESET_ALL} to abort)")

if config_path is None:
    print("Platform not recognized, aborted.")
    sys.exit()

if not os.path.exists(config_path):
    os.makedirs(config_path)

# exit on empty config folder
if not os.listdir(config_path):
    print(f"No templates found. To add templates, go to {config_path}.")
    print("For more information, see the documentation on github.")
    sys.exit()

# category select menu
categories = [f for f in Path(config_path).iterdir() if f.is_dir()]
category = select_menu.select(options=[i.name for i in categories], clear_at_end=True)

if category is None:
    print("IniCTF was aborted.")
    sys.exit()
else:
    # exit on empty category folder
    if not os.listdir(f"{config_path}/{category}"):
        print(f"The folder {accent_color}{category}{Style.RESET_ALL} contains no templates.")
        print(f"To add templates, go to {config_path}.\nFor more information, see the documentation on github.")
        sys.exit()

    # template select menu
    templates = [f for f in Path(f"{config_path}/{category}").iterdir() if f.is_dir()]
    template = select_menu.select(options=[i.name for i in templates], clear_at_end=True)

    # Copy the template files to the current directory
    if template is not None:
        print(f"Creating {accent_color}{template}{Style.RESET_ALL}...")

        files = list(Path(f'{config_path}/{category}/{template}').iterdir())
        for f in files:
            shutil.copyfile(f"{f}", f"./{f.name}")

        print("Done!")
