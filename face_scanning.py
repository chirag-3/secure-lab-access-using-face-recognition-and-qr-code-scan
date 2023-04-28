from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import face_recognition
import cv2
import qr_generation as qrg
import widthHeightDevice as dimensions
from tkinter import *
from tkinter import messagebox

def capture(cam,details):
    global img
    global frame
    global window_face_scan
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    if len(boxes) == 0:
        # print('Error: no face detected')
        messagebox.showerror("showerror", "No faces detected")
        # cam.release()
        # cv2.destroyAllWindows()
        return
    elif len(boxes) > 1:
        # print('Error: multiple faces detected')
        messagebox.showerror("showerror", "Multiple faces detected")
        # cam.release()
        # cv2.destroyAllWindows()
        return
    top, right, bottom, left = boxes[0]
    face = rgb[top:bottom, left:right]
    cam.release()
    cv2.destroyAllWindows()
    # compute face encoding
    filtered_face = cv2.bilateralFilter(face, 9, 75, 75)
    encoding = face_recognition.face_encodings(filtered_face)[0]
    # print(" type of the encodiung is ",type(encoding))
    details.append(encoding)
    window_face_scan.destroy()

    ## The qr scanning function has to be called
    qrg.generate_QR(details)  




def update_cam(cam_label,window_face_scan,cam):
    global img
    global frame
    ret, frame = cam.read()
    if ret:
        img = get_image()
        cam_label.config(image=img)
        cam_label.image = img
        window_face_scan.after(10,lambda: update_cam(cam_label,window_face_scan,cam))

def get_image():
    global img
    global frame
    f = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(f, (700, 394))
    img = PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
    return img



def face_scan(details):

    
    global window_face_scan
    

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame5")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window_face_scan = Toplevel()
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
    canvas_face_scan.create_text(
        40.0,
        30.0,
        anchor="nw",
        text="SecureLabs",
        fill="#000000",
        font=("Poppins SemiBold", 25 * -1)
    )

    canvas_face_scan.create_text(
        41.0,
        175.0,
        anchor="nw",
        text="Face\nRecogination",
        fill="#000000",
        font=("Poppins SemiBold", 45 * -1)
    )

    canvas_face_scan.create_text(
        40.0,
        647.0,
        anchor="nw",
        text="Tap to detect face",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )

    canvas_face_scan.create_text(
        40.0,
        358.0,
        anchor="nw",
        text="Make sure you are\nin visible range",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )
    global capture_button_image
    global cam_bck_image

    cam_bck_image = PhotoImage(
        file=relative_to_assets("image_1.png"))

    cam_frame = Frame(window_face_scan,width=1009,height=859)
    cam_frame.pack_propagate(0)
    cam_frame.place(x = 414,y = 21)

    cam_label = Label(cam_frame,width=700,height=394)
    cam_label.place(relx = 0.5,rely = 0.5,anchor=CENTER)

    bg_img = Label(cam_frame, image=cam_bck_image)
    bg_img.pack()
    bg_img.lower()
    


    capture_button_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    capture_button_1 = Button(
        window_face_scan,
        image=capture_button_image,
        borderwidth=0,
        highlightthickness=0,
        # command=lambda: print("capture"),
        command=lambda: capture(cam,details),
        relief="flat"
    )
    capture_button_1.place(
        x=141.0,
        y=484.0,
        width=120.0,
        height=120.0
    )
   

    cam = cv2.VideoCapture(0)
    global frame
    global img
    ret, frame = cam.read()
    if ret:
        img = get_image()
        cam_label.config(image=img)
        cam_label.image = img
        window_face_scan.after(10,lambda: update_cam(cam_label,window_face_scan,cam))

    window_face_scan.resizable(True, True)
