

from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


import sqlite3
import tkinter as tk
from tkinter import ttk
import time
from tkinter import messagebox

def isAuth(x):
    if x==0:
        return "NO"
    else:
        return "YES"


def do_auth():
    global unauth_button
    global auth_button
    global selected_row
    if selected_row is None:
        messagebox.showerror('error','Please select a record first')
        return 
    db = sqlite3.connect("app_data/user_data.sqlite")
    c = db.cursor()
    c.execute(f''' UPDATE USERS SET authorized=1 WHERE id={selected_row[0]}''')
    db.commit()
    selected_row = None
    unauth_button.lift()
    populate_table()

def do_unauth():
    global unauth_button
    global auth_button
    global selected_row
    if selected_row is None:
        messagebox.showerror('error','Please select a record first')
        return 
    db = sqlite3.connect("app_data/user_data.sqlite")
    c = db.cursor()
    c.execute(f''' UPDATE USERS SET authorized=0 WHERE id={selected_row[0]}''')
    db.commit()
    selected_row = None
    auth_button.lift()
    populate_table()


def on_click(event):
    global unauth_button
    global auth_button
    global selected_row
    item = tree_unauth.identify('item', event.x, event.y)
    if not item:
        selected_row = None
    else:
        selected_row = tree_unauth.item(item, 'values')
        x = selected_row[5]
        if x=='YES':
            unauth_button.lift()
        else:
            auth_button.lift()

    
def populate_table(x=None):
    global table_frame_unauth
    global table_label_unauth
    global tree_unauth
    global unauth_button
    global auth_button

    try:
        for r in tree_unauth.get_children():
            tree_unauth.delete(r)
        tree_unauth.pack_forget()
    except:
        pass
    db = sqlite3.connect("app_data/user_data.sqlite")
    c = db.cursor()
    

    c.execute('SELECT * FROM USERS')
    rows = c.fetchall()
    tree_unauth['columns'] = ('id','name', 'email', 'phone', 'employee_id','authorized')
    tree_unauth.heading('id', text='ID')
    tree_unauth.column('id', width=50)
    tree_unauth.heading('name', text='Name')
    tree_unauth.column('name', width=150)
    tree_unauth.heading('email', text='E-Mail')
    tree_unauth.column('email', width=200)
    tree_unauth.heading('phone', text='phone')
    tree_unauth.column('phone', width=150)
    tree_unauth.heading('employee_id', text='Unauth Employee ID')
    tree_unauth.column('employee_id', width=100)
    tree_unauth.heading('authorized', text='authorized')
    tree_unauth.column('authorized', width=100)

    for row in rows:
        tree_unauth.insert('', 'end', values=(row[0],row[1], row[2], row[3], row[4],isAuth(row[7])))
    table_frame_unauth.lift()
    tree_unauth.pack()



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame10")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def dashboard():
    global selected_row
    global auth_button_image
    global unauth_button_image
    global image_image_2
    global logout_button_image
    global auth_button
    global unauth_button
    dash_window = Toplevel()
    dash_window.geometry("1440x900")
    dash_window.configure(bg = "#FFFFFF")
    selected_row = None

    canvas = Canvas(
        dash_window,
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
        876.0,
        102.0,
        anchor="nw",
        text="Admin Dashboard ",
        fill="#000000",
        font=("Poppins SemiBold", 35 * -1)
    )




    auth_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    auth_button = Button(dash_window,
        image=auth_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: do_auth(),
        # command=lambda: print("auth_button clicked"),
        relief="flat"
    )
    auth_button.place(
        x=73.0,
        y=98.0,
        width=212.0,
        height=58.49334716796875
    )



    unauth_button_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    unauth_button = Button(dash_window,
        image=unauth_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: do_unauth(),
        # command=lambda: print("unauth_button clicked"),
        relief="flat"
    )
    unauth_button.place(
        x=73.0,
        y=98.0,
        width=212.0,
        height=58.49334716796875
    )





    logout_button_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    logout_button = Button(dash_window,
        image=logout_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: dash_window.destroy(),
        relief="flat"
    )
    logout_button.place(
        x=1268.0,
        y=102.0,
        width=127.0,
        height=58.0
    )



    # update_button_image = PhotoImage(
    #     file=relative_to_assets("button_4.png"))
    # update_button = Button(
    #     image=update_button_image,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("Update_button clicked"),
    #     relief="flat"
    # )
    # update_button.place(
    #     x=614.0,
    #     y=293.0,
    #     width=212.0,
    #     height=53.0
    # )







    image_image_2 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_2 = canvas.create_image(
        720.0,
        479.0,
        image=image_image_2
    )


    global table_frame_unauth
    global table_label_unauth

    table_frame_unauth = Frame(dash_window,width=1440,height=593)
    table_frame_unauth.pack_propagate(0)
    table_frame_unauth.place(x=0,y=183)

    table_label_unauth = Label(table_frame_unauth,width=1400,height=553)
    table_label_unauth.place(relx = 0.5,rely = 0.5,anchor=CENTER)


    global tree_unauth
    tree_unauth = ttk.Treeview(table_label_unauth)
    populate_table()
    tree_unauth.bind('<ButtonRelease-1>', on_click)
    dash_window.resizable(False, False)
    # window.mainloop()

