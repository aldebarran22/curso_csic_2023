"""
Limpieza de datos y cambios de tipo en un Dataframe de pandas
Estudiar la correlación de dos variables: presión vs velocidad
"""
import pandas as pd
import numpy as np

path = "../curso_csic_2023-main/practicas/pandas/csv/"

def correlacion(df):
    # Estudiar la correlación entre el viento y la presión
    # np.corrcoef
    tabla = np.corrcoef(df.Wind, df.Pressure)
    return round(tabla[0][1] * 100, 4)

def limpiarDF(fichero):
    df = pd.read_csv(path+fichero, sep=";")
    df.columns = [col.strip() for col in df.columns]
    df['Wind'] = pd.to_numeric(df.Wind.str.replace(' mph',''), \
                               downcast='unsigned')
    df['Pressure'] = pd.to_numeric(df.Pressure.str.replace(' mb',''), \
                               downcast='integer')
    df['Lat'] = pd.to_numeric(df.Lat.str[:-1], downcast='float')
    df['Lon'] = pd.to_numeric(df.Lon.str[:-1], downcast='float')   
    """  infer_datetime_format Deprecated!
    df['DateTime'] = pd.to_datetime(
        " 2005 " + df.Date + " " + df.Time.str.replace(" GMT",""),
        infer_datetime_format=True
    )"""
    df['DateTime'] = pd.to_datetime(
        "2005 " + df.Date + " " + df.Time.str.replace(" GMT",""),
        format="%Y %b %d %H:%M"
    )
    df.drop(columns=['Date','Time'], inplace=True)
    #print(df.info())
    return df

if __name__=='__main__':
    df = limpiarDF('IRMA.csv') 
    print(df.head(3))   
    print('Correlación W y P: ', correlacion(df),'%')

