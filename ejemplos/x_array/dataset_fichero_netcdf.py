"""
Cargar un fichero netCDF
"""

import xarray as xr

ds = xr.open_dataset('gistemp1200_ERSSTv5.nc')

print(ds)