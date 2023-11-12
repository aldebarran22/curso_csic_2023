"""
Calcular el determinante y la norma de arrays y matrices
"""

import numpy as np 

a = np.array([1,0,2,-1])
a = a.reshape(2,2)
det = np.linalg.det(a)
print(a)
print('det', det)
n = np.linalg.norm(a)
print('Norma', n)
