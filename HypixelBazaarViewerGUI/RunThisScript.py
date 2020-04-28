import sys
import os
from tkinter import *
#from tkinter import messagebox
#import tkinter as tk
sys.path.insert(1, 'ScriptsAndData')

window = Tk()
window.title("In which modus do you want to run BazaarViewer in?")

def open1():
    window.destroy()
    import EveryProduct
    os.system("EveryProduct.py")
    
    
def open2():
    window.destroy()
    import HighestPriceDifference
    os.system("HighestPriceDifference.py")
    
label = Label(window, text="In which modus do you want to run BazaarViewer in?")


text = Text(window, height=3, width=70)
text.insert(INSERT, "In which modus do you want to run BazaarViewer in?\nYou can search after the item that you can resell for the most money, or the item that has the highest buy-sell difference on the bazaar.")
text.pack()
text.config(state="disabled")


Button1 = Button(window, text="Best margin", command=open1).pack()

Button2 = Button(window, text="Highest difference", command=open2).pack()

mainloop()
