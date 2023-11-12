import matplotlib.pyplot as plt 

# List of Days 
dias = [1, 2, 3, 4, 5] 

# No of Study Hours 
area1 = [7, 8, 6, 11, 7] 

# No of Playing Hours 
area2 = [8, 5, 7, 8, 13] 

area3 = [2,1,1,2,6]

# Stackplot with X, Y, colors value 
plt.stackplot(dias, area1, area2, area3, colors =['r', 'c','y']) 

# Days 
plt.xlabel('Días') 

# No of hours 
plt.ylabel('Horas') 

# Title of Graph 
plt.title('Gráfico de áreas') 

# Displaying Graph 
plt.show() 
