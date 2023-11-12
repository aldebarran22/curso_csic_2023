# DataFrame con Pandas

from pandas import DataFrame, Series
import pandas as pd
import numpy as np


data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)

#Pasando los nombres de las columnas, será el orden de estas:
frame = DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)

#Igual que en las series si no pasamos un dato, aparecerá NaN
# Y además podemos indicar un indice
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
print(frame2)

print("\n\nColumnas:")
print(frame2.columns)

# Se puede pedir una columna concreta:
print("\nState")
print(frame2['state'])
print()

print("\nAño:")
print(frame2.year)
print()

print("\nDimensiones:")
print(frame2.shape)
print()

print("\nValues:")
L=frame2.values.tolist()
print(L)


# Las filas se pueden indexar:
print("\nFilas:")
print(frame2.ix[0])
print(frame2.ix['one'])

#Modificar una columna:
frame2['debt']=16.5
print("\nModificar col:")
print(frame2)

print("\nModificar col con np.arange:")
frame2['debt']=np.arange(5.)
print(frame2)



# Se pueden añadir series a una col, y sólo tomará los valores que coinciden:
# Y los que no coinciden los deja con NaN
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt']=val
print('\nColumna modificada:')
print(frame2)


# Si se intenta asignar un valor a una columna que NO existe, la crea:
frame2['eastern']=frame2.state == 'Ohio'
print("\nCon una col nueva:")
print(frame2)


# Se puede borrar una col entera:
del frame2['eastern']
print('\nDespues de borrar:')
print(frame2.columns)

# Se puede crear tambien anidando dos dict:
data2 = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(data2)
print(frame3)
print("\nTrasponer:")
print(frame3.T)



