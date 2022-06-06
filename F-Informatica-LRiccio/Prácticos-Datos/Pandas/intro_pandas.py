import pandas as pd
import seaborn as sns
import scipy.stats as sspip

# Desafío I y II: Estos métodos aceptan otros parámetros que merecen la pena ser explorados. Descargá a tu computadora la tabla de personas que conforman el Ministerio de Ciencia y Tecnología de 
# Argentina, en formato csv. Cargá (lee) la tabla a un DataFrame de Pandas de nombre personas ¿Qué forma te lectura de 
# archivos usarías? ¿Qué separación entre columnas posee el archivo? ¿Cómo te diste cuenta? 
# Averiguá para qué sirven los parámetro sep, index_col, nrows y header
# personas = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv")
# print(personas.head())
# # sep --> Sirve para separar los datos segun el caracter que le ponga
personas = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";")
# print(personas.head())
# # index_col --> Sirve para usar columnas como etiquetas de fila del DataFrame, ya sea como nombre de cadena o índice de columna.
# # en el siguiente ejemplo, pone a la segunda columna al principio  
# personas_icol = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";", index_col=2)
# print(personas_icol.head())
# # nrows --> Número de filas de archivo a leer. Muestra las primeras n filas.
# personas_nrows = pd.read_csv(r"C:\Users\ulichtenbaum\Downloads\personas_2011.csv", sep=";", nrows=3)
# print(personas_nrows.head())

# filtrado: personas de sexo 1 y menor de 40 años
# filtro = personas[(personas["sexo_id"] == 1) & (personas["edad"] < 40)]
# print(filtro)
# retorna una parte del dataframe original

# describe: de todas las columnas numericas me devuelve los parametros estadisitcos
# print(personas.describe())
# el problema con describe es que se aplica a todas las columnas con tipo de dato numerico, y en algunos no tiene 
# sentido ya que son identificadores.

# personas.info --> devuelve las columnas con tipo de dato y Non-Null Count

# # para convertir el tipo de dato: 
# personas["seniority_level"].astype("string")
# dataframe = dato inmutable --> no se modifica. Para cambiar el tipo de dato entonces tengo que reasignar o reescribir:
# personas["seniority_level"] = personas["seniority_level"].astype("string")

# calcular un dato sobre filtro de otras columnas:
# personas[(personas["sexo_id"] == 1) & (personas["edad"] < 40)]["producciones_ult_4_anios"].mean()

# metodo para filtrar en columnas de tipo str:
# personas[personas["seniority_level"].str.contains("A")]
# str.contains() sirve para encontrar substrings dentro de una columna 

# loc[] --> le paso fila y columna, e imprime la interseccion (Celda)
# personas.loc[19, 'seniority_level']
# si le paso fila e imprime todos los datos de las columnas para esa fila
# personas.loc[19]

# concatenar --> adherir dos dataframes
# categoria_a = personas[personas["seniority_level"].str.contains("A")]
# categoria_b = personas[personas["seniority_level"].str.contains("B")]
# pd.concat([categoria_a, categoria_b])
# me devuelve los seniority level A y despues los B

