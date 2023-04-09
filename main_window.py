
# print("MAIN MAIN MAIN")
from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from tkinter import *
import tkinter as tk
import widthHeightDevice as dimensions

import homepage as home

# print(" MAIN MIAN")

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_homepage():
    # window.withdraw()
    home.homepage()

window = tk.Tk()
window.title("Main Window")


window.geometry("1440x900")
# window.geometry(f"{dimensions.width}x{dimensions.height}")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 900,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)



welcome_secureLabs = PhotoImage(
    file=relative_to_assets("welcome_secureLabs_button.png"))
welcome_secureLabs_button = Button(
    window,
    image=welcome_secureLabs,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_homepage(),
    relief="flat"
)
welcome_secureLabs_button.place(
    x=20.0,
    y=12.0,
    width=1400.0,
    height=875.0
)
window.resizable(False, False)
window.mainloop()