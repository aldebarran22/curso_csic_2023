#cargar datos de ficheros:

import pandas as pd

df = pd.read_csv('datos.txt')
print(df)

print('ix[0]')
print(df.index[0])

#indicar los nombres de las cols, e indicar uno de estos como indice  de las columnas:
print("\n\nPrueba2:")
names = ['a', 'b', 'c', 'd', 'message']
df2 = pd.read_csv('datos.txt', names=names, index_col='message')
print(df2)

#Crear un indice jerarquico a partir de dos columnas:
print("\n\nPrueba3:")
df3 = pd.read_csv('datos2.txt', index_col=['key1','key2'])
print(df3)

print("\n\nPrueba4:")
result = pd.read_csv('datos3.txt', na_values=['NULL'])
print(result)

print("\n\nAnalisis nulos")
print(pd.isnull(result))
