import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import json

f = open('json_files\personas.json', 'r')
personer = json.load(f)

def view_cars(self):
        print("Nå ser du på biler. Wow. De er veldig fine.")
        # Toplevel object which will
        # be treated as a new window
        newWindow = Toplevel(self)
    
        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")
    
        # sets the geometry of toplevel
        newWindow.geometry("1000x400")

        columns = ('id', 'name', 'age', 'city', 'phoneNumber', 'car', 'singleDay', 'multiDay')

        tree = ttk.Treeview(newWindow, columns=columns, show='headings')

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


        def item_selected(event):
                for selected_item in tree.selection():
                        item = tree.item(selected_item)
                        record = item['values']
                        # show a message
                        showinfo(title='Information', message=','.join(record))


        tree.bind('<<TreeviewSelect>>', item_selected)

        tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(newWindow, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')


        
