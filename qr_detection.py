


from pathlib import Path
import time
# from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import cv2
import access_granted
import access_denied
from datetime import datetime

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame6")

# print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_image():
    global img
    global frame
    f = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(f, (700, 394))
    img = PhotoImage(data=cv2.imencode('.png', img)[1].tobytes())
    return img


def update_cam(cam_label,window,cam,correct_str):
    global img
    global frame
    global points
    global decoded
    global start_time
    global name
    if decoded=="":
        # print(" ================== ",decoded)
        current_time = time.time()
        if (current_time-start_time)>25:
            cam.release()
            with open("login_log.txt",'a') as f:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                f.write(f"{name} has been denied entry due to qr detection timeout"+dt_string+"\n")
            cv2.destroyAllWindows()
            window.destroy()
            access_denied.deny()
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        qrCodeDetector = cv2.QRCodeDetector()
        decoded, points, _ = qrCodeDetector.detectAndDecode(gray)
        if ret:
            img = get_image()
            cam_label.config(image=img)
            cam_label.image = img
            window.after(10,lambda: update_cam(cam_label,window,cam,correct_str))
    elif decoded==correct_str:
        cam.release()
        cv2.destroyAllWindows()
        window.destroy()
        # if correct_str == decoded:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("login_log.txt",'a') as f:
            f.write(f"{name} has been granted entry "+dt_string+"\n")
        access_granted.grant()
        # else:
    else :
        cam.release()
        cv2.destroyAllWindows()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("login_log.txt",'a') as f:
            f.write(f"{name} has been denied entry due to incorrect QR "+dt_string+"\n")
        window.destroy()
        access_denied.deny()


def detect_qr(correct_str,Name):
    global start_time 
    global name
    name = Name
    start_time = time.time()
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
        82.0,
        311.0,
        anchor="nw",
        text="QR Code\nScanner",
        fill="#000000",
        font=("Poppins SemiBold", 45 * -1)
    )
    canvas.create_text(
        40.0,
        783.0,
        anchor="nw",
        text="Wait for QR detection",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )
    canvas.create_text(
        40.0,
        538.0,
        anchor="nw",
        text="Do place the QR in\nvisible range",
        fill="#000000",
        font=("Poppins SemiBold", 26 * -1)
    )

    global cam_bck_image

    cam_bck_image = PhotoImage(
        file=relative_to_assets("image_1.png"))


    cam_frame = Frame(window,width=1009,height=859)


    cam_frame.pack_propagate(0)
    cam_frame.place(x = 414,y = 21)

    cam_label = Label(cam_frame,width=700,height=394)
    # cam_label.place(x = 0,y = 0)
    cam_label.place(relx = 0.5,rely = 0.5,anchor=CENTER)

    bg_img = Label(cam_frame, image=cam_bck_image)
    bg_img.pack()
    bg_img.lower()


    cam = cv2.VideoCapture(0)
    global frame
    global img
    global points
    global decoded
    points = None
    decoded = ""
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    qrCodeDetector = cv2.QRCodeDetector()
    decoded, points, _ = qrCodeDetector.detectAndDecode(gray)
    if decoded=="":
        # print("yeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        if ret:
            img = get_image()
            cam_label.config(image=img)
            cam_label.image = img
            window.after(5,lambda: update_cam(cam_label,window,cam,correct_str))
    elif decoded==correct_str:
        cam.release()
        cv2.destroyAllWindows()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("login_log.txt",'a') as f:
            f.write(f"{name} has been granted entry "+dt_string+"\n")
        window.destroy()
        access_granted.grant()
        # else:
    else :
        cam.release()
        cv2.destroyAllWindows()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        with open("login_log.txt",'a') as f:
            f.write(f"{name} has been denied entry due to incorrect QR "+dt_string+"\n")
        window.destroy()
        access_denied.deny()
        

    window.resizable(False, False)
    # window.mainloop()


# detect_qr("chirag")