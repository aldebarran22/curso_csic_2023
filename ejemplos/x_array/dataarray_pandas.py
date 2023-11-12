"""
Cargar datos de pandas y luego pasarlos a xarray
"""

import pandas as pd 
import xarray as xr 


df = pd.read_csv("IRMA.csv",sep=';')

# Cargar el dataset a partir de un DataFrame
ds = xr.Dataset.from_dataframe(df)
print(ds)

print("---------------------")

# Convertir a un DataFrame de pandas
df = ds.to_dataframe()
print(df)
