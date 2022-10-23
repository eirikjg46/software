#Work in progress

#Ting som burde bli lagt til:
# Årsmodell for biler

import json

f = open('json\personas.json', 'r')

#JSON:
personer = json.load(f)

#Viser hva slags keys vi kan hente ut om personene:
#Vi spesifisere person 1, men ettersom alle personene har samme key-values så reflekterer det alle, som vi har det nå.
for keys in personer[0]:
  print(keys)

#Henter ut Fornavn og etternavn til Person 2.
print(personer[1]['firstName'], personer[1]['lastName'])

#Henter ut all dataen vi har om alle fra personas.json filen.
print(personer)

#Henter all dataen om Karl(Person 2)
Karl = personer[1]
print(Karl)

print(personer[0]['image'])

f.close()


