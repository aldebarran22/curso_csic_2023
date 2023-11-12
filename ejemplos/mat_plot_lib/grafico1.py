"""
Gráfico de líneas
"""

import matplotlib.pyplot as plt
from random import randint

def main():
    x = list(range(10))
    y = [randint(10, 30) for i in range(10)]

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()