"""
Extraer las funciones del modulo 1
"""

from inspect import getmembers, isfunction
import modulo1

print("Las funciones del modulo1:")
L = [f for f in getmembers(modulo1) if isfunction(f[1])]
print(L)
for nombre, f in L:
	print("\nEjecutar la funcion: ", nombre)
	f()
	
