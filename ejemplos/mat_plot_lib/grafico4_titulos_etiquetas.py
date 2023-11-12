"""
Dos graficos en la misma ventana indicando titulos, leyendas ...
"""

import matplotlib.pyplot as plt
from random import randint

def main():
    x = list(range(20))
    y = [randint(50,75) for i in range(20)]
    z = [randint(50,75) for i in range(20)]

    plt.suptitle("Gráficas comparativas")

    plt.subplot2grid((1,2),(0,0))
    plt.title("Gráfica1")
    plt.xlabel("x gráfica1")
    plt.ylabel("y gráfica1")
    plt.plot(x, y)

    plt.subplot2grid((1,2),(0,1))
    plt.title("Gráfica2")
    plt.xlabel("x gráfica2")
    plt.ylabel("y gráfica2")
    plt.plot(x, z)

    plt.show()
    

if __name__ == "__main__":
    main()