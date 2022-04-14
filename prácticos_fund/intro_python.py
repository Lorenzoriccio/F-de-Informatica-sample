# Tarea para clase 3
"""Crear script que arme la carpeta “datos_personales” y guarde allí un archivo con:
tu nombre, apellido y edad en users: 
Si quiero guardarlo en una carpeta: 

>>> import os 
>>> path = 'C:\\Users\\Usuario\\Desktop\\UNIVERSIDAD\\codigo_informatica_ss'
>>> os.chdir(path)
>>> os.getcwd()
'C:\\Users\\Usuario\\Desktop\\UNIVERSIDAD\\codigo_informatica_ss'
>>> path = path + '\\datos_personales'
>>> path
'C:\\Users\\Usuario\\Desktop\\UNIVERSIDAD\\codigo_informatica_ss\\datos_personales'
>>> with open(path, 'w') as datos_personales: 
...     datos_personales.write('Lorenzo Riccio con 19 años')
... 
26
>>> datos_personales.close()

Si lo quiero guardar en Users(predeterminado)
>>> import os 
>>> datos_personales = open('datos_personales', 'w')
>>> datos_personales.write('Lorenzo Riccio con 19 años)
>>> datos_personales.close()
"""

# Parte 1 de python 
# EJERCICIO 1
def longitud(string): 
    return len(string)

# EJERCICIO 2
string = input("Ingrese una frase: ")
if len(string) >= 6: 
  print(str.upperstring[4:6])
else: 
  print("Su frase no tiene suficientes caracteres, por favor intente nuevamente")

# EJERCICIO 3
nombre_completo = input("Ingrese su nombre y apellido: ")
print("Hola ", nombre_completo)

# EJERCICIO 4
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
print(str.upper(nombre[0]), str.upper(apellido[0]), str.upper(apellido2[0]))

# EJERCICIO 5
def promedio_numeros(un_numero, otro_numero, ultimo_numero): 
  return (un_numero + otro_numero + ultimo_numero) // 3

# EJERCICIO 6
minutos = int(input("Ingrese una cantidad de minutos "))
print(minutos // 60, "horas y ", (minutos%60), " minutos")

# EJERCICIO 7
def sueldo(base, ventas): 
  comision = base * 0.1
  return base + (comision * ventas)

# EJERCICIO 8
def nota_final(respuestas): 
  resultado = 0 
  for respuesta in respuestas: 
    if respuesta == "correcta": 
      resultado += 4
    elif respuesta == "incorrecta": 
      resultado -= 1
    else: 
      resultado = resultado 
  return resultado 

"""Ejemplo de invocación del 8: 
resultado = ("correcta", "correcta", "incorrecta", "blanco")
nota_final(resultado)
7 """

# EJERCICIO GRUPAL

# Parte 2 de python
# EJERCICIO 1 (condicionales)
str = input("Ingrese una palabra o una frase: ")
cap = str.capitalize() #sino puedo usar str.isupper[0]
if str == cap: 
  print("la primer letra es mayúscula.")
else: 
  print("la primer letra es minúscula")

# EJERCICIO 2 (condicionales)
numero = int(input("Ingrese un número: "))
if numero > 0: 
  print("es positivo")
  if numero%2 == 0: 
    print("es par")
  else: 
    print("es impar")
elif numero < 0: 
  print("es negativo")
  if numero%2 == 0: 
    print("es par")
  else: 
    print("es impar")
else: 
  print("es cero y par")

# EJERCICIO 3 (condicionales)
num = int(input("Escribí un número del 1 al 6: "))
if  num >= 1 or num <= 6: 
  print("la cara opuesta del dado es ") + str(7 - num)
else: 
  print("el número ingresado es incorrecto") 

# EJERCICIO 4 (condicionales)
peso_paquete = int(input("Ingrese el peso del paquete: "))
lugar = input("Ingrese la ubicación de la entrega: ")
costos_ubicacion = {"America del sur": "10usd", "America central": "15usd", "America del norte": "18usd", "Europa": "24usd", "Asia": "30usd"}
if peso_paquete <= 5: 
  print("el cobro por entrega es " + costos_ubicacion[lugar])  
else: 
  print("su entrega fue rechazada, no puede transportarse por exceso de peso")

# EJERCICIO 5 (condicionales)
num_dia = int(input("Ingrese el número del día del 1 al 7: "))
dias_semana = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6:"Sábado", 7:"Domingo"}
if num_dia > 7 or num_dia < 1: 
  print("el número ingresado es inválido, intentelo nuevamente")
