from tkinter import *
import widthHeightDevice as dimensions
import cv2
import face_recognition
import sqlite3
import numpy as np
import qr_detection 



def go_detect_qr(current_window,correct_str):
    current_window.destroy()
    qr_detection.detect_qr(correct_str)

def retry(cam,window_detect_face):
    print(" TRY AGIAN CALLED")
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

    window_detect_face = Toplevel()
    window_detect_face.title("Detect Face")
    # window_detect_face.geometry(f"{dimensions.width}x{dimensions.height}")
    window_detect_face.geometry("1440x900")


    cam_frame = Frame(window_detect_face,width=700,height=394)
    cam_frame.pack_propagate(0)
    cam_frame.place(x = 0,y = 20)
    
    cam_label = Label(cam_frame,text="HELOOOOOO",width=600,height=364)
    cam_label.configure(bg="#B62E11")
    cam_label.place(relx = 0.4,rely = 0.2,anchor=CENTER)
    

    name_label = Label(window_detect_face,
                      text="NOT RECOGNISED",
                      bg="yellow",
                      fg="red")
    name_label.place(x = 830,y = 420)


    next_button = Button(window_detect_face,
                         text="DISABLED",
                         state=DISABLED,
                         bg="grey",
                         command = lambda: go_detect_qr(window_detect_face,correct_str))
    next_button.place(x = 750, y = 420)
    # next_button.pack()

    cam = cv2.VideoCapture(0)

    try_again = Button(window_detect_face,
                         text="TRY AGAIN",
                         state = NORMAL,
                         bg="orange",
                         command = lambda: retry(cam,window_detect_face))
    try_again.place(x = 910, y = 420)



    db = sqlite3.connect("data/user_data.sqlite")
    c = db.cursor()

    
    global frame
    global img
    ret, frame = cam.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    name = None
    
    for encoding in encodings:
            # retrieve all stored face encodings from database
            c.execute('SELECT * FROM USERS')
            rows = c.fetchall()
            stored_encodings = [np.frombuffer(row[5], dtype=np.float64) for row in rows]
            names = [row[1] for row in rows]
            # indices = [row[0] for row in rows]
            strs = [row[6] for row in rows]
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
            else:
                name = 'unknown'
            
    

            # draw bounding box and label around the face
            # top, right, bottom, left = boxes[0]
            # cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            # cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            
            print(" person is recogonized as ",name)    
    if name is not None and name!='unknown':
         next_button['state'] = NORMAL
         next_button['text'] = "GO AHEAD"
         next_button['bg'] = 'green'
         
    if ret:
        img = get_image()
        cam_label.config(image=img)
        cam_label.image = img
        window_detect_face.after(10,lambda: update_cam(cam_label,window_detect_face,cam))
    

