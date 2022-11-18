import tkinter as tk
from tkinter import *


root = Tk()
root.title('Widget testing')
root.geometry("400x400")

def something():
    for thingy in root.grid_slaves():
        thingy.grid_forget()
    root.geometry("500x500")
    new_label = Label(root, text="All the previous widgets are removed.")
    new_label.grid(row=0, column=0, padx=0, pady=20)
    
mylabel = Label(root, text="This is the text", font=("Helvetica", 20))
mylabel.grid(row=0, column=0, padx=0, pady=10)

mybutton = Button(root, text="Press me!", command=something)
mybutton.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()