else: 
  print(dias_semana[num_dia])

# EJERCICIO 6 (listas)
lista = [input(), input(), input(), input(), input()]
lista_invertida = [lista[4], lista[3], lista[2], lista[1], lista[0]] #chequear por qué no se puede lista[-1]
print(lista_invertida)
''' sino también lo puedo hacer con strings inventados?: 
lista = ['pan', 'queso', 'aprobar', 'quedar', 'cansado'] 
lista2 = list(lista1)
lista_invertida = lista2[::-1] 
''' #el [::-1] funciona para invertir todos los elementos de la lista

# EJERCICIO 7 (listas)
numero = int(input("Ingrese un número: "))
lista_num = [] 
while numero >= 0:
  lista_num.append(numero)
print(lista_num)
#  print(list.append(lista_num, numero)) 

# EJERCICIO 8 (listas)
Lista1 = [int(input("ingrese 5 numeros, uno por linea: ")), int(input()), int(input()), int(input()), int(input())]
Lista2 = [int(input("ingrese 5 numeros nuevamente: ")), int(input()), int(input()), int(input()), int(input())]
Lista3 = [Lista1[0]+Lista2[0], Lista1[1]+Lista2[1], Lista1[2]+Lista2[2], Lista1[3]+Lista2[3], Lista1[4]+Lista2[4]]
print(Lista3)

# EJERCICIO 9 (listas)
lista_nombre = []
lista_edad = []
nombre = input('ingrese el nombre del alumno: ')
edad = input('ingrese la edad del alumno: ')
while nombre != "*":
    lista_nombre.append(nombre)   
    lista_edad.append(edad)
    nombre = input('ingrese el nombre del alumno: ')
    if nombre == "*":
        continue
    edad = input('ingrese la edad del alumno: ')
print("la edad máxima de los alumnos es: " + max(lista_edad))
dic = {"lista_nombre" : "lista_edad"} 

# EJERCICIO 10 (diccionarios)
contadores = {} 
cadena = input("Escribí una cadena de caracteres: ") 
for caracter in cadena: 
  contadores[caracter] += 1
else: 
  contadores[caracter] = 1

for clave, valor in contadores.items(): 
  print(clave, valor)

# EJERCICIO 11 (diccionarios)
contadores = {} 
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto + alfabeto.upper(): 
  contadores[letra] = 0

cadena = input("Escribí una cadena de caracteres: ")

for caracter in cadena: 
  if caracter.lower() in alfabeto: 
    contadores[caracter] += 1

for campo, valor in contadores.items(): 
  print (campo, valor)

# EJERCICIO 12 (diccionarios)
cantidad = int(input("Introducir cantidad de alumnos: "))
alumnos = {} 

for numero in range(cantidad): 
  alumno = input("alumno: ")
  notas = [] 
  nota = int(input("nota: "))
  while nota >= 0:
    notas.append(nota)
    nota = int(input("nota: "))
  alumnos[alumno] = notas 

for alumno in alumnos: 
  print(alumno, sum(alumnos[alumno]) / len(alumnos[alumno])) 

# EJERCICIO 13 (funciones)
n1 = int(input('Ingrese un número: '))
n2 = int(input('Ingrese el otro número: '))

def esMultiplo(n1, n2): 
  if (n1%n2) == 0: 
    print(str(n1) + ' es múltiplo de ' + str(n2)) 
  if (n2%n1) == 0: 
    print(str(n2) + ' es múltipo de ' + str(n1))
  else: 
    print('Los números que ingresaste no son múltiplos entre sí')

# EJERCICIO 14 (funciones)
# EJERCICIO 15 (funciones)
socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}

len(socios_activos) #Informar la cantidad de socios que tiene el club.
