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
juanita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)

# HECHO EN CLASE 18/4/22
from aves import pepita, juanita, roberta
print(juanita)
print(pepita)  

'''son dif objetos con dif identidades pero de la = clase 
tanto los dragones como las golondrinas comparten parte de su interfaz, no todo (POLIMORFISMO)'''