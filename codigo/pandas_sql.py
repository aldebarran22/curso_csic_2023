"""
Generar ficheros de json a partir de una BD con pandas
"""

from objetos import BaseDatos
import pandas as pd

path = '../curso_csic_2023-main/practicas/pandas/merge/'

def exportarJson(con, *args):
    for tabla in args:
        sql = f"select * from {tabla}"
        print(sql)
        fichero = path+tabla+".json"
        # Cargar el Dataframe de una consulta:
        df = pd.read_sql(sql, con)
        # Exportar a json:
        # force_ascii=False para el texto con acentos:
        df.to_json(fichero, orient="records", indent=4, force_ascii=False)
        print(f'Exportando {tabla}...')

if __name__ == '__main__':
    bd = BaseDatos("./empresa3.db")
    L = ("categorias","pedidos","clientes","empleados")
    exportarJson(bd.con, *L)