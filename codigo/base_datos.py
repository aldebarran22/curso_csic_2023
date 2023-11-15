"""
Ejemplo de conexión y ejecución de una consulta
a una base de datos sqlite3
"""
import sqlite3 as bd
from os.path import isfile

def grabarCategoria(path):
    # Comprobar si existe el fichero de BD:
    if not isfile(path):
        raise FileNotFoundError(f"No existe el fichero:{path}")
    else:
       #Abrir una conexion con la BD:
       con = bd.connect(path)   
       # Crear un cursor para ejecutar SQL
       cur = con.cursor()
       sql = "insert into categorias(id,nombre) values(?,?)"
       cur.execute(sql, (10,'Música'))
       con.commit()
       cur.close()
       con.close()

def abrirConexion(path):
    # Comprobar si existe el fichero de BD:
    if not isfile(path):
        raise FileNotFoundError(f"No existe el fichero:{path}")
    else:
       #Abrir una conexion con la BD:
       con = bd.connect(path)   
       # Crear un cursor para ejecutar SQL
       cur = con.cursor()
       sql = "select * from pedidos where pais=?"
       cur.execute(sql, ("Alemania",))
       cabs = tuple([t[0] for t in cur.description])
       print(cabs)
       for t in cur.fetchall():
           print(t)
       cur.close()
       con.close() 
    

if __name__=='__main__':
    #abrirConexion('empresa3.db')
    grabarCategoria('empresa3.db')