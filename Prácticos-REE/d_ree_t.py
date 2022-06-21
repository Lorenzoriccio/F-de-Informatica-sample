# 🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
# 🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga entre 3 y 6 letras minúsculas?
import re
string = 'Hola! 123 123. Probando.'
patern = '[a-z]{3,6}'
re.findall(patern, string)

# 🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
import re
texto = "absurdo es estar abajo en la terraza"
patron = "ab"
re.findall(patron , texto)

# 🧗‍♀️Desafio IV: ¿Qué expresión regular usarías para extraer el número de estudiantes que hay en una clase según el siguiente texto:
import re
texto = 'En la clase de Introducción a la programación hay 30 estudiantes' 
lista = re.findall('\d', texto) 
strList = "".join(lista) 
print(strList)

# 🧗‍♀️Desafio V: imprimí el fragmento del texto entre la posición 22 y 26 ¿Qué resultado obtenés? ¿Qué quiere decir el mensaje span?
# 🧗‍♀️Desafio VI: Expresá el patron de búsqueda utilizando lo visto anteriormente sobre metacaracteres y rangos.
'''
>>> re.findall(patron, texto)
['amet', 'amet']''' 