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

class Notebook():
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio        

    def descuento(self, descuento):
        self.precio -= descuento*(descuento/100)
        print("El valor final es: ") 
    
class Contador(): 
    def __init__(self, valor): 
        self.valor = 0

    def dis(self): 
        self.valor -= 1

    def inc(self, valor): 
        self.valor += 1

    def reset(self, valor): 
        self.valor = 0 
    
    def valorActual(self, valor):
        self.valor = 0 

    def valorNuevo(self, valor): 
        self.valor = valor 

contador = Contador(10)
contador.inc()
contador.dis()
contador.reset()
contador.valorActual()
contador.valorNuevo(27) 
