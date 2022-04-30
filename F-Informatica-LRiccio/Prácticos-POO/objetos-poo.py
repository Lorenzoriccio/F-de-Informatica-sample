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