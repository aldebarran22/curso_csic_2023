import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

# 1000 numeros aleatorios entre 0 y 50
x = np.random.randint(0, 50, 1000)

# Correlación positiva con algo de ruido:
y = x + np.random.normal(0, 10, 1000)


# Se calcula la correlación entre las dos variables:
c = np.corrcoef(x, y)
print("Correlacion", c)

plt.scatter(x, y)
plt.show()
