# EJERCICIO 1
import re 
string = "1. Profesora de la metria: Ana Julia Velez Rueda"
re.search('\w', string) #funciona porque quiero encontrar al menos 1, pero está ok?

# EJERCICIO 2
import re 
texto = "2. Tutor de la materia: Guillermo Benitez"
re.search('\W', texto)

# EJERCICIO 3 
# EJERCICIO 4
import re
string = "Defíni la función aprobar_materias"
patron = '\w' + '_' + '\w'
re.search(patron, string) 
