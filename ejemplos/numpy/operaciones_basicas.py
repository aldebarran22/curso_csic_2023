# operaciones basicas:

import numpy as np
from numpy import *

a = np.arange(1,7)
print(a)
print(np.arange(20))
print(np.arange(5,10))
print(np.zeros((2,3,4)))
print(np.empty((2,10)))
print(a.size)
print(a.itemsize)
print(a.nbytes)

a.fill(10)
print(a)

print(a.astype(complex))
print(a)

print("\n--------------------------------------")
x = np.array([1,8,0])
y = np.array([5,-1,4])
print(x * y)
print(x.dot(y))
print(inner(x,y))

print("\nProducto externo:")
print(outer(x,y))

print("\n--------------------------------------")
a = np.arange(20)
a[0] = 100
print(a)
a[a > 5] = 5
print(a)
print("\n--------------------------------------")
a = np.arange(15).reshape(3,5)
print(a)
print(a.T)
print("\n--------------------------------------")
print(np.random.randn(20))
print("\n--------------------------------------")
a = np.arange(10)
print(np.sqrt(a))
print(np.exp(a))
print("\n--------------------------------------")
x = np.random.randn(5)
x = x * 10
print(x)

y = np.random.randn(5)
y = y * 10
print(y)

print(np.maximum(x,y))
