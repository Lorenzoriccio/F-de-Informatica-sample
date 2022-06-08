#url a gatos: https://http.cat/

# Apuntes de clase
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
r1 = requests.get('https://macowins-server.herokuapp.com/prendas/20')
print(r1.json()) 

# Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
# Quiero ver si tiene 400
r2 = requests.get('https://macowins-server.herokuapp.com/prendas/400') 
print(r2)
# Tira error 404 porque no pudo encontrar y traerme el recurso, eso se lo denomina Status Code 

# Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
r3 = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(r3.headers) 
print(r3.status_code) 
# El Status Code es 200

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
r4 = requests.get('https://macowins-server.herokuapp.com/prindas/1')
print(r4) # <Response [404]>

# Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior
r5 = requests.get('https://macowins-server.herokuapp.com/ventas')
r6 = requests.get('https://macowins-server.herokuapp.com/ventas/2')
print(r5) # <Response [200]>
print(r6) # <Response [200]>

# Desafío VI: Obtené las remeras.
pedido_remeras = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
print(pedido_remeras.json())

# Desafío VII: Obtené las remeras XS
pedido_remeras_xs = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
print(pedido_remeras_xs.json()) 

# Desafío VIII: decí usando tus palabras qué significa la URI de este ejemplo cerebral 😛.
'''Las URI son un formato estandarizado de strings'''

# Desafío IX: ¿a través de qué IP accedés a google desde tu computadora?
'''Las IP son el identificatorio de cada computadora. Una dirección IP es una dirección única que identifica 
a un dispositivo en Internet o en una red local. IP significa “protocolo de Internet”, que es el conjunto de 
reglas que rigen el formato de los datos enviados a través de Internet o la red local.
Cuando accedes a Google estás usando 8.8.8.8. o 8.8.4.4¿?'''

# Desafío X: ¿Qué devolverá la página principal (home) de nuestro sitio? Averiguá el Content-Type de /home
print(r1.headers)
'''{'Server': 'Cowboy', 'Connection': 'keep-alive', 'X-Powered-By': 'Express', 'Expires': '-1', 'Content-Type': 'application/json; 
charset=utf-8', 'Content-Length': '49', 'Etag': 'W/"31-OlDFK7SS8oUCKcn/LZE2poJFDDo"', 'Vary': 'Accept-Encoding', 'Date': 'Mon, 06 Jun 2022 12:04:12 GMT', 'Via': '1.1 vegur'}'''

# Desafío XI: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, si el contenido se transfiere encriptado, y la fecha de expieración del contenido.
# Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo
# Desafío: Nos quedaron prendas con ids que no nos sirven; ¡borralas!
# Desafío XIII: Creá una venta.
# Desafío XIV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. ¿Qué sucede?
# Desafío XV: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
# Desafío XVI: si no se organizan de forma REST, ¿cómo se organizan sus rutas?
# Desafío XVII: ¿En dónde está desplegado QMP? ¿Podés averiguarlo las cabeceras HTTP y/o la URL?


# Guía teórica de Maquetado Web
# Desafio I: Buscá qué otras etiquetas existen y para qué sirven
'''Ejemplo de algunas etiquetas más:
<section> = representa una sección genérica de un documento
<div> = sirve para crear secciones o agrupar contenidos
<span> = sirve para aplicar estilo al texto o agrupar elementos en línea
<ul> = para hacer listas  '''

# Desafio II :Creá un archivo de texto con la herramienta que tengamos a mano (visual code, editor de texto, bloc de notas,etc) y lo guardamos con el nombre “mi_pagina” con extensión “.html” : “mi_cv.html”
# Desafio IV: Buscá qué otras etiquetas semánticas existen
# Desafio V: Buscá qué otros atributos existen y dale estilo al documento HTML creado en el Desafío II
# Desafío VI: Investigá en la documentación de ipywidgets qué otros elementos HTML podés mostrar y probalos