import tkinter as tk
from tkinter import *

class BaseLayout(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Testing")
        self.geometry("550x400")
        
        self.view_cars_btn = Button(self, text="Leie bil", padx=50, pady=50, command=self.view_cars)

        self.lend_your_car_btn = Button(self, text="Utleie av egen bil", padx=50, pady=50, command=self.lend_your_car)

        self.log_in_btn = Button(self, text="Log In", padx=50, pady=50, command=self.log_in)

        # Putting the buttons on to the grid
        self.view_cars_btn.grid(row=0, column=0, padx=10, pady=10)
        self.lend_your_car_btn.grid(row=0, column=1, padx=10, pady=10)
        self.log_in_btn.grid(row=0, column=2, padx=10, pady=10)

    def view_cars(self):
        print("Nå ser du på biler. Wow. De er veldig fine.")

    def lend_your_car(self):
        print("Så hyggelig av deg å låne bort din egen bil.")

    def log_in(self):
        print("Imagine å logge inn. Lol.")


if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()
