"""
Generar un fichero CSV por cada pais en el fichero
de pedidos.
"""

import pandas as pd

path = '../curso_csic_2023-main/practicas/pandas/merge/'
def exportar():
    df = pd.read_csv(path+'Pedidos.txt',sep=';')
    paises = df.pais.unique()
    for p in paises:
        fichero = path+f'paises/{p}.csv'
        df[df.pais==p].to_csv(fichero, sep=';',index=False, decimal='.')

if __name__=='__main__':
    exportar()