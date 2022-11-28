import tkinter as tk
from tkinter import *
import btn_functions.view_cars
import btn_functions.formToJson
from btn_functions.log_in import log_in
#from btn_functions.imagetest import test #Fjern # for å se bil (brukt til testing)

def home(self):

    for thingy in self.grid_slaves():
        thingy.grid_forget()

    self.title("Testing")
    self.geometry("650x150")
    
    view_cars_btn = Button(self, text="Leie bil", padx=50, pady=50, command=lambda: btn_functions.view_cars.view_cars(self))

    lend_your_car_btn = Button(self, text="Utleie av egen bil", padx=50, pady=50, command=lambda: btn_functions.formToJson.register(self))

    log_in_btn = Button(self, text="Log In (Dummy knapp)", padx=50, pady=50, command=lambda: log_in(self))

    #self.test = Button(self, text="test", padx=50, pady=50, command=lambda: test(self)) #Fjern # for å se bil (brukt til testing)

    # Putting the buttons on to the grid
    view_cars_btn.grid(row=0, column=0, padx=10, pady=10)
    lend_your_car_btn.grid(row=0, column=1, padx=10, pady=10)
    log_in_btn.grid(row=0, column=2, padx=10, pady=10)
    #self.test.grid(row=1, column=2, padx=10, pady=10) #Fjern # for å se bil (brukt til testing)

class BaseLayout(tk.Tk):
    def __init__(self):
        super().__init__()

        home(self)

if __name__ == "__main__":
    base = BaseLayout()
    base.mainloop()



