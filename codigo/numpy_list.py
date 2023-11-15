"""
Comparativa de t.ejecución entre un array de numpy
y una lista de Python
"""
import numpy as np
from datetime import datetime

my_arr = np.arange(1000000)
my_list = list(range(1000000))

t1 = datetime.now()
for _ in range(10): my_arr2 = my_arr * 2
t2 = datetime.now()
print('Tiempo numpy: ', t2-t1)

t1 = datetime.now()
for _ in range(10): my_list2 = [x*2 for x in my_list]
t2 = datetime.now()
print('Tiempo list: ', t2-t1)