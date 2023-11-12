# prueba con pandas

# PAra el resto de funciones:
import pandas as pd
import numpy as np

# Son los dos tipos mas utilizados:
from pandas import Series, DataFrame

#serie de numeros:
obj = Series([4,7,-5,3])
print(obj)

print("valores:", obj.values)
print("Indices:", obj.index)
print("Indices:", list(obj.index))
print()

#Crear una serie indicando los indices:
obj2 = Series([4,7,-5,3], index=['d','b','a','c'])
print(obj2)
print("indices:", obj2.index)
print()

#Se pueden indexar por separado:
print(obj2['d'])
obj2['d']=6
print(obj2)
print()


# filtrado, operaciones, 
print("mayores que 0:")
print(obj2[obj2 > 0])
# operaciones:
print(obj2*2)
print()

# Utilizando una funcion de numpy ....
print(np.exp(obj2))

#Comprobar si existe:
print('b' in obj2)
print('e' in obj2)

#Crear una serie a partir de un dict:
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)

#Es como el anterior pero pasando las claves del dict:
estados = ['California','Ohio','Oregon','Texas']
obj4 = Series(sdata, index=estados)
print("\n\nAdd California")
print(obj4)

#NaN not a number, si uno no lo encuentra

print("Nulos:")
print(pd.isnull(obj4))

print("No Nulos:")
print(pd.notnull(obj4))

# Como metodos:
print("Nulos:")
print(obj4.isnull())

print("No Nulos:")
print(obj4.notnull())

# sumando series:
print(obj3+obj4)

# establecer nombres a la serie y indice:
obj4.name = "poblacion"
obj4.index.name = "estado"
print("Con nombres:")
print(obj4)



