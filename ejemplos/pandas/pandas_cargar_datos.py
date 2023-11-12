# Cargar datos con Pandas

import pandas as pd

movie_names = ['movie_id', 'title', 'genres']
movies = pd.read_table('datos/movies.csv',sep=',') #,header=None, names=movie_names)
print(movies[:5])
print('Numero de pelis', len(movies))
