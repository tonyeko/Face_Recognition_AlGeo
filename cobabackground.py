from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
top = Tk()

C = Canvas(top, bg="blue")
filename = ImageTk.PhotoImage(file = "background_image.jpg")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
btn = Button(top, text = 'Run', height = 1, width = 8).pack()
C.pack()
top.mainloop()