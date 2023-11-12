"""
Ejemplos para crear DataArray
"""

from xarray import DataArray
import matplotlib.pyplot as plt 

# DataArray sin dimensiones o coordenadas:
L = list(range(10))
da1 = DataArray(L)
print(da1)

print()

# Se puede añadir un nombre a la dimension:
da2 = DataArray(L, dims=['x'])
print(da2)

print()

# Añadimos dimensiones y coordenadas: Las coordenadas tienen el mismo numero que los values:
da3 = DataArray([9,0,2,1,0], dims=['x'], coords={'x': [10,20,30,40,50]})
print(da3)
da3.plot(marker='o')
plt.show()


