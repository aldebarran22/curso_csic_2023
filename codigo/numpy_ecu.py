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
        print(self.a)

    def crearMatrizA(self):
        m = []
        for ecu in self.L:
            t = ecu.partition('=')  
            aux = t[0].replace('x',',').replace('y',',').replace('z',',')
            Laux = aux.split(',')[:-1]
            Laux = self.chequear(Laux)
            m.append([float(v) for v in Laux])        
        return np.array(m)
    
    def chequear(self, Laux):
        R  = []
        for i in Laux:
            if i == '':
                R.append(1)
            elif i=='-':
                R.append(-1)
            elif i =='+':
                R.append(1)
            else:
                R.append(i)
        return R

    def crearMatrizB(self):
        m = []
        for ecu in self.L:
            t = ecu.partition('=') 
            m.append([float(t[2])])
        return np.array(m)
    
    def resolver1(self):
        return np.linalg.solve(self.a, self.b)

    def resolver2(self):
        if np.linalg.det(self.a) == 0:
            # No se puede calcular.
            # lanzar excepcion o utilizar resolver1
            # Opcion1:
            #raise Exception('No se puede calcular det=0')
            # Opcion2:
            print('El determinante es 0, se aplica metodo1')
            return self.resolver1()
        else:
            return np.linalg.inv(self.a) @ self.b


if __name__=='__main__':
    L = ["3x + 9y - 10z = 24",
         "x - 6y + 4z = -4",
         "10x - 2y + 8z = 20"]
    L2 = ["3x + 2y + z = 1",
          "5x + 3y + 4z = 2",
          "x + y - z = 1"]
    ecu = Ecuaciones(L2)
    resul1 = ecu.resolver1()
    resul2 = ecu.resolver2()
    print(resul1)
    print(resul2)

