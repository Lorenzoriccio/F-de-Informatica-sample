# DESAFÍO I
# 🧗‍♀️ Desafío I: Creá un archivo de prueba (bio.txt) en la carpeta destinada a los prácticos de la materia.
'''
## Primero (antes de entrar a python) entras con cd a la carpeta 
with open('bio.txt', 'w') as file: 
    file.write("Mi nombre es Lorenzo Riccio y tengo 19 años. Estudio en la Ucema.") '''


# DESAFÍO II
# 🧗‍♀️ Desafío II: Investigá sobre los métodos os.mkdir() y os.listdir()
'''El comando de os.mkdir() crea una carpeta nueva ("Make directory")
El comando de os.listdir() te lista los archivos de tu biblioteca ("List directory") '''

# DESAFÍO III
# 🧗‍♀️ Desafío III: Abrí el archivo bio.txt y escribí una mini biografía de presentación. Para pensar 🤔:¿Cómo darías formato al texto que estas creando?
# ya está hecho en el desafío 1
# DESAFÍO IV
# 🧗‍♀️Desafio IV: Descargá el archivo manipulacion_archivos.txt y creá un programa que lea su contenido y lo imprima en pantalla el resultado.

'''
with open('manipulacion_archivos.txt', 'r') as file: 
    file.readlines() '''
