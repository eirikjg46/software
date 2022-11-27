from formToJson import *
import pytest


def test_input_data_right_type():
    assert type(firstNameEntry.get()) ==  str
    assert type(lastNameEntry.get()) == str
    assert type(int(ageEntry.get() or 0)) == int
    assert type(streetAddressEntry.get()) == str
    assert type(cityEntry.get()) == str
    assert type(stateEntry.get()) == str
    assert type(postalCodeEntry.get()) == str
    assert type(int(phoneNumberEntry.get() or 0)) == int
    assert type(brandEntry.get()) == str
    assert type(carTypeEntry.get()) == str
    assert type(carAgeEntry.get()) == str
    assert type(int(carKmEntry.get() or 0)) == int
    assert type(licenceNrEntry.get()) == str
    assert type(daysAvailableEntry.get()) == str
    assert type(gearboxEntry.get()) == str
    assert type(int(singleDayPriceEntry.get() or 0)) == int
    assert type(int(multiDayPriceEntry.get() or 0)) == int

#Legge til flere tester her:
# Sjekk om det finnes en allerede eksisterende person i JSON fil
# Med mer...

def test_does_phone_nr_exist():
    pass
