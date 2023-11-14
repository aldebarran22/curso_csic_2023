"""
Diccionarios: creación, acceso, funciones
"""

# Ojo, las claves inmutables!
d = {'a':1, 'b':2, 'c':3}
try:
    d2 = {[1,2]:5, [3,4]:7}
except Exception as e:
    print(e.__class__.__name__, e)

s = "adios"
L = list(range(5))
d = dict(zip(s, L))
print(d)
d2 = dict(zip(L, s))
print(d2)

# rellenar valores en un dict con dos colecciones desiguales
# cargar csv en un dict

