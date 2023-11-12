"""
Varios gráficos en la misma gráfica.
Coincide el mismo eje X y tenemos distintas listas para el eje Y
"""

import matplotlib.pyplot as plt
from random import randint

def main():
    x = list(range(20))
    
    y1 = [randint(10, 30) for i in range(20)]   
    y2 = [randint(50, 100) for i in range(20)]    
    y3 = [x**2 for x in range(20)]
    y4 = [x**1/2 for x in range(20)]

    plt.plot(x, y1)    
    plt.plot(x, y2)    
    plt.plot(x, y3)
  
    plt.show()


if __name__ == "__main__":
    main()