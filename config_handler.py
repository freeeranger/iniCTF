import sys
import os
import tomllib
from pathlib import Path
import tomli_w
import utils


def get_config_path():
    if utils.is_linux():
        # todo implement this
        return ""
    if utils.is_osx():
        return f"{str(Path.home())}/Library/Application Support/inictf"
    if utils.is_windows():
        # todo implement this
        return ""
    return None


def parse_config(path):
    # Create default config file if there is none
    if not os.path.isfile(f"{path}/inictf.toml"):
        with open(f"{path}/inictf.toml", "wb") as f:
            tomli_w.dump(default_config, f)

    with open(f"{path}/inictf.toml", "rb") as f:
        try:
            return tomllib.load(f)
        except Exception:
            print("Error parsing config.")
            sys.exit()


default_config = {
    "general": {
        "navigation_wrap": False
    },
    "appearance": {
        "pre_selector": "=>",
        "post_selector": "",
        "accent_color": "pink",
        "selector_color": "light_red"
    }
}

config_path = get_config_path()
config = parse_config(config_path)
accent_color = utils.parse_color(config["appearance"]["accent_color"])
selector_color = utils.parse_color(config["appearance"]["selector_color"])
