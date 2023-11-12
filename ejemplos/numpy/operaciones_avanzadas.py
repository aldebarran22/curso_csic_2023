# operaciones con arrays estructurados:

import numpy as np
import numpy.ma as ma
import random


tipo = [('nombre', 'S10'), ('altura',float),('edad',int)]
valores = [('Arturo Gomez Heredia', 1.8, 44), ('Olga',1.57, 55), ('Andrea',1.65,33)]

a = np.array(valores, dtype=tipo)
print(a)
print(np.sort(a, order='altura'))

print("\n-----------------------------------------")
b = np.array([random.randint(1,100)/ random.randint(1,20) for i in range(20)], dtype=float)
print(b, b.dtype)

print("\nDesv. estandar", np.std(b))
print("\nSuma: ", np.sum(b))
print("\nMedia: ", np.mean(b))

print("\n-----------------------------------------")
print("\nArreglos con mascara")
c = np.array([1,1,1,500-7j,1])
print(c)

m = ma.masked_array(c, mask=[0,0,0,1,0])
print(m)
print(np.mean(m))

m2 = ma.masked_array(a, mask=[0,1,0])
print(m2)

print("\n--------------------------------------------")
np.savetxt('test1.txt', b, delimiter=',')
bb = np.loadtxt('test1.txt', dtype=float)
print(bb)


# varios arrays en el mismo array:
a = np.array([1,2,3,4,5,6])
b = np.array([11,22,33,44,55,66])
c = np.array([111,222,333,444,555,666])

print(a,b,c)
np.savetxt('varios.txt', (a,b,c))
a2,b2,c2 = np.loadtxt('varios.txt')
print(a2,b2,c2)

print("\n--------------------------------------------")
arr = np.arange(10)
print(arr)
np.save('array.bin.npy', arr)
arr2 = np.load('array.bin.npy')
print(arr2)


