import facerecog
import tkinter

window = tkinter.Tk()
window.title("Face Recognition")

tkinter.Label(window, text = "Nama File Sample: ").grid(row = 0) # this is placed in 0 0
# 'Entry' is used to display the input-field
tkinter.Entry(window).grid(row = 0, column = 1) # this is placed in 0 1

tkinter.Label(window, text = "T").grid(row = 1) # this is placed in 1 0
tkinter.Entry(window).grid(row = 1, column = 1) # this is placed in 1 1


window.mainloop()

# sample = input("Masukkan nama file: ")
# sample = "Aaron Paul124_221.jpg"
# facerecog.main('1', 10, sample)
