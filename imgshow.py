import cv2
import os   
from tkinter import *
from PIL import ImageTk, Image
from functools import partial

def next(subwindow):
    # Hide/Unvisible
    subwindow.withdraw()
    subwindow.quit()
    subwindow.update()

def show_img(path, similarity, index):
    img = cv2.imread(path)
    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    # A root window for displaying objects
    subwindow = Toplevel()
    if (index != -9999):
        i = StringVar()
        i = "Gambar ke-"+str(index)
        subwindow.title(i)
    else :
        subwindow.title("Gambar Sample")

    name = StringVar()
    name = "File Name:      " + os.path.basename(path)
    Label(subwindow, text=name).pack()
    
    sim = StringVar()
    string = "Similarity: "+ str(similarity) 
    sim.set(string)
    if (similarity != -9999) :
        Label(subwindow, textvariable=sim).pack()
    
    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 

    # Put it in the display window
    Label(subwindow, image=imgtk).pack() 
    Button(subwindow, text="Next", command=partial(next, subwindow)).pack()
    subwindow.mainloop()