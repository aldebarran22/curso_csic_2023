"""
Varios gráficos en la misma ventana
"""

import matplotlib.pyplot as plt
from random import randint

def main():
    x1 = list(range(10))
    y1 = [randint(10, 30) for i in range(10)]

    x2 = list(range(20))
    y2 = [randint(50, 100) for i in range(20)]

    x3 = list(range(20))
    y3 = [x**2 for x in range(20)]

    plt.subplot2grid((2,2),(0,0))
    plt.plot(x1, y1)

    plt.subplot2grid((2,2),(0,1))
    plt.plot(x2, y2)

    plt.subplot2grid((2,2),(1,0), colspan=2)
    plt.plot(x3, y3)

    plt.show()


if __name__ == "__main__":
    main()