"""
Hacer un estudio de los nombres utilizados
en EEUU en un rango de años.
"""
import pandas as pd

path = "../curso_csic_2023-main/practicas/pandas/names/"

def cargaAño(año):
    fichero = path + f"yob{año}.txt"
    df = pd.read_csv(fichero,\
                  header=None, names=['nombre','sexo','cuenta'])  
    df.set_index(['nombre','sexo'], inplace=True)  
    return df

def sumaMal():
    df1 = pd.read_csv(path+'yob2000.txt',\
                    header=None, names=['nombre','sexo','cuenta'])
    df2 = pd.read_csv(path+'yob2001.txt',\
                    header=None, names=['nombre','sexo','cuenta'])
    suma = df1 + df2
    print(suma.head(3))

def sumaRangosAños(ini, fin):
    primeraVez = True
    for y in range(ini, fin+1):
        df = cargaAño(y)
        if primeraVez:
            #dfTotal =
            pass


if __name__=='__main__':
    df2000 = cargaAño(2000)
    df2001 = cargaAño(2001)
    #suma = df2000 + df2001
    suma = df2000.add(df2001, fill_value=0)
    suma.sort_values(by="cuenta",ascending=False, inplace=True)
    print(suma.head(6))
    # Imprimir cuantas veces se repite: Emily
    print(suma['cuenta']['Emily','F'])
    print(suma.loc['Emily','F']['cuenta'])


