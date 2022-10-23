import tkinter as tk
from tkinter import *
from btn_functions.view_cars import view_cars
from btn_functions.lend_your_car import lend_your_car
from btn_functions.log_in import log_in

class BaseLayout(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Testing")
        self.geometry("550x400")
        
        self.view_cars_btn = Button(self, text="Leie bil", padx=50, pady=50, command=lambda: view_cars(self))

        self.lend_your_car_btn = Button(self, text="Utleie av egen bil", padx=50, pady=50, command=lambda: lend_your_car(self))

        self.log_in_btn = Button(self, text="Log In", padx=50, pady=50, command=lambda: log_in(self))

        # Putting the buttons on to the grid
        self.view_cars_btn.grid(row=0, column=0, padx=10, pady=10)
        self.lend_your_car_btn.grid(row=0, column=1, padx=10, pady=10)
        self.log_in_btn.grid(row=0, column=2, padx=10, pady=10)

if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()
