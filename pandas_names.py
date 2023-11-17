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
        errores = [] 
        primeraVez = True
        for y in range(ini, fin+1):
            try:
                df = cargaAño(y)
                if primeraVez:
                    dfTotal = df
                    primeraVez = False
                else:
                    dfTotal = dfTotal.add(df, fill_value=0)
            except Exception as e:
                errores.append(y)
        if errores != []: print('Errores:',errores)
        dfTotal.sort_values(by="cuenta", ascending=False, inplace=True)
        return dfTotal

def concatenarAños(ini, fin):
    yy = []
    for y in range(ini, fin+1):
        try:
            df = cargaAño(y)
            # Elimina el index pero no borra los datos
            df.reset_index(inplace=True, allow_duplicates=True)
            df['año'] = y
            df = df[['nombre','año','sexo','cuenta']]
            #print(y, df.shape)
            print(df.head(3))
            yy.append(df)
        except Exception as e:
            print(e)
    dfTotal = pd.concat(yy, ignore_index=True)
    # Ordenar primero por año y luego por nombre:
    dfTotal.sort_values(by=['año','nombre'], inplace=True)
    dfTotal.to_html(f'estudio_{ini}_{fin}.html')
    return dfTotal

if __name__=='__main__':
    """
    df2000 = cargaAño(2000)
    df2001 = cargaAño(2001)
    #suma = df2000 + df2001
    suma = df2000.add(df2001, fill_value=0)
    suma.sort_values(by="cuenta",ascending=False, inplace=True)
    print(suma.head(6))
    # Imprimir cuantas veces se repite: Emily
    print(suma['cuenta']['Emily','F'])
    print(suma.loc['Emily','F']['cuenta'])"""
    #print(sumaRangosAños(2015,2018))
    df = concatenarAños(2010, 2012)
    print(df.shape)
    #print(df.loc['Emily'])
    


