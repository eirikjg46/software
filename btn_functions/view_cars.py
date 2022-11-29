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

        self.geometry("1400x500")
        self.title('Utforsk biler')

        columns = ('id', 'name', 'age', 'city', 'phoneNumber', 'car', 'singleDay', 'multiDay')

        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.heading('id', text='ID')
        tree.column('id', width=30)
        tree.heading('name', text='Navn')
        tree.column("name", width=150)
        tree.heading('age', text='Alder')
        tree.column("age", width=50)
        tree.heading('city', text='By')
        tree.column("city", width=100)
        tree.heading('phoneNumber', text='Mobil nummer')
        tree.column("phoneNumber", width=100)
        tree.heading('car', text='Bil')
        tree.column("car", width=150)
        tree.heading('singleDay', text='Pris 1-dag')
        tree.column("singleDay", width=100)
        tree.heading('multiDay', text='Pris flere dager')
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
                  width = 55,
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
                        fName = "Fornavn: " + personer[jsonIndex]['firstName']
                        lName = "Etternavn: " + personer[jsonIndex]['lastName']
                        age = "Alder til utleier: " + str(personer[jsonIndex]['age'])
                        address = "Adresse: " + personer[jsonIndex]['address']['streetAddress']
                        city = "By: " + personer[jsonIndex]['address']['city']
                        state = "Fylke: " + personer[jsonIndex]['address']['state']
                        postalCode = "Postnummer: " + personer[jsonIndex]['address']['postalCode']
                        phoneNumber = "Mobilnummer: " + str(personer[jsonIndex]['phoneNumber'])
                        brand = "Bilmerke: " + personer[jsonIndex]['cars']['brand']
                        type = "Modell: " + personer[jsonIndex]['cars']['type']
                        carAge = "Alder til bil: " + personer[jsonIndex]['cars']['age']
                        totalKm = "Total Km: " + str(personer[jsonIndex]['cars']['km'])
                        licenceNumber = "Skilt nummer: " + personer[jsonIndex]['cars']['licencenr']
                        daysAvailable = "Dager tilgjengelig: "
                        gearbox = "Girkasse: " + personer[jsonIndex]['cars']['gearbox']
                        price1Day = "Pris for å leie 1 dag: " + personer[jsonIndex]['cars']['rentOptions'][0]['price'] + "kr"
                        priceMultiDay = "Pris for å leie flere dager: " + personer[jsonIndex]['cars']['rentOptions'][1]['price'] + "kr"

                        #Legger til dager i daysAvailable
                        FIRST = True
                        for day in personer[jsonIndex]['cars']['daysAvailable']:
                                if FIRST:
                                        FIRST = False
                                        daysAvailable += day
                                else:
                                        daysAvailable += ", " + day
                        
                        listbox.insert(END, fName)
                        listbox.insert(END, lName)
                        listbox.insert(END, age)
                        listbox.insert(END, address)
                        listbox.insert(END, city)
                        listbox.insert(END, state)
                        listbox.insert(END, postalCode)
                        listbox.insert(END, phoneNumber)
                        listbox.insert(END, brand)
                        listbox.insert(END, type)
                        listbox.insert(END, carAge)
                        listbox.insert(END, totalKm)
                        listbox.insert(END, licenceNumber)
                        listbox.insert(END, daysAvailable)
                        listbox.insert(END, gearbox)
                        listbox.insert(END, price1Day)
                        listbox.insert(END, priceMultiDay)

                        


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

        

        


        
