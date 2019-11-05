# from functools import partial
# import tkinter
 
# APP_TITLE = "Main Window"
# APP_XPOS = 100
# APP_YPOS = 100
# APP_WIDTH = 350
# APP_HEIGHT = 200
 
 
# def mdfNames(mdf):
#     mdf.destroy()
       
# def mdfPanel():
#     mdf = tkinter.Toplevel()
#     mdf.title("Top Level Window")
#     mdfSize = 220
#     mdf.geometry('%dx%d+%d+%d' % (
#         mdfSize, mdfSize, (mdf.winfo_screenwidth()-mdfSize)/2,
#         (mdf.winfo_screenheight()-mdfSize)/2))                
  
#     tkinter.Button(mdf, text="Start", command=partial(mdfNames, mdf)
#         ).grid(row=7,column=1, columnspan=2)
            
# def main():
#     app_win = tkinter.Tk()
#     app_win.title(APP_TITLE)
#     app_win.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
#     app_win.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
     
#     app = mdfPanel()
     
#     app_win.mainloop()
  
  
# if __name__ == '__main__':
#     main()      






# from tkinter import *

# window = Tk()

# def close_window (): 
#     frame.destroy()

# frame = Frame(window)
# frame.pack()
# button = Button (frame, text = "Good-bye.", command = close_window)
# button.pack()

# window.mainloop()


from tkinter import *
import random
import math

root = Tk()
canvas = Canvas(root)
background_image=PhotoImage(file="datauji/Aaron Paul124_221.jpg")
canvas.pack(fill=BOTH, expand=1) # Stretch canvas to root window size.
image = canvas.create_image(0, 0, anchor=NW, image=background_image)
root.wm_geometry("794x370")
root.title('Map')

def toplevel():
    top = Toplevel()
    top.title('Optimized Map')
    top.wm_geometry("794x370")
    optimized_canvas = Canvas(top)
    optimized_canvas.pack(fill=BOTH, expand=1)
    optimized_image = optimized_canvas.create_image(0, 0, anchor=NW, image=background_image)

toplevel()

root.mainloop()