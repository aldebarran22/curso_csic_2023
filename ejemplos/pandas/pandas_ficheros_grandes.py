# manejo de fichero grandes

import pandas as pd
from pandas import DataFrame, Series

result = pd.read_csv('ex6.csv')
#print(result)

result = pd.read_csv('ex6.csv', nrows=5)
print(result)

chunker = pd.read_csv('ex6.csv', chunksize=1000)
print(chunker)

tot = Series([])
for piece in chunker:
	print(piece)
	tot = tot.add(piece['key'].value_counts() ,fill_value=0)

#tot = tot.order(ascending=False)
print(tot)
