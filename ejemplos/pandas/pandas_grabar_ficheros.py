
import sys
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

data = pd.read_csv('ex5.csv')
print(data)

print(data.to_csv(sys.stdout, sep='|'))
data.to_csv('nuevo_ex5.csv', sep='|')

print(data.to_csv(sys.stdout, index=False, columns=['a','b','c']))


# pruebas con series:

dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
ts.to_csv(sys.stdout) #'ch06/tseries.csv')
