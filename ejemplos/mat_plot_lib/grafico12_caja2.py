import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(123) 
dataline1 = np.random.normal( loc=50, scale=20, size=18 ) 
dataline2 = np.random.normal( loc=30, scale=10, size=18 ) 
data = np.stack( [ dataline1, dataline2 ], axis=1 ) 
plt.boxplot(data)
plt.show()