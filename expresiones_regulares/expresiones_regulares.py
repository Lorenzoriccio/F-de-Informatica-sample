# EJERCICIO 1
# Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re 
str = "1. Profesora de la materia: Ana Julia Velez Rueda"
def caracter_permitido(str):
    print(re.search('\w', str))  

caracter_permitido(str) 

# EJERCICIO 2
#Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re 
texto = "2. Tutor de la materia: Guillermo Benitez"
def funcion_2(texto): 
    print(re.search('\W', texto))

funcion_2(texto) 

# EJERCICIO 3 
'''Creá un programa que verifique las siguientes condiciones:
si un string dado tiene una h seguida de ninguna o más e.
si un string dado tiene una h seguida de una o más e.
si un string dado tiene una h seguida de una o más e.
si un string dado tiene una h seguida de dos o tres e.'''

import re
texto = input('Inserte su texto: ')
patern1 = 'he?'
patern2 = 'he+'
patern3 = 'he{2,3}'

def verificar(texto): 
    cond1 = re.search(patern1, texto)
    cond2 = re.search(patern2, texto)
    cond3 = re.search(patern3, texto)
    if cond3 is None: 
        if cond2 is not None:
            print('Se cumplieron las dos condiciones primeras')
        elif cond1 is not None: 
            print('Se cumplió sólo la condición primera')
        else:
            print('No se cumplió ninguna condición')
    else: 
        print('Se cumplieron las tres condiciones!') 

verificar(texto) 

# EJERCICIO 4
# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).
import re
string = "Defíni la función aprobar_materias"
patron = '\w_\w'
def funcion_4(string): 
    print(re.search(patron, string))


funcion_4(string) 

# EJERICIO 5
# Escribí un programa que diga si un string empieza con un número específico.
import re
str = input("ingrese una cadena de caracteres: ")
num = int(input('ingresa el número: '))
patron = "^3"
def funcion_5(str):
    if re.match(patron, str) is not None:
        print("el string comienza con el numero 3")
    else:
        print("el string no empieza con el numero 3")

funcion_5(str) 

# EJERICIO 6
# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
import re
lista = ["hola", "te", "ayer"]
frase = "hola como te sentis hoy?"

def funcion_6(lista, frase):
    for palabra in lista:
        if re.search(palabra, frase) is not None:
            print("la palabra '", palabra, "' está en la frase")
        else:
            print("la palabra '", palabra, "' no está en la frase") 

funcion_6(lista, frase) 

# EJERICIO 7
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.
import re
string = input('Inserte el string: ')
def funcion_7(string):
    if re.search('\w\s', string):
        print('Cumple las condiciones')
    else:
        print('No cumple las condiciones')

funcion_7(string) 

# EJERICIO 8
# Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
str = input('Ingrese un texto: ')
patron = '\d'
def funcion_8(str): 
    print(re.findall(patron, str))

funcion_8(str)  

# EJERICIO 9
'''Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: 
"Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")'''
# import re
# texto = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
# patron = '-' + '.+' + '-'
# re.findall(patron, texto) PREGUNTAR POR QUÉ ESTÁ MAL!
# Si lo sumas te busca el string exacto, no un patrón 

import re
string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
patron = "-(.*?)-"
print(re.findall(patron, string)) 
# imprime lo que está entre guiones

import re
def funcion_9(string):
    return re.sub('-(.*?)-', '', string)

print(funcion_9("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")) 
# imprime todo menos lo que está entre guiones

# EJERICIO 10
# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.
# EJERICIO 11
'''Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista 
de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).'''
import re
lista_strings = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
patron = "(P\w*)\s(P\w*)"
def funcion_11(lista_strings): 
    for string in lista_strings:
        coincidencia = re.search(patron, string)
        if coincidencia is not None:
            print(coincidencia.group())  

funcion_11(lista_strings) 

# EJERICIO 12
# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).
import re 
testo = 'En esta guía estamos trabajando con: expresiones_regulares! Wacala.'
patern = '[\s_:]'
re.sub(patern, '|', testo)

# EJERICIO 13
# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
def replace_primeros(string): 
    print(re.sub('\W', '_', string, 2)) 
    '''El 2 al final te indica cuántas veces querés que los reemplace (los n primeros). 
    Si poner {2} seria las n veces que ese mismo caracater aparece '''

# EJERICIO 14
# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.
import re
texto = '''Buen día.           Hoy no es.'''
patern = '[\s\t]'
re.sub(patern,';', texto)

# EJERICIO 15
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.
import re
def validar_mail (mail):
    return bool(re.search("[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+@[a-zA-Z]{2,9}(\.[a-zA-z]{2,4})",mail))

print(validar_mail("lorenzo.riccio@gmail.com")) 

# EJERCICIO EXTRA INVENTADO!
# Hacer un programa usando funciones regulares que valide ambos correos
import re
urls = '''https://google.com
http://ong.org'''
patern = 'https?://\w+\.\w{3}' 
print(re.findall(patern, urls))  