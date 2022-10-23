import tkinter as tk
from tkinter import *

def view_cars(self):
        print("Nå ser du på biler. Wow. De er veldig fine.")
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(self)
    
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
    
        # sets the geometry of toplevel
        newWindow.geometry("200x200")
    
        # A Label widget to show in toplevel
        Label(newWindow, text ="This is a new window").pack()
