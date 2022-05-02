#POO en clase
class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms 

class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)

class Titan(): 
    def __init__(self, salud): 
        self.salud = salud 
        self.correr = False 

    def salud_actual(self): 
        return self.salud 

    def recibir_ataques(self, cantidad): 
        self.salud -= 1.5 * cantidad 

    def grito(self): 
        return "¡Aaaarrrg!"

    def cuantas_casas(self): 
        return (self.salud * 8 / 100)

    def destruir_casas(self): 
        if (self.cuantas_casas() > 1): 
            if ((self.cuantas_casas() % 1) > 0): 
                self.salud -= (self.cuantas_casas() // 1) * 12.5
            else: 
                self.salud -= (self.cuantas_casas() - 1) * 12.5
        else: 
            print("No puede destruir ninguna casa")
    
    def esta_vivo(self): 
        return (self.salud > 0)

#crear clase Enterprise
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
# DESAFÍO I
'''🧗🏻‍♀️ Desafio I: Ahora te toca a vos:

1. Creá a la golondrina maria con 42 puntos de energía inicial
2. Creá al dragón chimuelo, con 200 dientes y 1000 de energía inicial
3. Definí el método esta_debil, que nos dice si nuestras "aves" tiene menos de 10 puntos de energía (golondrinas) o menos de 50 puntos de energía (dragones)
4. Definí el método esta_feliz, que nos dice si nuestras "aves" tiene más de 500 puntos de energía (sin importar de qué clase sean)
5. Hace a hipo, entrenador de dragones: sabe aceptar a dragones, quienes son sus entrenados y hacerlos entrenar todos los dias, haciendoles dar 20 vueltas en circulos y luego comer su comida favorita hasta saciarse (3 peces)
6. Hacé que hipo pueda entrenar a las golondrinas. ¿Qué comportamiento deberían entender las golondrinas ahora?
7. Definí el método entrenamiento_intensivo, que hace dar vueltas en circulos a sus entrenados hasta que estén débiles.'''
from tkinter import _ExceptionReportingCallback
from aves import pepita, roberta, anastasia, juanita, chimuelo, hipo
class AnimalesAlado: 
    def esta_feliz(self): 
      return self.energia > 500        #EJERICIO 5

class Golondrina(AnimalesAlado):
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms 
  
  def esta_debil(self): 
      return self.energia < 10         #EJERICIO 3a
  
  def esta_feliz(self): 
      return self.energia > 500        #EJERICIO 4a

  def entrenamiento_inetnsivo(self): 
    '''Probá que vuelen en círculos, salvo que estén débiles.'''
    try:  
      self.volar_en_circulos(self)     #EJERCICIO 7a
    except: 
      self.esta_debil(self)

class Dragon(AnimalesAlado):     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

def esta_debil(self): 
    self.energia < 50             #EJERICIO 3b

def esta_feliz(self): 
    return self.energia > 500     #EJERICIO 4b

def entrenamiento_inetnsivo(self): 
  try:  
    self.volar_en_circulos(self)  #EJERCICIO 7b
  except: 
    self.esta_debil(self)

pepita = Golondrina(100)
juanita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
maria = Golondrina(42)            #EJERCICIO 1
chimuelo = Dragon(200, 1000)      #EJERCICIO 2

'''Si las clases hijas heredan de la clase madre tendría todos sus atributos
Eso se hace poniendo en el parentetis de la clase hija (ej. class Golondrina(AnimalesAlado):) 
poniendole el apellido de su hija.'''

# EJERICIO 5
class Entrenador: """El estado del entrenador es el equipo"""
"""¿Qué hay que lograr? Un entrenador tiene un equipo y puede admitir nuevos miembros a su equipo"""
def __init__(self, equipo): 
    self.equipo = equipo 

def el_equipo(self): #el guetter que retorna el estado de un objeto, ES LA FORMA CORRECTA
    return self.equipo

def agregar_animal_alado(self, animal): 
    '''Este método toma un objeto animal alado que tendrá todos los atributos de esa clase'''
    self.equipo.append(animal)     #EJERCICIO 6?

def entrenar_dragon(self, dragon): #sólo self porque contempla ya todo
    for vuelta in range(20): 
        dragon.volar_en_circulos()
    dragon.comer_peces(3)

def entrenar_equipo(self): 
    for dragon in self.equipo: 
        self.entrenar_dragon(dragon) 

from aves import pepita, roberta, anastasia, juanita, chimuelo, hipo
hipo = Entrenador([roberta])

print(hipo) 
print(hipo.equipo)
print(hipo.agregar_animal_alado(chimuelo))
print("energia chimuelo: ", chimuelo.energia)
hipo.entrenar_dragon("energia chimuelo después: ", chimuelo.energia)
print("energia roberta antes: ", roberta.energia) 

# DESAFÍO II
# EJERCICIO 1
# Inluyendo en las clases Dragon y Golondrina la clase concreta (Entrenador)
# EJERCICIO 2
class AvesNoVoladoras: 
  def __init__(self, energia): 
    self.energia = energia 
  
  def correr_en_circulos(self): 
    self.energia -= 25

  def come_alpiste(self):
    return True

# EJERCICIO 3
#3.a. Una Golondrina y AvesNoVoladoras no son polimorficas desde el punto de vista del Entrenador
#3.b. Habría que agregar a la clase Entrenador los AvesNoVoladoras