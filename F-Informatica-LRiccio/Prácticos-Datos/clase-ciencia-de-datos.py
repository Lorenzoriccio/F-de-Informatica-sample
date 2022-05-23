import pandas as pd
import seaborn as sns 
import scipy.stats as ss 

'''
# Series
una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')
print(una_serie)

# Dataframe
paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Idioma": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
print(paises_latam) '''
# Desafío I: Estos métodos aceptan otros parámetros que merecen la pena ser explorados. Averiguá para qué sirven los parámetro sep, index_col, nrows y header
personas = pd.read_csv("personas_2011.csv")
print(personas.head())

