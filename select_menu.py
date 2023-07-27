from pynput import keyboard
from colorama import Style
from config_handler import config, selector_color

state = {
    "options": [],
    "selected": 0,
    "longest": 0,
}

aborted = False

def show_menu():
    index = 0
    for i in state["options"]:
        # special styling if the current option is selected
        pre_selector = selector_color + config["appearance"]["pre_selector"] + " " if index == state["selected"] else " " * (len(config["appearance"]["pre_selector"]) + 1)
        post_selector = " " + config["appearance"]["post_selector"] if index == state["selected"] else " " * (len(config["appearance"]["post_selector"]) + 1)

        print(pre_selector + f"{i}".ljust(state["longest"], ' ') + post_selector + Style.RESET_ALL)
        index += 1


def clear_menu():
    print("\033[A" * (len(state["options"]) + 1))


def navigate_up():
    if state["selected"] == 0:
        if config["general"]["navigation_wrap"]:
            state["selected"] = len(state["options"]) - 1
        else:
            await_input()
            return
    else:
        state["selected"] -= 1

    clear_menu()
    show_menu()
    print("\033[A")
    await_input()


def navigate_down():
    if state["selected"] == len(state["options"]) - 1:
        if config["general"]["navigation_wrap"]:
            state["selected"] = 0
        else:
            await_input()
            return
    else:
        state["selected"] += 1

    clear_menu()
    show_menu()
    print("\033[A")
    await_input()


def on_press(key):
    global aborted
    try:
        if key == keyboard.Key.up:
            navigate_up()
            return False
        if key == keyboard.Key.down:
            navigate_down()
            return False
        if key == keyboard.Key.enter:
            return False
        if key.char == "q":
            aborted = True
            return False
    except AttributeError as _:
        pass
    return True

def await_input():
    listener = keyboard.Listener(on_press=on_press, suppress=True)
    listener.start()
    listener.join()


def select(options, clear_at_end = False):
    global aborted 
    
    # reset data when function is run
    state["selected"] = 0
    state["options"] = options
    
    # maintain padding between runs
    longest_option = max(len(i) for i in options)
    state["longest"] = state["longest"] if state["longest"] >= longest_option else longest_option

    show_menu()
    await_input()

    if clear_at_end:
        # clear all input from the select menu
        print("\033[A\033[2K" * (len(options)) + "\033[A")

    if aborted:
        aborted = False
        return None

    return options[state["selected"]]
