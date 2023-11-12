# pruebas con numpy: ndarray

import numpy as np


L = list(range(10))
print(L)
data1 = np.array([2,56,7,8,9])
data2 = np.array(L)
print(data1)
print(data2)

data3 = np.array([list(range(10)),list(range(10))])
print(data3)

arr = np.array([1, 2, 3])
print(arr)


arr =  np.array([1, 2, 3.0])
print(arr)


arr =  np.array([[1, 2], [3, 4]])
print(arr)
print(arr[0])
print(arr[0][0])


arr =  np.array([1, 2, 3], ndmin=2)
print(arr)
print(arr.dtype)
print(arr.shape)

arr =  np.array([1, 2, 3], dtype=complex)
print(arr)

print("\n-------------------------------------------------")
arr = np.array([1, 2, 3])
print(arr)
print(arr+arr)
print(arr*10)

print("\n-------------------------------------------------")
print(arr[0:2])
print(arr.item(1))
arr[0:2]=100
print(arr)
print("\n-------------------------------------------------")
a = np.random.randn(10)
a *= 10

a.sort()
print(a)
print(a[::-1])

