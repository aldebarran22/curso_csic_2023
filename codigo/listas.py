"""
Creacion, acceso, recorrido, slicing, funciones, list compre.
"""
L = [3,4,45,65]
L2 = list(range(20)) # lista del 0 al 19
print(L2)
L3 = list(range(0,101, 5)) # inicio, fin-1, salto
print(L3)

print('El primero:',L3[0])
print('ULtimo: ', L3[-1])
print(L[:5]) # slicing: inicio, fin-1, salto
print(L3[::-1])
print(L)
print('Quitar el primero y el ultimo:', L[1:-1])
path = "C:/home/csic/cv.pdf"
print(path.split('/'))
fichero = path.split('/')[-1]
print(fichero)

for i in enumerate(L):
    print(i)

for k,v in enumerate(L):
    print(k,v)

# Saber si un elemento está en la lista:
print(65 in L)

print('min: ', min(L))
print('max: ', max(L))
print('sum: ', sum(L))
print('media: ', round(sum(L)/len(L),2))

# Generar una lista con las potencias de 2:
L = [2**i for i in range(0,11)]
print(L)

# Generar numeros aleatorios:
from random import randint, seed

seed(1234)
L = [randint(0,100) for _ in range(20)]
L.sort()
print(L)

# Generar con list compr. una lista de tuplas,
# simulando que son horas: [(hh, mm), (hh, mm)]
horas = [(randint(0,23), randint(0,59)) \
          for _ in range(20)]
print(horas)
# (2,4) => 02:04
# (12,4) => 12:04
for t in horas:
    print("%02d:%02d" % t)

# "/home/ficheros/yob1998.txt"
# f-string
for i in range(1990,2000):
    path = f"/home/ficheros/yob{i}.txt"
    print(path)

# listar ficheros de una carpeta:
from os import listdir
path = "../curso_csic_2023-main/practicas/pandas/names"
fichero = "libro1.xlsx"
print(fichero.partition('.'))
años = []
for f in listdir(path):
    # Expande la tupla de tres:
    nombre, _, ext = f.partition('.')    
    if ext == 'txt':
        año = int(nombre[-4:])
        años.append(año)
print(años)


