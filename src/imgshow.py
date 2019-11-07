import cv2
import os   
from tkinter import *
from PIL import ImageTk, Image
from functools import partial

def loading_background_img(self):
    # Add background image
    im = Image.open("img/loading-background.gif")
    backgroundfile = ImageTk.PhotoImage(im)
    background_label = Label(self, image=backgroundfile)
    background_label.image = backgroundfile
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

def background_img(self):
    # Add background image
    im = Image.open("img/background_image.jpg")
    backgroundfile = ImageTk.PhotoImage(im)
    background_label = Label(self, image=backgroundfile)
    background_label.image = backgroundfile
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

def next(subwindow):
    # Hide/Unvisible
    subwindow.withdraw()
    subwindow.quit()
    subwindow.update()

def show_sample_img(path, window):
    name = StringVar()
    name = "Gambar Sampel:      " + os.path.basename(path)
    img = cv2.imread(path)
    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 
    Label(window, text = name).grid(row = 14, column = 6)
    imglabel = Label(window, image=imgtk)
    imglabel.image = imgtk  # keep a reference to the Tkinter object
    imglabel.grid(row = 15, column = 6, rowspan = 7)
    Label(window).grid(pady = 3)
    
def show_img(path, similarity, index, method):
    img = cv2.imread(path)
    b,g,r = cv2.split(img)
    img = cv2.merge((r,g,b))
    # A root window for displaying objects
    subwindow = Toplevel()
    subwindow.geometry('+800+480')

    # set focus to subwindow
    subwindow.focus()
    i = StringVar()
    i = "Gambar ke-"+str(index)
    subwindow.title(i)

    name = StringVar()
    name = "File Name:      " + os.path.basename(path)
    Label(subwindow, text=name).pack()
    
    sim = StringVar()
    if method == 1:
        string = "Similarity: "+ str(similarity) 
    else:
        string = "Distance: "+ str(similarity) 
    sim.set(string)
    Label(subwindow, textvariable=sim).pack()
    
    # Convert the Image object into a TkPhoto object
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im) 

    # Put it in the display window
    Label(subwindow, image=imgtk).pack() 
    # Bind Enter key with Next
    subwindow.bind("<Return>", (lambda event: next(subwindow)))
    # Bind Right key with Next
    subwindow.bind("<Right>", (lambda event: next(subwindow)))
    Button(subwindow, text="Next", command=partial(next, subwindow)).pack()
    subwindow.mainloop()