"""
Resolver sistemas lineales de ecuaciones con numpy
"""
import numpy as np

class Ecuaciones:

    def __init__(self, L) -> None:
        self.L = [e.replace(" ","")  for e in L]
        print(self.L)
        self.b = self.crearMatrizB()
        print(self.b)
        self.a = self.crearMatrizA()

    def crearMatrizA(self):
        m = []
        for ecu in self.L:
            t = ecu.partition('=')  
            print(t[0].replace('x',',').replace('y',',').replace('z',','))

    def crearMatrizB(self):
        m = []
        for ecu in self.L:
            t = ecu.partition('=') 
            m.append([int(t[2])])
        return np.array(m)



if __name__=='__main__':
    L = ["3x + 9y - 10z = 24",
         "x - 6y + 4z = -4",
         "10x - 2y + 8z = 20"]
    ecu = Ecuaciones(L)

