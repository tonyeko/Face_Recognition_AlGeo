import samplefacerecog
import os
from header import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

def runfacerecog():
    samplefacerecog.main(choice.get(), T.get(), sample.get())
    return

def open_dialog():
    path = askopenfilename(initialdir = "datauji/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    name = os.path.basename(path)
    filename.delete(0, END)
    filename.insert(0, name)
    sample = name

window = Tk()
window.iconbitmap("facerecog.ico")
window.title("Face Recognition by UNITY")

backgroundfile = ImageTk.PhotoImage(file = "background_image3.jpg")
background_label = Label(window, image=backgroundfile)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

sample = StringVar()
T = IntVar()
choice = IntVar()

header()

filelabel = Label(window, text = "Nama File Sample: ").grid(row = 14, column = 2, padx = 0, pady = 10) # this is placed in 0 0
# 'Entry' is used to display the input-field
filename = Entry(window, textvariable = sample)
filename.grid(row = 14, column = 3, columnspan = 2) # this is placed in 0 1
button = Button(window, text="Browse File", command=open_dialog)
button.grid(row = 14, column = 5, padx = 10)

Label(window, text = "Banyaknya wajah yang cocok: ").grid(row = 15, column = 2, padx = 0, pady = 10) # this is placed in 1 0
Entry(window, textvariable = T).grid(row = 15, column = 3, columnspan = 2) # this is placed in 1 1

Label(window, text = "Metode: ").grid(row = 17, column = 2, padx = 0, pady = 10) # this is placed in 1 0
Radiobutton(window, text="Cosine Similarity", padx = 20, variable=choice, value=1).grid(row = 17, column = 4)
Radiobutton(window, text="Euclidean Distance", padx = 20, variable=choice, value=2).grid(row = 17, column = 5)
Label(window).grid(pady = 7)
btn = Button(window, text = 'Run', command = runfacerecog, height = 1, width = 8).grid(row = 18, column = 4)

window.mainloop()