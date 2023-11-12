"""
Agrupar datos de xarray
"""

import pandas as pd 
import xarray as xr 
import numpy as np

def standardize():
    return (x - x.mean()) / x.std()

ds = xr.Dataset(
    {"foo": (("x","y"), np.random.rand(4,3))},
    coords={"x":[10,20,30,40], "letters":("x", list("abba"))}
)

print(ds)
print("-------------------------------")
print(ds.groupby("letters"))
print("-------------------------------")
print(ds.groupby("letters").groups)
print("-------------------------------")
print(list(ds.groupby("letters").groups))

print("---------------------")
x_bins = [0, 25, 50]
print(ds.groupby_bins("x", x_bins).groups)

# Etiquetado de los intervalos:
x_bins_labels = [12.5, 37.5]
print(ds.groupby_bins("x", x_bins, labels=x_bins_labels).groups)