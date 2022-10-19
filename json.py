import json

#Importen blir lagret som et dictionary.

#JSON:
Personer = {
    "firstName": "Olav",
    "lastname": "Larsen",
    "age": 25,
    "address": {
        "streetAddress": "Tangerudveien 30",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0982"
    },
    "phoneNumber": 71892331,
    "cars": {
        "brand": "Audi",
        "type": "Petrol",
        "age": "5 years",
        "km": 62000,
        "licencenr": "KJ 49223",
        "daysAvailable": ["Tuesday", "Wednesday", "Friday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1000"
            },
            {
              "type": "multiDay",
              "price": "850"
            }
        ]
    }
}

{
    "firstName": "Karl",
    "lastname": "Olavesen",
    "age": 35,
    "address": {
        "streetAddress": "Reinergata 10",
        "city": "Raade",
        "state": "Ostfold",
        "postalCode": "1580"
    },
    "phoneNumber": 42112921,
    "cars": {
        "brand": "BMW",
        "type": "Petrol",
        "age": "3 years",
        "km": 29000,
        "licencenr": "KU 33190",
        "daysAvailable": ["Monday", "Tuesday", "Wednesday", "Thursday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1500"
            },
            {
              "type": "multiDay",
              "price": "1200"
            }
        ]
    }
}

{
    "firstName": "Markus",
    "lastname": "Hovstad",
    "age": 40,
    "address": {
        "streetAddress": "Oppsalveien 21 B",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0026"
    },
    "phoneNumber": 97199101,
    "cars": {
        "brand": "Tesla",
        "type": "Electric",
        "age": "2 years",
        "km": 30000,
        "licencenr": "EL 22189",
        "daysAvailable": ["Monday", "Tuesday", "Wednesday", "Friday", "Sunday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1800"
            },
            {
              "type": "multiDay",
              "price": "1500"
            }
        ]
    }
}

{
    "firstName": "Brage",
    "lastname": "Andreasen",
    "age": 21,
    "address": {
        "streetAddress": "Fjerdingbyveien 5 A",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0041"
    },
    "phoneNumber": 81373148,
    "cars": {
        "brand": "Mercedes-Benz",
        "type": "Petrol",
        "age": "5 years",
        "km": 80000,
        "licencenr": "NJ 21392",
        "daysAvailable": ["Wednesday", "Friday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "900"
            },
            {
              "type": "multiDay",
              "price": "650"
            }
        ]
    }
}

{
    "firstName": "Mohammed",
    "lastname": "Abu",
    "age": 22,
    "address": {
        "streetAddress": "Nygata 22 D",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0050"
    },
    "phoneNumber": 93784231,
    "cars": {
        "brand": "BMW",
        "type": "Petrol",
        "age": "4 years",
        "km": 76000,
        "licencenr": "LJ 21440",
        "daysAvailable": ["Friday", "Saturday", "Sunday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1100"
            },
            {
              "type": "multiDay",
              "price": "1000"
            }
        ]
    }
}

{
    "firstName": "Lars",
    "lastname": "Nygaard",
    "age": 29,
    "address": {
        "streetAddress": "Leirdalsgata 19 B",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0044"
    },
    "phoneNumber": 92201380,
    "cars": {
        "brand": "Volvo",
        "type": "Petrol",
        "age": "7 years",
        "km": 110000,
        "licencenr": "LK 92144",
        "daysAvailable": ["Monday", "Tuesday", "Wednesday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "700"
            },
            {
              "type": "multiDay",
              "price": "500"
            }
        ]
    }
}

{
    "firstName": "Ronny",
    "lastname": "Fredriksen",
    "age": 42,
    "address": {
        "streetAddress": "Bydalsgata 12",
        "city": "Fredrikstad",
        "state": "Ostfold",
        "postalCode": "1610"
    },
    "phoneNumber": 93177111,
    "cars": {
        "brand": "Tesla",
        "type": "Electric",
        "age": "2 years",
        "km": 50000,
        "licencenr": "EL 91033",
        "daysAvailable": ["Saturday", "Sunday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1400"
            },
            {
              "type": "multiDay",
              "price": "1200"
            }
        ]
    }
}

{
    
    "firstName": "Sebastian",
    "lastname": "Thomassen",
    "age": 33,
    "address": {
        "streetAddress": "Sentrumsveien 33 B",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0010"
    },
    "phoneNumber": 64892451,
    "cars": {
        "brand": "BMW",
        "type": "Electric",
        "age": "3 years",
        "km": 50000,
        "licencenr": "EL 47823",
        "daysAvailable": ["Monday", "Wednesday", "Friday", "Sunday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1000"
            },
            {
              "type": "multiDay",
              "price": "800"
            }
        ]
    }
}

