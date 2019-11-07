import tkinter as tk
from tkinter import ttk
import facerecog
import os
import imgshow
from header import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

LARGE_FONT = ("Verdana", 12)

class Master (tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        # Add title and icon
        tk.Tk.iconbitmap(self, default="img/facerecog.ico")
        tk.Tk.wm_title(self, "Face Recognition by UNITY")
        self.geometry('+500+100')
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainPage, HelpPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        if cont == StartPage:
            self.after(2000, self.show_frame, MainPage)
            self.overrideredirect(True)
        if cont != StartPage:
            self.overrideredirect(False)

class StartPage(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Show Loading Background Image
        imgshow.loading_background_img(self)
        label = tk.Label(self, text="Welcome to UNITY Face Recognition ", font=LARGE_FONT)
        label.grid(row=0, column=0, padx=320, pady=150)

class MainPage(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Show Background Image
        imgshow.background_img(self)
        # Tkinter Variable Declaration
        sample = StringVar()
        T = IntVar()
        T.set(10) # set default value 
        choice = IntVar()
        # Show Header
        header(self)

        def runfacerecog():
            a = choice.get()
            b = T.get()
            c = sample.get()
            imgshow.show_sample_img(os.path.join('../test/datauji/', c), self)
            facerecog.main(a, b, c)
            return c   

        def open_dialog():
            path = askopenfilename(initialdir = "../test/datauji/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            name = os.path.basename(path)
            filename.delete(0, END)
            filename.insert(0, name)
            sample = name
        # Choose Sample Photo
        filelabel = Label(self, text = "Nama File Sample: ").grid(row = 14, column = 2, padx = 0, pady = 10)
        filename = Entry(self, textvariable = sample)
        filename.grid(row = 14, column = 3, columnspan = 2)
        button = Button(self, text="Browse File", command=lambda:open_dialog())
        button.grid(row = 14, column = 5, padx = 10)
        # Choose T
        Label(self, text = "Banyaknya wajah yang cocok: ").grid(row = 15, column = 2, padx = 0, pady = 10) 
        Entry(self, textvariable = T).grid(row = 15, column = 3, columnspan = 2) 
        # Choose Method (Cosine Similarity / Euclidean Distance)
        Label(self, text = "Metode: ").grid(row = 17, column = 2, padx = 0, pady = 10) 
        Radiobutton(self, text="Cosine Similarity", padx = 20, variable=choice, value=1).grid(row = 17, column = 4)
        Radiobutton(self, text="Euclidean Distance", padx = 20, variable=choice, value=2).grid(row = 17, column = 5)
        # Run Button
        btn = Button(self, text = 'Run', command = lambda:[runfacerecog()], height = 1, width = 8).grid(row = 18, column = 4)
        # Help Button
        buttonhelp = tk.Button(self, text="Help", command=lambda: controller.show_frame(HelpPage)) 
        buttonhelp.grid(row=18, column=5, padx = 2)

class HelpPage(tk.Frame) :

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        # Show Background Image
        imgshow.background_img(self)
        # Back to MainPage Button
        button2 = tk.Button(self, text="<<", command=lambda: controller.show_frame(MainPage)) 
        button2.grid(row=0, column=9, pady=5)
        # Show Help Text
        help_txt(self)

        def runfacerecog2(a,b,c):
            imgshow.show_sample_img(os.path.join('../test/datauji/', c), self)
            facerecog.main(a, b, c)
            return    


app = Master()
app.mainloop()