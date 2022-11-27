from tkinter import *
import json
import base_layout

def register(self):

    for thingy in self.grid_slaves():
        thingy.grid_forget()

    self.geometry('300x425')
    self.title('Registreringsskjema')

    #Legg til beskrivelse til hver label i tekst:

    firstNameLabel = Label(self, text="Fornavn:")
    lastNameLabel = Label(self, text="Etternavn:")
    ageLabel = Label(self, text="Alder:")
    streetAddressLabel = Label(self, text="Adresse:")
    cityLabel = Label(self, text="By:")
    stateLabel = Label(self, text="Fylke:")
    postalCodeLabel = Label(self, text="Postnr:")
    phoneNumberLabel = Label(self, text="Tlfnr:")
    brandLabel = Label(self, text="Bilmerke:")
    carTypeLabel = Label(self, text="Drivstofftype:")
    carAgeLabel = Label(self, text="Alder av bil:")
    carKmLabel = Label(self, text="Km (tall):")
    licenceNrLabel = Label(self, text="Skiltnr:")
    daysAvailableLabel = Label(self, text="Utleiedager")
    gearboxLabel = Label(self, text="Girtype:")
    singleDayPriceLabel = Label(self, text="En dag's pris:")
    multiDayPriceLabel = Label(self, text="Fler dag's pris:")


    firstNameEntry = Entry(self)
    lastNameEntry = Entry(self)
    ageEntry = Entry(self)
    streetAddressEntry = Entry(self)
    cityEntry = Entry(self)
    stateEntry = Entry(self)
    postalCodeEntry = Entry(self)
    phoneNumberEntry = Entry(self)
    brandEntry = Entry(self)
    carTypeEntry = Entry(self)
    carAgeEntry = Entry(self)
    carKmEntry = Entry(self)
    licenceNrEntry = Entry(self)
    daysAvailableEntry = Entry(self)
    gearboxEntry = Entry(self)
    singleDayPriceEntry = Entry(self)
    multiDayPriceEntry = Entry(self)

    with open('json_files\personas.json', 'r') as f:
            data = json.load(f)   


    def click():
        with open('json_files\personas.json', 'r') as f:
            data = json.load(f)   
            if phoneNumberEntry.get() in data:
                print("The " + phoneNumberEntry.get() + " phone number is already registred!")
                exit("Enter a unique phone number")
                #Can add a message to Tkinter and not a print for better feedback

            elif licenceNrEntry.get() in data:
                print("The " + licenceNrEntry.get() + " licence number is already registred!")
                exit("Enter a unique licence number")
                #Can add a message to Tkinter and not a print for better feedback

            personer = {
                            "firstName": firstNameEntry.get(),
                            "lastName": lastNameEntry.get(),
                            "age": int(ageEntry.get() or 0),
                            "address": {
                                "streetAddress": streetAddressEntry.get(),
                                "city": cityEntry.get(),
                                "state": stateEntry.get(),
                                "postalCode": postalCodeEntry.get()
                            },
                            "phoneNumber": int(phoneNumberEntry.get() or 0),
                            "cars": {
                                "image": "placeholder.png",
                                "brand": brandEntry.get(),
                                "type": carTypeEntry.get(),
                                "age": carAgeEntry.get(),
                                "km": int(carKmEntry.get() or 0),
                                "licencenr": licenceNrEntry.get(),
                                "daysAvailable": [daysAvailableEntry.get()],
                                "gearbox": carTypeEntry.get(),
                                "rentOptions": [
                                    {
                                        "type": "singleDay",
                                        "price": int(singleDayPriceEntry.get() or 0),
                                    },
                                    {
                                        "type": "multiDay",
                                        "price": int(multiDayPriceEntry.get() or 0)
                                    }
                                ]
                            }
                    }


            data.append(personer)  
            
            with open('json_files\personas.json', 'w') as f:
                json.dump(data, f)

    firstNameLabel.grid(row=0, column=1)
    firstNameEntry.grid(row=0, column=2)

    lastNameLabel.grid(row=1, column=1)
    lastNameEntry.grid(row=1, column=2)


    ageLabel.grid(row=2, column=1)
    ageEntry.grid(row=2, column=2)

    streetAddressLabel.grid(row=3, column=1)
    streetAddressEntry.grid(row=3, column=2)

    cityLabel.grid(row=4, column=1)
    cityEntry.grid(row=4, column=2)

    stateLabel.grid(row=5, column=1)
    stateEntry.grid(row=5, column=2)

    postalCodeLabel.grid(row=6, column=1)
    postalCodeEntry.grid(row=6, column=2)

    phoneNumberLabel.grid(row=7, column=1)
    phoneNumberEntry.grid(row=7, column=2)

    brandLabel.grid(row=8, column=1)
    brandEntry.grid(row=8, column=2)

    carTypeLabel.grid(row=9, column=1)
    carTypeEntry.grid(row=9, column=2)

    carAgeLabel.grid(row=10, column=1)
    carAgeEntry.grid(row=10, column=2)

    carKmLabel.grid(row=11, column=1)
    carKmEntry.grid(row=11, column=2)

    licenceNrLabel.grid(row=12, column=1)
    licenceNrEntry.grid(row=12, column=2)

    daysAvailableLabel.grid(row=13, column=1)
    daysAvailableEntry.grid(row=13, column=2)

    gearboxLabel.grid(row=14, column=1)
    gearboxEntry.grid(row=14, column=2)

    singleDayPriceLabel.grid(row=15, column=1)
    singleDayPriceEntry.grid(row=15, column=2)

    multiDayPriceLabel.grid(row=16, column=1)
    multiDayPriceEntry.grid(row=16, column=2)

    button = Button(text='Submit', command=click)
    button.grid(row=17, column=2)

    #Fiks hvis test funker..
    #savebutton = Button(text='Save', command=exitclick)
    #savebutton.grid(row=18, column=2)

    exitbutton = Button(text='Back', command=lambda: base_layout.home(self))
    exitbutton.grid(row=20, column=2)
