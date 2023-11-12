import pandas as pd
from pandas import Series, DataFrame


df1 = DataFrame({'key':list('hola'), 'data1': range(4)})
df2 = DataFrame({'key':list('adios'), 'data2': range(5)})
df3 = DataFrame({'key':list('holadios'), 'data3': range(8)})

print('df1')
print(df1)

print('\ndf2')
print(df2)

"""
print('\ndf3')
print(df3)
"""

print('\nMerge:')
dfM = pd.merge(df1, df2)
print(dfM)


print('\nMerge2:')
dfM2 = pd.merge(df1, df3)
print(dfM2)

