import json

f = open('personas.json', 'r')

#JSON:
data = json.load(f)

for i in data[0]["navn"]:
  print(i)

f.close()
