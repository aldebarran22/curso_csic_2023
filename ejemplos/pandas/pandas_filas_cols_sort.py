from pandas import DataFrame

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
print()

# Cambiar los indices de las filas:
frame.index = [i for i in range(10,15)]
print(frame)

print()
print('Numero de filas:', len(frame.index))
print('Numero de cols: ', len(frame.columns))
print()

# Operaciones con filas:
print(frame[2:5])
print()

# Ordenar por la col pop DESC:
print('Ordenado:')
df = frame.sort_values(frame.columns[2], ascending=False)
print(df)


