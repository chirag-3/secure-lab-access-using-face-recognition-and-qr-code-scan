



from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import homepage as hp

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame3")

def go_to_home():
    global window
    window.destroy()
    hp.homepage()

def wait(time):
    global window
    window.after(time, lambda: go_to_home())



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def go_to_home():
    global window
    window.destroy()
    hp.homepage()

def deny():

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
        text="ACCESS\nDENIED",
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
        595.0,
        anchor="nw",
        text="Sorry! Try Again",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )
    global image_image_1
    global try_again_button_image


    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        918.0,
        450.0,
        image=image_image_1
    )

    try_again_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    try_again_button = Button(
        window,
        image=try_again_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_to_home(),
        relief="flat"
    )
    try_again_button.place(
        x=95.0,
        y=675.0,
        width=212.0,
        height=53.0
    )
    window.resizable(False, False)
    # window.mainloop()

    wait(10000)
