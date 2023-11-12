"""
Dataset.map
"""

import numpy as np 
import xarray as xr
from xarray import Dataset, DataArray

da = DataArray(np.random.randn(2,3))
ds = Dataset({"var1":da, "var2":("x", [-1,2])})

print(ds)
ds_abs = ds.map(np.fabs)
print()
print(ds_abs)
