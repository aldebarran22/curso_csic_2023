import json

d = {"nombre":"Ana", "ape":None, "dir":{"calle":"Pinar", "numero":12}}
s = json.dumps(d)
print(s, type(s))

d2 = json.loads(s)
print(d2, type(d2))

f = open("datos.json","w")
json.dump(d, f)
f.close()

f2 = open("datos.json","r")
d3 = json.load(f2)
print(d3)
f2.close()