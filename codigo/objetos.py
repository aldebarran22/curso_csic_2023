"""
POO. Clase Empleado
"""
import sqlite3 as db
from os.path import isfile
import json

class Empleado:
    """
    Implementación de la clase Empleado: id, nombre, cargo
    """
    def __init__(self, id=0, nombre="", cargo="") -> None:
        # Definición de atributo
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
    
    def __str__(self):
        return str(self.id) + " " + self.nombre + " " +\
        self.cargo
    
    def __repr__(self) -> str:
        return str(self) # return self.__str__()
    
    def __lt__(self, otro):
        # return self.nombre < otro.nombre
        if self.nombre < otro.nombre:
            return True
        else:
            return False
        
    def __del__(self):
        #print('Eliminado: ', self.nombre)
        pass

class Analista(Empleado):

    def __init__(self, id=0, nombre="", cargo="",proyectos=[]) -> None:
        # Llamar al constructor de Empleado:
        #super().__init__(id, nombre, cargo)
        # Otra forma:
        Empleado.__init__(self, id, nombre, cargo)
        self.proyectos = proyectos

    def __str__(self):
        return super().__str__()+ " " + ",".join(self.proyectos)

class BaseDatos:

    def __init__(self, path) -> None:
        if not isfile(path):
            raise FileNotFoundError(f'No existe:{path}')
        else:
            self.con = db.connect(path)

    def select(self):
        sql = "select * from empleados"            
        cur = self.con.cursor()
        cur.execute(sql)
        return [Empleado(*t) for t in cur.fetchall()]

    def __del__(self):
        if hasattr(self, 'con'):
            self.con.close()

def test1():
    base_datos = BaseDatos('./empresa3.db')
    L = base_datos.select()
    L.sort()
    for i in L:
        print(i)

    emp1 = Empleado(10, 'Raquel', 'Ventas')
    print(emp1.__dict__)

    # Convertir a json la colección de empleados:
    Ljson = [e.__dict__ for e in L]
    print(json.dumps(Ljson, indent=4))
    """
    emp1 = Empleado(10, 'Raquel', 'Ventas')
    print(emp1)
    emp2 = Empleado(11, 'Eva', 'Comercial')
    print(emp2)
    print(str(emp2))
    print(emp2.__str__())
    L = [emp1, emp2, Empleado(13,'Jose','Comercial')]
    print(L)
    #L.sort(key=lambda o : o.nombre)
    L.sort()
    print(L)
    """

def test2():
    a1 = Analista(12, 'Jorge','Jefe de Grupo',['App1'])
    a2 = Analista(15, 'Miguel','Jefe de Dpo',['App1','Web1'])
    print(a1)
    if a1 < a2:
        print(a1.nombre,'es menor',a2.nombre)
    else:
        print(a2.nombre,'es menor',a1.nombre)

    print(a1.__class__)    
    print(a1.__class__.__name__)  

    obj = "{}({},'{}','{}',{})" \
        .format("Analista",1,'Pepe','admin',[])
    print(obj)
    an2 = eval(obj)
    print(an2, type(an2))

if __name__=='__main__':
    #test1()
    s = "test2()"
    eval(s)
    print(__file__)

    