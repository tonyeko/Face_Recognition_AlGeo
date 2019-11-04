import samplefacerecog
import os
from tkinter import *
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Face Recognition by UNITY")

def runfacerecog():
    print(sample.get())
    samplefacerecog.main(choice.get(), T.get(), sample.get())
    return

def open_dialog():
    path = askopenfilename(initialdir = "datauji/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    name = os.path.basename(path)
    filename.delete(0, END)
    filename.insert(0, name)
    sample = name

sample = StringVar()
T = IntVar()
choice = IntVar()

filelabel = Label(window, text = "Nama File Sample: ").grid(row = 0, column = 0, padx = 0, pady = 10) # this is placed in 0 0
# 'Entry' is used to display the input-field
filename = Entry(window, textvariable = sample)
filename.grid(row = 0, column = 1) # this is placed in 0 1
button = Button(window, text="Browse File", command=open_dialog)
button.grid(row = 0, column = 2, padx = 10)

Label(window, text = "T").grid(row = 1, column = 0, padx = 0, pady = 10) # this is placed in 1 0
Entry(window, textvariable = T).grid(row = 1, column = 1) # this is placed in 1 1

Label(window, text = "Metode: ").grid(row = 2, column = 0, padx = 0, pady = 10) # this is placed in 1 0
Radiobutton(window, text="Cosine Similarity", padx = 20, variable=choice, value=1).grid(row = 2, column = 1)
Radiobutton(window, text="Euclidean Distance", padx = 20, variable=choice, value=2).grid(row = 2, column = 2)

btn = Button(window, text = 'Run', command = runfacerecog).grid(row = 3, column = 1)

window.mainloop()

# T = 10
# sample = "Aaron Paul124_221.jpg"

# facerecog.main('1', T, sample)