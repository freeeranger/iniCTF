import sys
import tomllib
from pathlib import Path
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


def parse_config():
    with open(f"{get_config_path()}/inictf.toml", "rb") as f:
        try:
            print("ready")
            return tomllib.load(f)
        except Exception:
            print("Error parsing config.")
            sys.exit()


config = parse_config()
