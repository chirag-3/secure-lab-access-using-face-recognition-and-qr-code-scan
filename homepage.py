# print("HOME HOME HOME HOME")
from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import widthHeightDevice as dimensions
import how_to_enter as hte
import register as rp
import face_detection1 as fd





def enter_lab():
    global window_home
    window_home.destroy()
    fd.detect_face()



def enter_lab_guide():
    global window_home
    window_home.destroy()
    hte.enter_guide()

def user_register():
    global window_home
    window_home.destroy()
    rp.register()


def homepage():

    global window_home

    global welcome_image_1
    global register_image_1
    global enter_button_image_1
    global instruction_button_image_1

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame8")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window_home = Toplevel()
    window_home.title("Homepage")

    # window_home.geometry(f"{dimensions.width}x{dimensions.height}")
    window_home.geometry("1440x900")
    window_home.configure(bg = "#FFFFFF")


    canvas1 = Canvas(
        window_home,
        bg = "#FFFFFF",
        height = 900,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas1.place(x = 0, y = 0)


    register_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    register_button_1 = Button(
        window_home,
        image=register_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: user_register(),
        relief="flat"
    )
    register_button_1.place(
        x=118.0,
        y=586.0,
        width=429.0,
        height=53.0
    )


    enter_button_image_1 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    enter_button_1 = Button(
        window_home,
        image=enter_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command = enter_lab,
        relief="flat"
    )
    enter_button_1.place(
        x=118.0,
        y=200.0,
        width=429.0,
        height=86.0
    )



    instruction_button_image_1 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    instruction_button_1 = Button(
        window_home,
        image=instruction_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: enter_lab_guide(),
        relief="flat"
    )
    instruction_button_1.place(
        x=118.0,
        y=337.0,
        width=429.0,
        height=86.0
    )



    canvas1.create_text(
        96.0,
        538.0,
        anchor="nw",
        text="If you don’t have an account register",
        fill="#000000",
        font=("Poppins Regular", 21 * -1)
    )
    canvas1.create_text(
        40.0,
        30.0,
        anchor="nw",
        text="SecureLabs",
        fill="#000000",
        font=("Poppins SemiBold", 25 * -1)
    )
    welcome_image_1 = PhotoImage(
        file=relative_to_assets("welcome_secureLabs.png"))
    image_1 = canvas1.create_image(
        1055.0,
        450.0,
        image=welcome_image_1
    )

    window_home.resizable(False, False)


