import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import json
from base_layout import home

f = open('json_files\personas.json', 'r')
personer = json.load(f)

def view_cars(self):

        for thingy in self.grid_slaves():
                thingy.grid_forget()

        self.geometry("1200x500")
        self.title('Utforsk biler')

        columns = ('id', 'name', 'age', 'city', 'phoneNumber', 'car', 'singleDay', 'multiDay')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.heading('id', text='ID')
        tree.column('id', width=30)
        tree.heading('name', text='Full Name')
        tree.column("name", width=150)
        tree.heading('age', text='Age')
        tree.column("age", width=50)
        tree.heading('city', text='City')
        tree.column("city", width=100)
        tree.heading('phoneNumber', text='Phone Number')
        tree.column("phoneNumber", width=100)
        tree.heading('car', text='Car')
        tree.column("car", width=150)
        tree.heading('singleDay', text='Single-Day Price')
        tree.column("singleDay", width=100)
        tree.heading('multiDay', text='Multi-Day, Price Per Day')
        tree.column("multiDay", width=140)

        contacts = []
        for i in range(len(personer)):
                id = i+1
                fullName = personer[i]['firstName'], personer[i]['lastName']
                age = personer[i]['age']
                city = personer[i]['address']['city']
                phoneNumber = personer[i]['phoneNumber']
                car = personer[i]['cars']['brand'], personer[i]['cars']['type']
                singleDay = personer[i]['cars']['rentOptions'][0]['price']
                multiDay = personer[i]['cars']['rentOptions'][1]['price']

                contacts.append((id, fullName, age, city, phoneNumber, car, singleDay, multiDay))

        # add data to the treeview
        for contact in contacts:
                tree.insert('', tk.END, values=contact)

        listbox = Listbox(self, height = 15,
                  width = 30,
                  bg = "white",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "black")

        listbox.grid(row=0, column=2)

        def item_selected(event):
                for selected_item in tree.selection():

                        listbox.delete(0, END)

                        item = tree.item(selected_item)

                        jsonIndex = item['values'][0]-1
                        fName = "First Name: " + personer[jsonIndex]['firstName']
                        lName = "Last Name: " + personer[jsonIndex]['lastName']
                        age = "Age: " + str(personer[jsonIndex]['age'])
                        address = "Address: " + personer[jsonIndex]['address']['streetAddress']
                        city = "City: " + personer[jsonIndex]['address']['city']
                        state = "State: " + personer[jsonIndex]['address']['state']
                        postalCode = "Postal Code: " + personer[jsonIndex]['address']['postalCode']
                        phoneNumber = "Phone Number: " + str(personer[jsonIndex]['phoneNumber'])


                        listbox.insert(END, fName)
                        listbox.insert(END, lName)
                        listbox.insert(END, age)
                        listbox.insert(END, address)
                        listbox.insert(END, city)
                        listbox.insert(END, state)
                        listbox.insert(END, postalCode)
                        listbox.insert(END, phoneNumber)

                        


        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar_treeview = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar_treeview.set)
        scrollbar_treeview.grid(row=0, column=1, sticky='ns')

        scrollbar_listbox = tk.Scrollbar(self, orient=tk.VERTICAL, command=listbox.yview)
        listbox.config(yscroll=scrollbar_listbox.set)
        scrollbar_listbox.grid(row=0, column=4, sticky='ns')

        home_btn = Button(self, text="Back", padx=50, pady=50, command=lambda: home(self))
        home_btn.grid(row=1, column=0, sticky=W)

        

        


        
