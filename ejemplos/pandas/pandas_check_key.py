from pandas import DataFrame
import pandas as pd


d = {'col1': [1,2,3], 'col2': ['a','b','c']}
columnas = ['col1', 'col2']
indices = ['k1','k2','k3']

df = DataFrame(d, columns=columnas, index=indices)
print(df)
print()

df.ix['k4']=[4,'d']
print(df)
print()

# Duplicar un index:
df.ix['k4']=[5,'e']
print(df)
print()

