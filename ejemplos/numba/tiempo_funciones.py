"""
Ejemplo de medición de tiempo de dos funciones que suman un array de 1000 x 1000
Por un lado con numoy y por otro con dos bucles anidados
"""

import numba
import timeit
import numpy as np



def suma_numpy(arr):
    #np.random.rand(1000,1000)
    return np.sum(arr)

def suma_python(arr):
    #arr = np.random.rand(1000,1000)
    N, M = arr.shape
    suma = 0
    for i in range(N):
        for j in range(M):
            suma += arr[i,j]
    return suma

@numba.jit
def suma_numba(arr):
    #arr = np.random.rand(1000,1000)
    N, M = arr.shape
    suma = 0
    for i in range(N):
        for j in range(M):
            suma += arr[i,j]
    return suma


if __name__ == "__main__":        
    print("timeit con numpy: ", timeit.timeit("suma_numba()", setup="from __main__ import suma_numba"))
    #print("Suma python: ", suma_python(arr))
    print("fin ...")