# DESAFÍO I
from aves import pepita, juanita, roberta
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
    self.energia < 50           #EJERICIO 3b

def esta_feliz(self): 
    return self.energia > 500   #EJERICIO 4b

pepita = Golondrina(100)
juanita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 1000)    # EJERCICIO 2

'''Si las clases hijas heredan de la clase madre tendría todos sus atributos
Eso se hace poniendo en el parentetis de la clase hija (ej. class Golondrina(AnimalesAlado):) 
poniendole el apellido de su hija.'''

# EJERICIO 5
class Entrenador: """El estado del entrenador es el equipo"""
"""¿Qué hay que lograr? Un entrenador tiene un equipo y puede admitir nuevos miembros a su equipo"""
def __init__(self, equipo): 
    self.equipo = equipo 

def equipo(self): 
    return self.equipo

def agregar_animal_alado(self, animal): 
    '''Este método toma un objeto animal alado que tendrá todos los atributos de esa clase'''
    self.equipo.append(animal)

from aves import pepita, roberta, anastasia, juanita, chimuelo
hipo = Entrenador([roberta])
'''Entrenador: 
print(hipo)
print()    '''