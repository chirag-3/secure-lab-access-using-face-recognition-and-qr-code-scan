from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import widthHeightDevice as dimensions
from tkinter import *
import face_scanning as fs
from tkinter import messagebox


def scan_face(details):
    ## name,email,phone,em-id

    name = details[0]
    email = details[1]
    phone = details[2]
    em_id = details[3]

    if name=='' or email=='' or phone=='' or em_id=='':
        messagebox.showerror('error','no field should be left empty')
        return
    if '@' not in email:
        messagebox.showerror('error','email must contain @')
        return
    if '.' not in email:
        messagebox.showerror('error','email must contain .')
        return
    if len(phone)!=10:
        messagebox.showerror('error','length of phone must be 10')
        return
    try :
        temp = int(phone)
    except:
        messagebox.showerror('error','phone number can contain only digits')
        return
    window_face_scan.destroy()
    fs.face_scan(details)

def register():

    global employee_id_image
    global phone_image
    global email_image
    global name_image
    global side_image
    global scan_face_image
    global window_face_scan



    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame2")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window_face_scan = Toplevel()

    # window_face_scan.geometry(f"{dimensions.width}x{dimensions.height}")
    window_face_scan.geometry("1440x900")
    window_face_scan.configure(bg = "#FFFFFF")


    canvas_face_scan = Canvas(
        window_face_scan,
        bg = "#FFFFFF",
        height = 900,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas_face_scan.place(x = 0, y = 0)


    ##Employee id entry
    employee_id_image = PhotoImage(file=relative_to_assets("entry_1.png"))
    employee_id_bg = canvas_face_scan.create_image(
        326.5,
        618.0,
        image=employee_id_image
    ) 
    employee_id = Entry(
        window_face_scan,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    employee_id.place(
        x=112.0,
        y=596.0,
        width=429.0,
        height=42.0
    )



    ##Phone number entry
    phone_image = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    phone_bg = canvas_face_scan.create_image(
        326.5,
        526.0,
        image=phone_image
    )
    phone = Entry(
        window_face_scan,
        bd=0, 
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    phone.place(
        x=112.0,
        y=504.0,
        width=429.0,
        height=42.0
    )


    ##Email id entry
    email_image = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    email_bg = canvas_face_scan.create_image(
        326.5,
        434.0,
        image=email_image
    )
    email = Entry(
        window_face_scan,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    email.place(
        x=112.0,
        y=412.0,
        width=429.0,
        height=42.0
    )


    #name entry
    name_image = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    name_bg = canvas_face_scan.create_image(
        326.5,
        342.0,
        image=name_image
    )
    name = Entry(
        window_face_scan,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    name.place(
        x=112.0,
        y=320.0,
        width=429.0,
        height=42.0
    )




    #Making and placing the side image
    side_image = PhotoImage(
        file=relative_to_assets("image_1.png"))
    app_image = canvas_face_scan.create_image(
        1055.0,
        450.0,
        image=side_image
    )



    scan_face_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    scan_face_button = Button(
        window_face_scan,
        image=scan_face_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: scan_face([name.get(),email.get(),phone.get(),employee_id.get()]),
        relief="flat"
    )
    scan_face_button.place(
        x=112.0,
        y=696.0,
        width=429.0,
        height=53.0
    )


    ##Adding Text To the canvas
    canvas_face_scan.create_text(
        40.0,
        30.0,
        anchor="nw",
        text="SecureLabs",
        fill="#000000",
        font=("Poppins SemiBold", 25 * -1)
    )
    canvas_face_scan.create_text(
        112.0,
        191.0,
        anchor="nw",
        text="Sign up",
        fill="#000000",
        font=("Poppins Medium", 30 * -1)
    )
    canvas_face_scan.create_text(
        129.0,
        296.0,
        anchor="nw",
        text="Full Name",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    canvas_face_scan.create_text(
        129.0,
        388.0,
        anchor="nw",
        text="Email",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    canvas_face_scan.create_text(
        129.0,
        480.0,
        anchor="nw",
        text="Phone No.",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )
    canvas_face_scan.create_text(
        129.0,
        578.0,
        anchor="nw",
        text="Employee ID",
        fill="#000000",
        font=("Poppins Medium", 16 * -1)
    )

    window_face_scan.resizable(False, False)