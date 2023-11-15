
class Fecha:

    def __init__(self, d=1,m=1,y=1970):
        self.d = d
        self.m = m
        self.y = y

    def __str__(self):
        return "%02d/%02d/%d" % (self.d, self.m, self.y)
    
class Hora:

    def __init__(self,H=0,M=0,S=0) -> None:
        self.H=H
        self.M=M
        self.S=S

    def __str__(self):
        return "%02d:%02d:%02d" % (self.H, self.M, self.S)
    
class FechaHora(Hora, Fecha):

    def __init__(self, d=1, m=1, y=1970, H=0, M=0, S=0):
        Fecha.__init__(self,d, m, y)
        Hora.__init__(self, H,M,S)
    
    def __str__(self):
        return Fecha.__str__(self)+ " "+Hora.__str__(self)
    
class FechaHora2:
    # Solución por composición
    def __init__(self, d=1, m=1, y=1970, H=0, M=0, S=0):
        self.fecha = Fecha(d, m, y)
        self.hora = Hora(H,M,S)
    
    def __str__(self):
        return str(self.fecha) + " "+ str(self.hora)
    """
    def __str__(self):
        return 
    """
if __name__=='__main__':
    hoy = Fecha(15,11,2023)
    ahora = Hora(10,35,50)
    print(hoy, ahora)
    fh = FechaHora2(15,11,2023, 1,56,8)
    print(fh)