

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame11")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x900")
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
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    326.5,
    497.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=112.0,
    y=475.0,
    width=429.0,
    height=42.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    326.5,
    405.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=112.0,
    y=383.0,
    width=429.0,
    height=42.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    1055.0,
    450.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=112.0,
    y=611.0,
    width=429.0,
    height=53.0
)

canvas.create_text(
    112.0,
    254.0,
    anchor="nw",
    text="Admin Log In ",
    fill="#000000",
    font=("Poppins Medium", 30 * -1)
)

canvas.create_text(
    129.0,
    451.0,
    anchor="nw",
    text="Password ",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    129.0,
    359.0,
    anchor="nw",
    text="Username ",
    fill="#000000",
    font=("Poppins Medium", 16 * -1)
)

canvas.create_text(
    40.0,
    30.0,
    anchor="nw",
    text="SecureLabs",
    fill="#000000",
    font=("Poppins SemiBold", 25 * -1)
)
window.resizable(False, False)
window.mainloop()
