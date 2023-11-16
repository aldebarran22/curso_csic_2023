import unittest
from pandas_paises import path, exportar
from os import listdir, remove
import pandas as pd

class EjemploPruebas(unittest.TestCase): 

    def setUp(self) -> None:
        exportar() # Generar los ficheros

    def testNumFicheros(self): 
        """Comprobar si coincide el número de ficheros
        de la carpeta con el número de paises en el DF. Pedidos"""
        path_paises = path+"paises"
        numFicheros = len(listdir(path_paises))
        df = pd.read_csv(path+'Pedidos.txt',sep=';')
        numPaises = len(df.pais.unique())
        self.assertEqual(numFicheros, numPaises, \
                         msg="No coinciden los ficheros y los paises")

    def testNombreFicheros(self):
        """Comprobar si coincide el nombre de los ficheros
        de la carpeta con el nombre de los paises en el DF. Pedidos"""
        path_paises = path+"paises"
        ficheros = [t.partition('.')[0] for t in listdir(path_paises)]
        ficheros.sort()
        df = pd.read_csv(path+'Pedidos.txt',sep=';')
        paises = sorted(df.pais.unique())
        self.assertEqual(ficheros, paises, msg="No coinciden los nombres")
        
    def tearDown(self) -> None:
        for f in listdir(path+'paises'):
            remove(path+'paises/'+f)
        

if __name__ == "__main__": 
    unittest.main()