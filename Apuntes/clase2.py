# PARTE 2
# HTTPS & REST
# Apuntes clase 

import requests 
pedido = requests.get('https://macowins-server.herokuapp.com/prendas')
print(pedido) 
# Si nos da una respuesta, el canal de comunicación funciona 
print(pedido.json()) 
# Json es un diccionario python 
# Json es el formato en el cual los servidores devuelven la información al cliente 
print(len(pedido.json()))  
# Averiguamos la cantidad de prendas (recursos) que tiene
print(pedido.headers) 
# Headers me dice toda la metadata (la información del pedido)

# Guía teórica de HTTP & REST
# Desafío I: Hacé otro pedido para traer a la prenda 20. Deberías obtener el siguiente resultado:
r = requests.get('https://macowins-server.herokuapp.com/prendas/20')
print(r.json()) 

# Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
# Quiero ver si tiene 400
r = requests.get('https://macowins-server.herokuapp.com/prendas/400') 
print(r)
# Tira error 404 porque no pudo encontrar y traerme el recurso, eso se lo denomina Status Code 

# Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(r.headers) 
print(r.status_code) 
# El Status Code es 200

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
# Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior
# Desafío VI: Obtené las remeras.
# Desafío VII: Obtené las remeras XS