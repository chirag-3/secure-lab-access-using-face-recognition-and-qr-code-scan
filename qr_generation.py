from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, Label
from tkinter import *
from tkinter import filedialog
import widthHeightDevice as dimensions

import string, random, qrcode, sqlite3
import homepage as hp

def download_qr(qr_img,qr_string):
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_path_is = folder_path + '/qr_code_' + qr_string + '.png'
        qr_img.save(file_path_is)

def open_homepage():
    global window_qr_code
    hp.homepage()
    window_qr_code.destroy()



def register_user(qr_string,details):
    # pass
    global window_qr_code
    db = sqlite3.connect("app_data/user_data.sqlite")
    cur = db.cursor()

    ##Creating the table if it does not already exist
    create_table_query = '''CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,phone BIGINT,employee_id TEXT,
                            encoding BLOB,qr_string TEXT,authorized INTEGER)'''
    cur.execute(create_table_query)
    

    ##Inserting the values
    name = details[0]
    email = details[1]
    phone = details[2]
    employee_id = details[3]
    encoding = details[4]
    auth = 0
    # insert_query = f"INSERT INTO USER (name,email,phone,employee_id,encoding,qr_string) VALUES ({name},{email},{phone},{employee_id},{encoding.tobytes()},{qr_string}) "
    cur.execute("INSERT INTO USERS (name,email,phone,employee_id,encoding,qr_string,authorized) VALUES (?,?,?,?,?,?,?)",
                (name,email,phone,employee_id,encoding.tobytes(),qr_string,auth))
    db.commit()
    window_qr_code.destroy()


def generate_QR(details):
# def generate_QR():

    
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    global window_qr_code

    window_qr_code = Toplevel()

    window_qr_code.geometry("1440x900")
    window_qr_code.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window_qr_code,
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
        82.0,
        311.0,
        anchor="nw",
        text="QR Code",
        fill="#000000",
        font=("Poppins SemiBold", 45 * -1)
    )

    characters = list(string.ascii_letters)
    for i in range(10):
        characters.append(str(i))
    last = len(characters) - 1

    ##create random string of length 10 for QR
    qr_string = ""
    
    for i in range(20):
        qr_string += characters[random.randint(0,last)]

    qr_code = qrcode.make(qr_string)
    qr_code.save("temp/temp1.png")

    global qr_img_back, qr_image_1


    qr_img_back = PhotoImage(
        file=relative_to_assets("image_1.png"))

    qr_image_1 = PhotoImage(
        file="temp/temp1.png")

    qr_frame = Frame(window_qr_code,width=1009,height=859)
    qr_frame.pack_propagate(0)
    qr_frame.place(x = 414,y = 21)

    qr_label = Label(qr_frame,width=330,height=330)
    qr_label.place(relx=0.5,rely=0.5,anchor=CENTER)

    bg_img = Label(qr_frame, image=qr_img_back)
    bg_img.pack()
    bg_img.lower()
   
    qr_img = Label(qr_label, image=qr_image_1)
    qr_img.pack()



    global donwload_regiter_image_1 , donwload_regiter_button_1
    global enter_lab_image_2, enter_lab_button_2


    donwload_regiter_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    donwload_regiter_button_1 = Button(
        window_qr_code,
        image=donwload_regiter_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: [register_user(qr_string,details),download_qr(qr_code, qr_string)],
        relief="flat"
    )
    donwload_regiter_button_1.place(
        x=94.0,
        y=450.0,
        width=212.0,
        height=53.0
    )



    enter_lab_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    enter_lab_button_2 = Button(
        window_qr_code,
        image=enter_lab_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: open_homepage(),
        relief="flat"
    )
    enter_lab_button_2.place(
        x=94.0,
        y=543.0,
        width=212.0,
        height=86.0
    )
    window_qr_code.resizable(True, True)
