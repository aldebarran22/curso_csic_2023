"""
Construye un DataSet
"""

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt 

# Cargar el fichero
argo_data = np.load('argo_float_4901412.npz')

# Preparar los datos:
S = argo_data['S']  #argo_data.f.S
T = argo_data.f.T
P = argo_data.f.P
levels = argo_data.f.levels
lon = argo_data.f.lon
lat = argo_data.f.lat
date = argo_data.f.date

# Preparar el Dataset
ds = xr.Dataset(
    data_vars={'salinidad': (('level', 'date'), S), 
    'temperatura': (('level','date'), T), 
    'presion': (('level','date'),P)},
    coords={'level':levels, 'date':date})
print(ds)

print()

# Modificar el Dataset, añadir coordenadas:
ds.coords['lon'] = ('date', lon)
ds.coords['lat'] = ('date', lat)
print(ds)

print()

# Modificar los valores variables:
#print(ds * 10000)

# Seleccionar por level, por fecha
#ds.salinidad[2].plot()
#ds.salinidad.sel(date='2012-10-22').plot(y='level',yincrease=False)

# Seleccionar una parte con slicing:
#ds.salinidad[:,10].plot()


ds.salinidad.sel(date=slice('2012-10-01','2012-12-01')).plot()

# Visualizar el grafico:
plt.show()

# Operaciones estadísticas:
media = ds.temperatura.mean(dim='date')
print("MEDIA DE TEMPERATURA")
print(media)
