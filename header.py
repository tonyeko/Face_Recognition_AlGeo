from tkinter import *

text = r"""
 ______                  , __                                                   
(_) |                   /|/  \                            o     o               
   _|_  __,   __   _     |___/  _   __   __   __,  _  _     _|_     __   _  _   
  / | |/  |  /    |/     | \   |/  /    /  \_/  | / |/ |  |  |  |  /  \_/ |/ |  
 (_/   \_/|_/\___/|__/   |  \_/|__/\___/\__/ \_/|/  |  |_/|_/|_/|_/\__/   |  |_/
                                               /|                               
                                               \|                               
            
  """

root = Tk()
Label(root, justify=LEFT, text=text).pack()
root.mainloop()