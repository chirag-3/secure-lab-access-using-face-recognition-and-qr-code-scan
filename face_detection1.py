
from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from tkinter import *
import cv2
import face_recognition
import sqlite3
import numpy as np
import qr_detection
from tkinter import messagebox
import homepage as hp
from datetime import datetime

def go_detect_qr(current_window,correct_str,name):
    global authorized
    if authorized==0:
        messagebox.showerror('error','the user is registered but has not been authorized by the admin')
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("login_log.txt",'a') as f:
            f.write(f"{name} had face authenticated but was not authorized to enter "+dt_string+"\n")
        current_window.destroy()
        hp.homepage()
    else:
        current_window.destroy()
        qr_detection.detect_qr(correct_str,name)

def retry(cam,window_detect_face):
    # print(" TRY AGIAN CALLED")
    cam.release()
    cv2.destroyAllWindows()
    window_detect_face.destroy()
    detect_face()

def get_image():
    global img
    global frame
    f = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(f, (700, 394))
    img = PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
    return img

def update_cam(cam_label,window_detect_face,cam):
    global img
    global frame
    ret, frame = cam.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    if ret:
        img = get_image()
        cam_label.config(image=img)
        cam_label.image = img
        window_detect_face.after(10,lambda: update_cam(cam_label,window_detect_face,cam))


def detect_face():

    global window_detect_face

    idx = None
    correct_str = None
    name = None
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame9")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window_detect_face = Toplevel()
    window_detect_face.title("Detect Face")

    window_detect_face.geometry("1440x900")
    window_detect_face.configure(bg = "#FFFFFF")

    canvas = Canvas(
        window_detect_face,
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
        41.0,
        175.0,
        anchor="nw",
        text="Face\nRecogination",
        fill="#000000",
        font=("Poppins SemiBold", 45 * -1)
    )
    canvas.create_text(
        40.0,
        358.0,
        anchor="nw",
        text="Make sure you are\nin visible range",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )



    global cam_bck_image
    global ty_again_button_image
    global go_ahead_green_button_image
    global go_ahead_red_button_image
    
    cam_bck_image = PhotoImage(
        file=relative_to_assets("image_1.png"))
    cam_frame = Frame(window_detect_face,width=1009,height=859)

    cam_frame.pack_propagate(0)
    cam_frame.place(x = 414,y = 21)

    cam_label = Label(cam_frame,width=700,height=394)
    cam_label.place(relx = 0.5,rely = 0.5,anchor=CENTER)

    bg_img = Label(cam_frame, image=cam_bck_image)
    bg_img.pack()
    bg_img.lower()

    cam = cv2.VideoCapture(0)

    ty_again_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    try_again_button = Button(
        window_detect_face,
        image=ty_again_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: retry(cam,window_detect_face),
        relief="flat"
    )

    try_again_button.place(
        x=95.0,
        y=675.0,
        width=212.0,
        height=53.0
    )

    go_ahead_red_button_image = PhotoImage(
        file=relative_to_assets("button_2.png"))
    go_ahead_red_button = Button(
        window_detect_face,
        image=go_ahead_red_button_image,
        # state="disabled",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print(""),
        relief="flat"
    )

    go_ahead_red_button.place(
        x=93.0,
        y=585.0,
        width=212.0,
        height=53.0
    )

    go_ahead_green_button_image = PhotoImage(
        file=relative_to_assets("button_3.png"))
    go_ahead_green_button = Button(
        window_detect_face,
        image=go_ahead_green_button_image,
        state="disabled",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: go_detect_qr(window_detect_face,correct_str,name),
        relief="flat"
    )
    go_ahead_green_button.place(
        x=93.0,
        y=585.0,
        width=212.0,
        height=53.0
    )
    go_ahead_green_button.lower()

    name_label = Label(
        window_detect_face,
        text= "NOT RECOGINSED",
        
        font=("Poppins SemiBold", 26 * -1)
    )
    name_label.place(x = 40.0,y = 480.0)
    
    

    db = sqlite3.connect("app_data/user_data.sqlite")
    c = db.cursor()


    global frame
    global img
    ret, frame = cam.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    # name = None
    global authorized
    authorized = 0
    for encoding in encodings:
            # retrieve all stored face encodings from database
            c.execute('SELECT * FROM USERS')
            rows = c.fetchall()
            stored_encodings = [np.frombuffer(row[5], dtype=np.float64) for row in rows]
            names = [row[1] for row in rows]
            # indices = [row[0] for row in rows]
            strs = [row[6] for row in rows]
            auth_values = [row[7] for row in rows]
            # compute distances between current face encoding and stored encodings
            distances = face_recognition.face_distance(stored_encodings, encoding)
            min_idx = np.argmin(distances)
            min_distance = distances[min_idx]

            # if the minimum distance is less than a threshold, the face is recognized
            if min_distance < 0.6:
                name = names[min_idx]
                name_label['text'] = name
                # idx = indices[min_idx]
                correct_str = strs[min_idx]
                authorized = auth_values[min_idx]
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")  
                with open('login_log.txt','a') as f:
                    f.write(f"{name} tried to login got face authenticated successfully "+dt_string+"\n")           
            else:
                name = 'unknown'
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                with open("login_log.txt",'a') as f:
                    f.write("unknown person tried to login "+dt_string+"\n")



            # draw bounding box and label around the face
            # top, right, bottom, left = boxes[0]
            # cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            # print(" person is recogonized as ",name)    
    if name is not None and name!='unknown':
        go_ahead_red_button.lower()
        go_ahead_green_button.lift()
        go_ahead_green_button['state'] = NORMAL
        go_ahead_red_button['state'] = DISABLED

    if ret:
        img = get_image()
        cam_label.config(image=img)
        cam_label.image = img
        window_detect_face.after(10,lambda: update_cam(cam_label,window_detect_face,cam))

    window_detect_face.resizable(False, False)
    # window_detect_face.mainloop()