# Práctica de repaso! Simulacro!
# EJERCICIO 1
'''Consigna N°1 (RE) Escribir funciones que, dado un String, permitan obtener: 
1.a. cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios. 
1.b. la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.'''

import re
def funcion_1(texto): 
    patron = 'bc9'
    i = len(re.findall(patron, texto)) 
    print(i)                            #1.a.

def funcion_1_2(string): 
    aa_gg = re.findall('aa[^c]*?gg', string)
    print(aa_gg)
funcion_1_2('ttaatatggttaacatgg')       #1.b. 

# EJERCICIO 2
'''Consigna N°2 (POO)
Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor. El prototipo de motor tiene 5 cambios (de primera a quinta), 
y soporta hasta 5000 rpm. La velocidad del auto se calcula así: (rpm / 100) * (0.5 + (cambio / 2)). Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40. También nos interesa controlar el 
consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes:

2.a. Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
2.b. Si el motor está en primera, entonces se multiplica por 3.
2.c. Si el motor está en segunda, entonces se multiplica por 2.
Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km. El modelo debe entender estos mensajes:'''
class Auto: 
    def __init__(self): 
        self.cambios = 0
        self.rpm = 0
        self.consumo = 0.5

    def arrancar(self): 
        if self.rpm >= 500: 
            self.cambios == 1

    def subirCambio(self): 
        self.cambios += 1
    
    def bajarCambio(self): 
        self.cambios -= 1

    def subirRPM(self, cuantos_rpm):
        self.rpm += cuantos_rpm 

    def bajarRPM(self, cuantos_rpm):
        self.rpm -= cuantos_rpm

    def velocidad(self): 
        return (self.rpm/100)*(0.5+(self.cambio /2))
    
    def consumoActualPorKm(self): 
        if self.rpm > 3000: 
            return self.consumo * (self.rpm - 2500) / 500
        if self.cambio == 1: 
            return self.consumo * ((self.rpm - 2500) / 500)* 3 
        if self.cambio == 2: 
            return self.consumo * ((self.rpm - 2500) / 500)* 2

# EJERCICIO 3
'''Consigna N°3 (Manejo de exepciones) Ejecutá el script_misterioso.py y realizá resolvé: 
1. ¿Qué tipo de exepción arroja la corrida del script? 
2. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error 
3. ¿Qué otras excepciones deberias considerar?'''

# 3.1. ZeroDivisionError 
# 3.2. 
def obtener_media(lista): 
    sumatoria = 0
    for valor in lista: 

      sumatoria += valor
    longitud = len(lista)

    try: 
      return sumatoria / longitud 
    except ZeroDivisionError:  
        print('Algo falló! No se puede dividir por 0.')
# 3.3. Se podría verificar que una lista sea una lista, ya que si el parámetro es de otro tipo (no itinerable) el for no va a funcionar. 

# EJERCICIO 4
'''Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada Resultado y, 
por otro, que lea todos los archivos con extensión .txt y escriba el contenido de todos en un único archivo llamado 
texto_completo.txt, que tiene que estar dentro de la carpeta Resultado. NO se pueden usar rutas absolutas'''
# El os.getcwd() es una ruta absoluta y no se pueden usar en este ejercicio
import os, glob 

def unir_txt(): 
    os.mkdir('Resultado')
    lista_txt = glob.glob('*.txt')
    salida = open('Resultado/texto_coompleto.txt', 'a')
    for txt in lista_txt: 
        archivo = open(txt, 'r')
        salida.write(archivo.read())
        archivo.close()
    salida.close()

# Alternativa: 
import os,glob

def unir_txt(): 
    os.mkdir('Resultado')
    lista_txt = glob.glob('*.txt')
    with open('Resultado/texto_completo.txt', 'a') as salida: 
        for txt in lista_txt: 
            with open(txt, 'r') as archivo: 
                salida.write(archivo.read())

# Comentario
import glob
glob.glob('*.py') #es como un ls que busca archivos.py

# Ejercicio 3 integrador
# Escribí un programa que obtenga, a partir de una lista de strings una lista con la longitud de esas strings e imprima la longitud de la lista de strings y los elementos de la lista de longitudes
lista_de_strings = ['hola', 'la paso', 'como el orto']
len(lista_de_strings) #da 3 (ok)

for i in lista_de_strings: 
  long = len(i)
  print('La longitud del string',i, 'es de: ',long) 

# EJERCICIO EXTRA! (objetos)
# Class Enterprise
class Enterprise(): 
    def __init__(self, potencia, coraza):
        self.potencia = 0
        self.coraza = 0
    
    def potencia(self): 
        return self.potencia 

    def coraza(self): 
        return self.coraza 

    def encontrarPilaAtomica(self, potencia): 
        return potencia + 25

    def encontrarEscudo(self, coraza):
        return coraza + 10

    def fortalezaDefensiva(self):
        return self.potencia + self.coraza
        
    def necesitaFortalecerse(self):
        return self.potencia < 20 and self.coraza == 0
        
    def fortalezaOfensiva(self): 
        if self.potencia < 20: 
            return 0
        else: 
            return (self.potencia -20) / 2  

    def recibirAtaque(self, fuerza):
        resto = self.coraza - fuerza
        self.coraza -= fuerza 
        if self.coraza <= 0:
            self.coraza -= resto
        resto2 = self.potencia + resto
        self.potencia += resto 
        if self.potencia <= 0: 
            self.potencia -= resto2 

# class Persona y Estudiante 
class Persona: 
    def __init__(self, energia):
        self.energia = energia 

    def energia_actual(self): 
        return self.energia 

    def dormir(self, horas): 
        if horas <= 8: 
            self.energia += horas*12.5
        else: 
            self.energia = 100
    
    def comer(self): 
        self.energia += 10

    def hacer_ejercicio(self, minutos):
        treinta = minutos//30 
        self.energia -= treinta*25
    
    def energia_actual(self): 
      return self.energia 

class Estudiante(Persona): 
    def estudiar(self, horas):
        self.energia -= 20*horas

    def aprobar(self): 
        return True 

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual()) 