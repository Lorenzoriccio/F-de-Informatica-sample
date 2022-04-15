# EJERCICIO 1
import re 
string = "Profesora del 2022: Ana Julia Velez Rueda"
re.search('\w', string) #funciona porque quiero encontrar al menos 1, pero está ok?

# EJERCICIO 2
import re 
texto = "Tutor de la materia: Guillermo Benitez"
re.search('\W', texto)