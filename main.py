import facerecog
import os
import imgshow
from header import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image

def runfacerecog():
    imgshow.show_sample_img(os.path.join('datauji/', sample.get()), window)
    facerecog.main(choice.get(), T.get(), sample.get())
    return    

def open_dialog():
    path = askopenfilename(initialdir = "datauji/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    name = os.path.basename(path)
    filename.delete(0, END)
    filename.insert(0, name)
    sample = name

window = Tk()
# Add title and icon
window.iconbitmap("facerecog.ico")
window.title("Face Recognition by UNITY")
window.geometry('+500+100')
# Add background image
backgroundfile = ImageTk.PhotoImage(file = "background_image.jpg")
background_label = Label(window, image=backgroundfile)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# Tkinter Variable Declaration
sample = StringVar()
T = IntVar()
T.set(10) # set default value 
choice = IntVar()
# Show Header
header()

filelabel = Label(window, text = "Nama File Sample: ").grid(row = 14, column = 2, padx = 0, pady = 10)
filename = Entry(window, textvariable = sample)
filename.grid(row = 14, column = 3, columnspan = 2)
button = Button(window, text="Browse File", command=open_dialog)
button.grid(row = 14, column = 5, padx = 10)

Label(window, text = "Banyaknya wajah yang cocok: ").grid(row = 15, column = 2, padx = 0, pady = 10) 
Entry(window, textvariable = T).grid(row = 15, column = 3, columnspan = 2) 

Label(window, text = "Metode: ").grid(row = 17, column = 2, padx = 0, pady = 10) 
Radiobutton(window, text="Cosine Similarity", padx = 20, variable=choice, value=1).grid(row = 17, column = 4)
Radiobutton(window, text="Euclidean Distance", padx = 20, variable=choice, value=2).grid(row = 17, column = 5)
Label(window).grid(pady = 7)
btn = Button(window, text = 'Run', command = runfacerecog, height = 1, width = 8).grid(row = 18, column = 4)

window.mainloop()
print('Terima kasih telah menggunakan program ini.')