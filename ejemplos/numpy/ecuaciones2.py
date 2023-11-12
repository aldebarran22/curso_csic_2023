"""
Resolver el sistema.
x + 2y + 3z = 6
2x + 5y + 2z = 4
6x - 3y + z = 2
"""

import numpy as np

def resolver(La, Lb):   
    a = np.matrix(La)
    b = np.matrix(Lb)
    print(a)
    print(b)

    x = a**(-1)*b
    print(x)
    x2 = a * x
    print(x2)

La = [[1,2,3],[2,5,2],[6,-3,1]]
Lb = [[6],[4],[2]]
resolver(La, Lb)



