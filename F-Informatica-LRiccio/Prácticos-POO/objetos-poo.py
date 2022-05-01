# POO EJERCICIOS ~ PRÁCTICA
# EJERCICIO 1
'''class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2'''
    # El estado de la clase Perro es el alimento y las caricias
    # La interfaz son: energia(), comer(), acariciar() y estaDebil()

# EJERCICIO 2

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    if self.energia <= 0: 
        return False
    else: 
        self.energia -= 10 + kms 
'''  def volar(self, kms):
    self.energia -= 10 + kms''' #inicial

# EJERCICIO 3
class Notebook():
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio        

    def descuento(self, descuento):
        self.precio -= int(self.precio*(descuento/100))
        print(self.precio)  
    
# EJERCICIO 4
class Contador(): 
    def __init__(self, valor): 
        self.valor = valor

    def dis(self): 
        self.valor -= 1

    def inc(self): 
        self.valor += 1

    def reset(self): 
        self.valor = 0 
    
    def valorActual(self):
        return self.valor

    def valorNuevo(self, valor): 
        self.valor = valor 

contador = Contador(10)
contador.inc()
contador.dis()
contador.reset()
contador.valorActual() #da 12 (ok)
contador.valorNuevo(27) 
contador.dis()
contador.dis()
contador.valorActual() #da 25 (ok)

# EJERCICIO 5
class Contador(): 
    def __init__(self, valor): 
        self.valor = valor
        self.comando = ''

    def dis(self): 
        self.valor -= 1
        self.comando = 'disminuye'

    def inc(self): 
        self.valor += 1
        self.comando = 'incrementa'

    def reset(self): 
        self.valor = 0 
        self.comando = 'reset'
    
    def valorActual(self):
        return self.valor

    def valorNuevo(self, valor): 
        self.valor = valor 
        self.comando = 'actualiza'

    def ultimoComando(self): 
        print(self.comando)

contador = Contador(10)
contador.inc()
contador.ultimoComando() #da incrementa (ok)

# EJERCICIO 6
class Calculadora: 
    def cargar(self, numero): 
        self.numero = numero

    def sumar(self, suma): 
        self.numero += suma

    def multiplicar(self, multiplicador): 
        self.numero *= multiplicador 

    def restar(self, resta): 
        self.numero -= resta
    
    def valorActual(self): 
        return self.numero 

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual() #da 24 (ok)

# EJERCICIO 7
class Gorriones:
    def _init_ (self):
        self.gramos = 0
        self.kms = 0
        self.vuelos = []
        self.comidas = []

    def volar(self, kms):
        self.kms += kms
        self.vuelos.append(kms)

    def comer(self, gramos):
        self.gramos += gramos
        self.comidas.append(gramos)

    def CSS(self):
        if self.gramos <= 0:
            return None
        else:
            return self.kms/self.gramos

    def CSSP(self):
        if self.gramos <= 0:
            return None
        else:
            return int(max(self.vuelos))/int(max(self.comidas))

    def CSSV(self):
        if self.gramos <= 0:
            return None
        else:
            return len(self.vuelos)/len(self.comidas)
    
    def enEquilibrio(self):
        if(self.CSS() > 0,5 and self.CSS() < 2):
            return True
        else:
            return False

lila = Gorriones()
lila.comer(35)
lila.volar(80)
lila.comer(70)
lila.volar(120)
print(lila.CSS())
print(lila.CSSP())
print(lila.CSSV())
print(lila.enEquilibrio())

# Parte 2 de POO
# EJERCICIO 1
'''class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4'''
#1. Sus estados son las caricias y los alimentos 
#2. Sus interfaces son: Gato: energia(), comer(), caricias(), acariciar() y estaDebil() ;Perro: alimento(), pasear() + Gato
#3. Sí, el __init__() y acariciar() coinciden en ambos
#4. Sí, son polimórficas

# EJERCICIO 2
class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms 

    def esta_en_equilibrio(self): 
        return self.energia >= 150 and self.energia <= 300

# EJERCICIO 3

# EJERCICIO 4
class MedioDeTransporte: 
  def __init__(self, combustible): 
    self.combustible = combustible 
    
  def cargar_combustible(self, litros): 
    self.combustible += litros 
    
  def entran_personas(self, personas): 
    return personas <= self.maximo_personas()
    
class Moto(MedioDeTransporte): 
  def recorrer(self, kilometros): 
     self.combustible -= 1*kilometros
      
  def maximo_personas(self): 
    return 2
    
class Auto(MedioDeTransporte): 
  def recorrer(self, kilometros): 
     self.combustible -= 0.5*kilometros
      
  def maximo_personas(self): 
    return 5