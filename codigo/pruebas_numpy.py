"""
Pruebas con la inferencia de tipos
"""

import numpy as np

def inferirTipos():
    a1 = np.array([1,2,4.5])
    print(a1, a1.dtype)
    a2 = np.array([1, 2.3, 4+5j])
    print(a2, a2.dtype)
    a3 = np.array(('23','56','6'), dtype=np.int8)
    print(a3, a3.dtype)
    a4 = a3.astype(np.float32)
    print(a4, a4.dtype)

def variasDim():
    m = np.arange(30).reshape(5,6)
    print(m)
    m = np.arange(100).reshape(2,5,10)
    print(m)
    # Calcula el num. cols
    m = np.arange(30).reshape(5,-1)
    print(m)

def filtros():
    # Filtrar información:
    # Un array de 15 posiciones entre 10 y 50
    arr = np.random.randint(10,50, 15)
    # and & or |
    print('Entre 30 y 40:', arr[(arr >= 30) & (arr <= 40)])
    # Limitar a un valor los mayores de 30
    print('todos:', arr)
    print('indices:',np.where(arr>=30))
    arr[arr > 30] = 30
    print(arr)

    # Indexación multiple, 
    print(arr[[0,2,4]])
    # slicing ...
    print(arr[2:10])

def operadorRelArit():
    arr = np.random.randint(10,50, 10)
    arr2 = np.random.randint(10,50, 10)
    print(arr)
    print(arr2)
    # Enfrenta cada posición
    print(arr > arr2)

    # Operar un escalar contra un array:
    arr = np.array([10, 14, 16, 20, 25])
    arr2 = arr * 2
    print(arr2)
    arr[0] = 1000
    print('arr', arr, id(arr))
    print('arr2', arr2, id(arr2))

def matrices():
    # Generar dos matrices: sumar y multiplicar:
    m1 = np.random.randint(10,20, (5,4))    
    m2 = m1.copy()
    m1[0][0]=999
    print(m1)
    print()
    print(m2)
    m2 = np.random.randint(10,20, (4,5))
    resul = m1 @ m2 # Producto matrices:
    print(resul)

    # Traspuesta
    t = resul.copy().T # resul.traspose()
    print(t)

    # Identidad:
    m = np.eye(5) # np.identity(5)
    print(m)

    # Crear matrices a partir de otras
    print(np.nan)
    m2 = np.full_like(m, fill_value=np.nan)
    print(m2)
    m2[3,4] = 10
    print(m2)

def matrices2():
    m1 = np.random.randint(10,20, (5,5)) 
    print(m1.shape)
    #print(m1.flatten()) # Aplana la matriz
    #print(m1.shape)

    # Quitar el contorno de la matriz:
    print(m1)
    print()
    print(m1[1:-1,1:-1])

def indexar():
    m1 = np.random.randint(10,20, (5,5)) 
    print(m1)
    print()
    indices = [0,2,4]
    print(m1[indices]) # Retorna las filas.
    print(m1[0][indices]) # Retornas los valores de la fila 0
    indices2 = [(1,3),(2,2),(2,4)] # filas 1 y 3
    print('----------------')
    print(m1[indices2])

def np_where():
    # Generar matriz de 4x4 con randn(4,4)
    # Los valores < 0 colocar nan
    m = np.random.randn(4,4)
    print(m)
    resul = np.where(m<0, np.nan, m)
    print(resul)

    m2 = np.random.randn(4,4)
    # Colocar a 0 los que son nan
    resul = np.where(np.isnan(resul), 0, resul)
    print(resul)
    suma = resul + m2
    print(suma)
    


if __name__=='__main__':
    #inferirTipos()
    #variasDim()
    #filtros()
    #operadorRelArit()
    #matrices()
    #matrices2()
    #indexar()
    np_where()