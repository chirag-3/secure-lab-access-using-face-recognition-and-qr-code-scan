


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import homepage as hp

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame4")

def go_to_home():
    global window
    window.destroy()
    hp.homepage()

def wait(time):
    global window
    window.after(time, lambda: go_to_home())

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def grant():
    global window

    window = Toplevel()

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
    canvas.create_text(
        40.0,
        30.0,
        anchor="nw",
        text="SecureLabs",
        fill="#000000",
        font=("Poppins SemiBold", 25 * -1)
    )

    canvas.create_text(
        38.0,
        311.0,
        anchor="nw",
        text="ACCESS\nGRANTED",
        fill="#000000",
        font=("Poppins SemiBold", 45 * -1)
    )

    canvas.create_text(
        40.0,
        783.0,
        anchor="nw",
        text="Redirecting to Homepage in 10 seconds",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )

    canvas.create_text(
        40.0,
        618.0,
        anchor="nw",
        text="Thank You very much.\n",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )
    global image_image_1

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        918.0,
        450.0,
        image=image_image_1
    )

    wait(10000)
    
    window.resizable(False, False)
    # window.mainloop()
