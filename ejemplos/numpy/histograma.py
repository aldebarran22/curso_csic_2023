import numpy as np

np.random.seed(1)

# 1000 numeros aleatorios entre 0 y 50
x = np.random.randint(0, 20, 1000)

index = np.arange(0,20)

v, i = np.histogram(x, index)
print(v)
print(i)

# Contar de prueba el valor 0:
cont = len([val for val in x if val == 0])
print("0:", cont)

