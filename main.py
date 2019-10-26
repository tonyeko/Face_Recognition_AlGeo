import facerecog
import tkinter

def runfacerecog():
    facerecog.main('1', T.get(), sample.get())
    return

window = tkinter.Tk()
window.title("Face Recognition")

sample = tkinter.StringVar()
T = tkinter.IntVar()

tkinter.Label(window, text = "Nama File Sample: ").grid(row = 0, column = 0, padx = 0, pady = 10) # this is placed in 0 0
# 'Entry' is used to display the input-field
tkinter.Entry(window, textvariable = sample).grid(row = 0, column = 1) # this is placed in 0 1
# sample = sample.get()

tkinter.Label(window, text = "T").grid(row = 1, column = 0, padx = 0, pady = 10) # this is placed in 1 0
tkinter.Entry(window, textvariable = T).grid(row = 1, column = 1) # this is placed in 1 1
# T = T.get()

btn = tkinter.Button(window, text = 'Run', command = runfacerecog).grid(row = 2, column = 1)

window.mainloop()

# T = 10
# sample = "Aaron Paul124_221.jpg"

# facerecog.main('1', T, sample)