{
    "firstName": "Ida",
    "lastname": "Karstensen",
    "age": 25,
    "address": {
        "streetAddress": "Pettersgaten 10 A",
        "city": "Fredrikstad",
        "state": "Viken",
        "postalCode": "1659"
    },
    "phoneNumber": 47122981,
    "cars": {
        "brand": "Toyata",
        "type": "Diesel",
        "age": "5 years",
        "km": 80000,
        "licencenr": "AS 23591",
        "daysAvailable": ["Wednesday", "Thursday", "Saturday", "Sunday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1000"
            },
            {
              "type": "multiDay",
              "price": "900"
            }
        ]
    }
}

{
    "firstName": "Petter",
    "lastname": "Hermansen",
    "age": 40,
    "address": {
        "streetAddress": "Fugleveien 1 A",
        "city": "Bergen",
        "state": "Vestland",
        "postalCode": "5012"
    },
    "phoneNumber": 69400321,
    "cars": {
        "brand": "Skoda",
        "type": "Diesel",
        "age": "8 years",
        "km": 103021,
        "licencenr": "SS 43191",
        "daysAvailable": ["Friday", "Saturday", "Sunday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1000"
            },
            {
              "type": "multiDay",
              "price": "700"
            }
        ]
    }
}

{
    "firstName": "Andrea",
    "lastname": "Thorvaldsen",
    "age": 29,
    "address": {
        "streetAddress": "Operagaten 44 D",
        "city": "Oslo",
        "state": "Oslo",
        "postalCode": "0050"
    },
    "phoneNumber": 47871506,
    "cars": {
        "brand": "Mercedes-Benz",
        "type": "Electric",
        "age": "1 years",
        "km": 13501,
        "licencenr": "EL 87000",
        "daysAvailable": ["Monday", "Wednesday", "Sunday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1500"
            },
            {
              "type": "multiDay",
              "price": "1300"
            }
        ]
    }
}

{
    "firstName": "Berit",
    "lastname": "Skogsberg",
    "age": 63,
    "address": {
        "streetAddress": "Operagaten 44 D",
        "city": "Stavanger",
        "state": "Rogaland",
        "postalCode": "4019"
    },
    "phoneNumber": 98231741,
    "cars": {
        "brand": "Honda",
        "type": "Diesel",
        "age": "4 years",
        "km": 50431,
        "licencenr": "RE 67301",
        "daysAvailable": ["Tuesday", "Wednesday", "Friday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1100"
            },
            {
              "type": "multiDay",
              "price": "950"
            }
        ]
    }
}

{
    "firstName": "Kasper",
    "lastname": "Roaldsen",
    "age": 35,
    "address": {
        "streetAddress": "Storhamargata 16 B",
        "city": "Hamar",
        "state": "Innlandet",
        "postalCode": "2315"
    },
    "phoneNumber": 98000221,
    "cars": {
        "brand": "Volkswagen",
        "type": "Petrol",
        "age": "5,5 years",
        "km": 67043,
        "licencenr": "FT 49781",
        "daysAvailable": ["Monday", "Friday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "900"
            },
            {
              "type": "multiDay",
              "price": "700"
            }
        ]
    }
}

{
    "firstName": "Hedda",
    "lastname": "Gabrielsen",
    "age": 19,
    "address": {
        "streetAddress": "Måkeveien 22 A",
        "city": "Sarpsborg",
        "state": "Viken",
        "postalCode": "1718"
    },
    "phoneNumber": 47093421,
    "cars": {
        "brand": "BMW",
        "type": "Electric",
        "age": "2 years",
        "km": 34011,
        "licencenr": "EV 87612",
        "daysAvailable": ["Wednesday", "Friday", "Sunday"],
        "gearbox": "Automatic",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "1400"
            },
            {
              "type": "multiDay",
              "price": "1200"
            }
        ]
    }
}

{
    "firstName": "Thomas",
    "lastname": "Monsen",
    "age": 48,
    "address": {
        "streetAddress": "Notveien 3 B",
        "city": "Bodø",
        "state": "Nordland",
        "postalCode": "8013"
    },
    "phoneNumber": 69100403,
    "cars": {
        "brand": "Ford",
        "type": "Petrol",
        "age": "7 years",
        "km": 96514,
        "licencenr": "YF 32516",
        "daysAvailable": ["Sunday"],
        "gearbox": "Manual",
        "rentOptions": [
            {
              "type": "singleDay",
              "price": "800"
            },
            {
              "type": "multiDay",
              "price": "600"
            }
        ]
    }
}

P = json.loads(Personer)

print(P["navn"])