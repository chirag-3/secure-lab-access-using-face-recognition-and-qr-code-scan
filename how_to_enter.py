
from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import homepage as home
import face_detection1 as fd
import register as rp

def enter_home():
    global window_guide
    window_guide.destroy()
    home.homepage()

def enter_lab():
    global window_guide
    window_guide.destroy()
    fd.detect_face()
    
def register_user():
    global window_guide
    window_guide.destroy()
    rp.register()


def enter_guide():

    global window_guide

    global welcome_image_2
    global register_image_2
    global enter_button_image_2
    global instruction_button_image_2

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame7")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window_guide = Toplevel()
    window_guide.title("Enter Guide")

    window_guide.geometry("1440x900")
    window_guide.configure(bg = "#FFFFFF")


    canvas2 = Canvas(
        window_guide,
        bg = "#FFFFFF",
        height = 900,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas2.place(x = 0, y = 0)

    register_image_2 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    register_button_2 = Button(
        window_guide,
        image=register_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: register_user(),
        relief="flat"
    )
    register_button_2.place(
        x=116.0,
        y=644.0,
        width=212.0,
        height=53.0
    )

    enter_button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    enter_button_2 = Button(
        window_guide,
        image=enter_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: enter_lab(),
        relief="flat"
    )
    enter_button_2.place(
        x=118.0,
        y=200.0,
        width=212.0,
        height=86.0
    )

    instruction_button_image_2 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    instruction_button_2 = Button(
        window_guide,
        image=instruction_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: enter_home(),
        relief="flat"
    )
    instruction_button_2.place(
        x=118.0,
        y=337.0,
        width=212.0,
        height=125.0
    )

    canvas2.create_text(
        96.0,
        538.0,
        anchor="nw",
        text="If you don’t have an\naccount register",
        fill="#000000",
        font=("Poppins Regular", 21 * -1)
    )

    canvas2.create_text(
        40.0,
        30.0,
        anchor="nw",
        text="SecureLabs",
        fill="#000000",
        font=("Poppins SemiBold", 25 * -1)
    )

    welcome_image_2 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_2 = canvas2.create_image(
        918.0,
        450.0,
        image=welcome_image_2
    )
    window_guide.resizable(False, False)
