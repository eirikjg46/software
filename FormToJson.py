from tkinter import *
import json
from tkinter.filedialog import asksaveasfile

def click():
    with open('test.json', 'w') as f:
        json.dump(personer, f)
        print(personer[0])
        f.close()


window = Tk()
window.geometry('640x300')
window.title('Bilutleie')

#Legg til beskrivelse til hver label i tekst:

firstNameLabel = Label(window, text='Fornavn')
firstNameEntry = Entry(window)

firstNameLabel.pack()
firstNameEntry.pack()

lastNameLabel = Label(window, text='Etternavn')
lastNameEntry = Entry(window)

lastNameLabel.pack()
lastNameEntry.pack()

ageLabel = Label(window, text='Alder')
ageEntry = Entry(window)

ageLabel.pack()
ageEntry.pack()

button = Button(text='Submit', command=click)
button.pack()

firstName = firstNameEntry.get()


r = open('test.json', 'r')

personer = json.load(r)

personer[0] = {
                    'firstName': firstName,
                    'lastName': lastNameEntry['text'],
                    'age': ageEntry['text'],
                }

r.close()
mainloop()