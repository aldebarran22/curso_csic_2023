"""
3x+9y-10z  =   24
x-6y+4z    =   -4
10x-2y+8z  =  20
"""

import numpy as np 

# Se crean las matrices:
a = np.matrix([[3,9,-10],[1,-6,4],[10,-2,8]])
print(a)
b = np.matrix([[24],[-4],[20]])
print(b)

# Se calcula X = inv(A)*B
x = a**(-1)*b
print("Resultado:")
print(x)

# Para verificar el resultado
# Se debe cumplir que X*A debe de dar B
x2 = a * x
print(x2)