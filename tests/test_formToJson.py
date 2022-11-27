from btn_functions.formToJson import *
import pytest

def test_input_data_right_type():
    assert type(register.firstNameEntry.get()) ==  str
    assert type(register.lastNameEntry.get()) == str
    assert type(int(register.ageEntry.get() or 0)) == int
    assert type(register.streetAddressEntry.get()) == str
    assert type(register.cityEntry.get()) == str
    assert type(register.stateEntry.get()) == str
    assert type(register.postalCodeEntry.get()) == str
    assert type(int(register.phoneNumberEntry.get() or 0)) == int
    assert type(register.brandEntry.get()) == str
    assert type(register.carTypeEntry.get()) == str
    assert type(register.carAgeEntry.get()) == str
    assert type(int(register.carKmEntry.get() or 0)) == int
    assert type(register.licenceNrEntry.get()) == str
    assert type(register.daysAvailableEntry.get()) == str
    assert type(register.gearboxEntry.get()) == str
    assert type(int(register.singleDayPriceEntry.get() or 0)) == int
    assert type(int(register.multiDayPriceEntry.get() or 0)) == int

# Med mer...
