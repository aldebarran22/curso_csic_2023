"""
Pruebas con colecciones: list, set y dict
"""

def pruebaListas(cadena='Cadena por defecto'):
    """
    Ejemplos con listas
    """
    L = list(cadena)
    print(L)

def histograma(s):
    # Hacer un recuento del numero de veces que se
    # repite cada letra
    # d = {'a':4, ' ':8}
    d = dict()
    for letra in set(s):
        d[letra] = s.count(letra)
    L = sorted(d.items(), key=lambda t:t[1], reverse=True)
    print(L)


"""
def pruebaListas():
    L = list('cadena por defecto')
    print(L)
"""
if __name__=='__main__':
    # Si esta el modulo en ejecución ...
    pruebaListas()
    histograma('Hacer un recuento del numero de veces que se')

