import sys
import os
import tomllib
from pathlib import Path
import tomli_w
from colorama import Style
import utils


# Returns the appropriate config path depending on os
def get_config_path():
    if utils.is_linux():
        return f"{str(Path.home())}/.config/inictf"
    if utils.is_osx():
        return f"{str(Path.home())}/Library/Application Support/inictf"
    if utils.is_windows():
        backslash = "\\"
        return f"{str(Path.home()).replace(backslash, '/')}/AppData/Roaming/inictf"
        return ""
    print("Platform not recognized, aborted.")
    sys.exit()


# Parses the config file into a dictionary
def parse_config(path):
    # Create config folder if there is none
    if not os.path.isdir(path):
        os.makedirs(path)

    # Create default config file if there is none
    if not os.path.isfile(f"{path}/inictf.toml"):
        with open(f"{path}/inictf.toml", "wb") as f:
            tomli_w.dump(default_config, f)

    with open(f"{path}/inictf.toml", "rb") as f:
        try:
            toml = tomllib.load(f)
            validate_config(toml)
            return toml
        except Exception:
            print("Error parsing config.")
            sys.exit()


def validate_config(toml):
    found_errors = False

    color = utils.parse_color(default_config["appearance"]["accent_color"])

    error_messages = []

    for category, items in default_config.items():
        for item in items.items():
            if category in toml and item[0] in toml[category]:
                if type(toml[category][item[0]]) is not type(item[1]):
                    error_messages.append(
                        f"The setting {color}{category}.{item[0]}{Style.RESET_ALL} is of the wrong type."
                    )
                    found_errors = True
                else:
                    if "color" in item[0]:
                        if utils.parse_color(toml[category][item[0]]) is None:
                            error_messages.append(
                                f"The setting {color}{category}.{item[0]}{Style.RESET_ALL} references an invalid color: {color}{toml[category][item[0]]}{Style.RESET_ALL}"
                            )
                            found_errors = True
            else:
                error_messages.append(
                    f"The setting {color}{category}.{item[0]}{Style.RESET_ALL} is not present in the config."
                )
                found_errors = True

    if found_errors:
        print("Aborted due to errors found in config:")
        for message in error_messages:
            print(f" - {message}")
        sys.exit()


default_config = {
    "general": {"navigation_wrap": False},
    "appearance": {
        "pre_selector": "=>",
        "post_selector": "",
        "accent_color": "pink",
        "selector_color": "light_red",
    },
}

config_path = get_config_path()
config = parse_config(config_path)
accent_color = utils.parse_color(config["appearance"]["accent_color"])
selector_color = utils.parse_color(config["appearance"]["selector_color"])
