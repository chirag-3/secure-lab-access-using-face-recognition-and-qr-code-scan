

from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


import sqlite3
import tkinter as tk
from tkinter import ttk



def toggle_button_unauth():
    auth_button.lift()
    table_frame_auth.lift()

def toggle_button_auth():
    unauth_button.lift()
    table_frame_unauth.lift()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame10")


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
auth_button = Button(
    image=auth_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: toggle_button_auth(),
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
unauth_button = Button(
    image=unauth_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: toggle_button_unauth(),
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
logout_button = Button(
    image=logout_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("logout_button clicked"),
    relief="flat"
)
logout_button.place(
    x=1268.0,
    y=102.0,
    width=127.0,
    height=58.0
)


update_button_image = PhotoImage(
    file=relative_to_assets("button_4.png"))
update_button = Button(
    image=update_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Update_button clicked"),
    relief="flat"
)
update_button.place(
    x=614.0,
    y=793.0,
    width=212.0,
    height=53.0
)



image_image_2 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_2 = canvas.create_image(
    720.0,
    479.0,
    image=image_image_2
)




# create a connection to the database
db = sqlite3.connect("data/user_data.sqlite")
c = db.cursor()


# retrieve data from the database
c.execute('SELECT * FROM USERS')
rows = c.fetchall()




table_frame_unauth = Frame(window,width=1440,height=593)
table_frame_unauth.pack_propagate(0)
table_frame_unauth.place(x=0,y=183)

table_label_unauth = Label(table_frame_unauth,width=1400,height=553)
table_label_unauth.place(relx = 0.5,rely = 0.5,anchor=CENTER)



# create a treeview to display the data
tree_unauth = ttk.Treeview(table_label_unauth)
# tree_unauth.heading("Unauth users")
tree_unauth['columns'] = ('name', 'email', 'phone', 'employee_id', 'qr_string')
tree_unauth.heading('#0', text='ID')
tree_unauth.column('#0', width=50)
tree_unauth.heading('name', text='Name')
tree_unauth.column('name', width=150)
tree_unauth.heading('email', text='E-Mail')
tree_unauth.column('email', width=200)
tree_unauth.heading('phone', text='phone')
tree_unauth.column('phone', width=150)
tree_unauth.heading('employee_id', text='Unauth Employee ID')
tree_unauth.column('employee_id', width=100)
# tree.heading('qr_string', text='QR String')
# tree.column('qr_string', width=150)



# insert the data into the treeview
for row in rows:
    tree_unauth.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))




table_frame_auth = Frame(window,width=1440,height=593)
table_frame_auth.pack_propagate(0)
table_frame_auth.place(x=0,y=183)

table_label_auth = Label(table_frame_auth,width=1400,height=553)
table_label_auth.place(relx = 0.5,rely = 0.5,anchor=CENTER)

tree_auth = ttk.Treeview(table_label_auth)
# tree_auth.heading("auth users")
tree_auth['columns'] = ('name', 'email', 'phone', 'employee_id', 'qr_string')
tree_auth.heading('#0', text='ID')
tree_auth.column('#0', width=50)
tree_auth.heading('name', text='Name')
tree_auth.column('name', width=150)
tree_auth.heading('email', text='E-Mail')
tree_auth.column('email', width=200)
tree_auth.heading('phone', text='phone')
tree_auth.column('phone', width=150)

for row in rows:
    tree_auth.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))

table_frame_unauth.lift()

tree_unauth.pack()
tree_auth.pack()

window.resizable(False, False)
window.mainloop()


