"""
Cargar un fichero npz con la libreria numpy
"""

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt 

argo_data = np.load('argo_float_4901412.npz')
print(type(argo_data))
keys = list(argo_data.keys())
print(keys)
print("type",type(argo_data.f))

tipos = [type(argo_data[t]) for t in keys]
print("tipos", tipos)

# Imprimir datos a partir de las etiquetas:
print("Rango de fechas:", argo_data['date'][0], argo_data['date'][-1])

# Preparar un DataArray:
S = argo_data['S']  #argo_data.f.S
T = argo_data.f.T
P = argo_data.f.P
levels = argo_data.f.levels
lon = argo_data.f.lon
lat = argo_data.f.lat
date = argo_data.f.date
print(S.shape, lon.shape, date.shape)

# Organizar los datos de salinidad:
da_salinidad = xr.DataArray(S, dims=['level', 'date'], coords={'level':levels, 'date':date})
print(da_salinidad)
da_salinidad.plot(yincrease=False)
plt.show()

# Establecer att:
da_salinidad.attrs['units'] = 'PSU'
da_salinidad.attrs['standard_name'] = 'sea_water_salinity'
print(da_salinidad)


