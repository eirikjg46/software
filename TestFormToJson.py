from formToJson import *

def test_input_data_right_type():
    assert firstNameEntry.get() == str
    assert lastNameEntry.get() == str
    assert ageEntry.get() == int
    assert streetAddressEntry.get() == str
    assert cityEntry.get() == str
    assert stateEntry.get() == str
    assert postalCodeEntry.get() == str
    assert phoneNumberEntry.get() == int
    assert brandEntry.get() == str
    assert carTypeEntry.get() == str
    assert carAgeEntry.get() == str
    assert carKmEntry.get() == int
    assert licenceNrEntry.get() == str
    assert daysAvailableEntry.get() == str
    assert gearboxEntry.get() == str
    assert singleDayPriceEntry.get() == int
    assert multiDayPriceEntry.get() == int

def test_does_user_already_exist():
    assert firstNameEntry.get() # Logikk
    assert lastNameEntry.get() # Logikk
    assert phoneNumberEntry.get() # Logikk
    assert streetAddressEntry.get() # Logikk

#Legge til flere tester her:
# Sjekk om det finnes en allerede eksisterende person i JSON fil
# Med mer...

