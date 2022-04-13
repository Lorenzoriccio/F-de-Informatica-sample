# DESAFÍO I
"""
Paso 1) Seleccionar el mate
Paso 2) Buscar el yerbero
Paso 3) Verificar si el mate está vacío:
    Momento decisivo:
        Paso 4) Si el mate está vacío, llenarlo con la yerba del yerbero.
        Paso 5) Si el mate está lleno:
            Paso 6) Buscar la meceta
            Paso 7) Vaciarlo en la maceta
            Paso 8) Llenarlo con la yerba del yerbero.
Paso 9) Verificar si el mate tiene agua
Paso 10) Buscar una pava
Paso 11) Calentar agua en la pava
Paso 12) Verificar si el mate tiene agua: 
    Momento decisivo: 
        Paso 13) Si el mate no tiene agua, llenarlo con agua de la pava 
        Paso 14) Si el mate tiene agua, tomar y repetir el paso anterior """

"""    
mate = mate seleccionado
yerbero = lata de yerba
maceta = maceta con cactus del balcón 

if mate está vacio:
    llenar mate con yerba del yerbero
de lo contrario:
    vaciar mate en maceta
    llenar mate con yerba del yerbero
    
if mate no tiene agua: 
    calentar con agua de la pava
de lo contrario: 
    romar mate y repetir paso anterior """

# DESAFÍO II
"""prompt de ambas: Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information._ 

El prompt de ambas es el mismo. 
El lenguaje que "entiende" la terminal de Visual Code es python."""

# DESAFÍO III
"""saludo = "Hola mundo"_ al invocarlo no devuelve nada ya que se está creando una nueva variable pero... 
Al correr `len(saludo)` te devuelve la cantidad de caracteres en el saludo= "Hola mundo". 
Luego `saludo.upper()` te devuelve el string en mayúsculas, mientras que `saludo.lower()` en minúsculas. 
En `saludo.count("o")` te dice la cantidad de veces que la letra "o" se repite en el saludo."""

# DESAFÍO IV
#Al probar `saludo.replace("mundo", "terricolas")` reemplaza "mundo" por "terricolas"

# DESAFÍO VI
def termos_por_ronda(personas): 
    return (personas * 30) / 1000

# DESAFÍO VII
def vaquita(costos, comensales):
    return costos / comensales

# DESAFÍO VIII
termo = 1000
def calcular_cantidad_de_agua(personas): 
    if termo >= (personas * 30): 
        return personas * 30
    else:
        return "vas a necesitar más de un térmo"

# DESAFÍO IX
# hecho como ejemplo en donde te devuelve cada pedido 
def empanadas_por_gusto():
    for i in lista_comensales:
        print(pedido[i])

gustos = {"no_veggie": 0, "veggie": 0} # iniciar un contador para cada gusto
pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "vegetarianas"}
lista_comensales = ["Ana", "Paul", "Luz"]
def empanadas_por_gusto(): 
    for comensal in lista_comensales: 
        gustos[pedido[comensal]] += 1 # del gusto que sea sumame 1
    # si usas if lo tenés que hacer para cada gusto y no estaría del todo ok 
    
print(gustos)
