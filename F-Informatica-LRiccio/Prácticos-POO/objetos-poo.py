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
'''
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
            return (self.potencia -20) / 2   '''

#no me sale la de recibirAtaque aiuda 
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
'''  def volar(self, kms):
    self.energia -= 10 + kms''' #inicial

'''
def volar(self, kms):
    if self.energia <= 0: 
        return False
    else: 
        self-energia -= 10 + kms''' 

class Notebook():
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio        #cuando es estado se le pone return, cuando no, NO

    def descuento(self, descuento):
        self.precio -= descuento*(descuento/100)
        print("El valor final es: ")
    
class Contador(): 
    def __init__(self, valor): 
        self.valor = 0

    def contadorNeg(self): 
        self.valor -= 1
    