import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk

db = sqlite3.connect("data/user_data.sqlite")
c = db.cursor()


# retrieve data from the database
c.execute('SELECT * FROM USERS')
rows = c.fetchall()


# table_frame = Frame(window,width=1440,height=593)
# table_frame.pack_propagate(0)
# table_frame.place(x=0,y=183)

# table_label = Label(table_frame,width=1400,height=553)
# table_label.place(relx = 0.5,rely = 0.5,anchor=CENTER)



# create a treeview to display the data

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        tree = ttk.Treeview(self)
        tree['columns'] = ('name', 'email', 'phone', 'employee_id', 'qr_string')
        tree.heading('#0', text='ID')
        tree.column('#0', width=50)
        tree.heading('name', text='Name')
        tree.column('name', width=150)
        tree.heading('email', text='E-Mail')
        tree.column('email', width=200)
        tree.heading('phone', text='phone')
        tree.column('phone', width=150)
        tree.heading('employee_id', text='Employee ID')
        tree.column('employee_id', width=100)
        # tree.heading('qr_string', text='QR String')
        # tree.column('qr_string', width=150)


        # insert the data into the treeview
        for row in rows:
            tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4]))


        tree.pack()

        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tree = ttk.Treeview(self)
        tree['columns'] = ('name', 'email', 'phone')
        tree.heading('#0', text='ID')
        tree.column('#0', width=50)
        tree.heading('name', text='Name')
        tree.column('name', width=150)
        tree.heading('email', text='E-Mail')
        tree.column('email', width=200)
        tree.heading('phone', text='phone')
        tree.column('phone', width=150)
        # tree.heading('employee_id', text='Employee ID')
        # tree.column('employee_id', width=100)
        # tree.heading('qr_string', text='QR String')
        # tree.column('qr_string', width=150)


        # insert the data into the treeview
        for row in rows:
            tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3]))


        tree.pack()
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = SeaofBTCapp()
app.mainloop()