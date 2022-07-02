#url a gatos: https://http.cat/

# Apuntes de clase
import requests 
prendas = requests.get('https://macowins-server.herokuapp.com/prendas')
print(prendas) 
# Si nos da una respuesta, el canal de comunicación funciona 
print(prendas.json()) 
# Json es un diccionario python 
# Json es el formato en el cual los servidores devuelven la información al cliente 
print(len(prendas.json()))  
# Averiguamos la cantidad de prendas (recursos) que tiene
print(prendas.headers) 
# Headers me dice toda la metadata (la información del pedido)

# Guía teórica de HTTP & REST
# Desafío I: Hacé otro pedido para traer a la prenda 20. Deberías obtener el siguiente resultado:
r20 = requests.get('https://macowins-server.herokuapp.com/prendas/20')
print(r20.json()) 

# Desafío II: ¡averigualo! Hacé requests.get('https://macowins-server.herokuapp.com/prendas/400') y observá qué sucede.
# Quiero ver si tiene 400
r400 = requests.get('https://macowins-server.herokuapp.com/prendas/400') 
print(r400)
# Tira error 404 porque no pudo encontrar y traerme el recurso, eso se lo denomina Status Code 

# Desafío III: contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
r1 = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(r1.headers) 
print(r1.status_code) 
# El Status Code es 200

# Desafío IV: ¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!
r1 = requests.get('https://macowins-server.herokuapp.com/prindas/1')
print(r1) # <Response [404]>

# Desafío V: hacé requests.get('https://macowins-server.herokuapp.com/ventas') y requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior
ventas = requests.get('https://macowins-server.herokuapp.com/ventas')
v2 = requests.get('https://macowins-server.herokuapp.com/ventas/2')
print(v2) # <Response [200]>
print(v2) # <Response [200]>

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
charset=utf-8', 'Content-Length': '49', 'Etag': 'W/"31-OlDFK7SS8oU(CKcn/LZE2poJFDDo"', 'Vary': 'Accept-Encoding', 'Date': 'Mon, 06 Jun 2022 12:04:12 GMT', 'Via': '1.1 vegur'}'''

# Desafío XI: consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, si el contenido se transfiere encriptado, y la fecha de expieración del contenido.
ml = requests.get('https://www.mercadolibre.com.ar/#from=homecom')
print(ml.headers)
'''Expires=Thu, 08 Jun 2023 16:45:58 GMT;'content-encoding': 'gzip;'Server': 'Tengine' '''
ps = requests.get('https://www.playstation.com/es-ar/')
print(ps.headers)
''''Expires': 'Wed, 08 Jun 2022 16:41:12 GMT';'Content-Encoding': 'gzip';'Server': 'Apache' '''
netflix = requests.get('https://www.netflix.com/ar/login')
print(netflix.headers) 
''''Expires=Thu, 8 Jun 2023 16:36:22 GMT;'Content-Encoding': 'gzip';'Server': 'nq_website_nonmember-prod-release 84ee2c12-8b52-4d46-baa4-9378ee9e7b0d' '''
yt = requests.get('https://www.youtube.com/')
print(yt.headers)
''' 'Expires=Mon, 05-Dec-2022 16:28:03 GMT;Content-Encoding': 'gzip';'Server': 'ESF' '''

# Desafío XII: ¿qué código de estado devuelve cuando un recurso es creado? Averigualo
import json, requests
r = requests.get('https://macowins-server.herokuapp.com/prendas')
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=json.dumps(data), headers=headers)
print(r.status_code)
print(r.json()) 
#haciendo POST sobre la ruta de /prendas creamos una prenda, sin especificar un id, dado que se generará solo. 
#de todas formas, si quisieramos podríamos haberlo especificado agregándolo en el cuerpo.
'''
201
{'tipo': 'chomba', 'talle': 'XS', 'id': 'xX_hbCG'} '''

# Desafío: Nos quedaron prendas con ids que no nos sirven; ¡borralas!
# Desafío XIII: Creá una venta.

# Desafío XIV: Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. ¿Qué sucede? 
data = {'id':21, 'tipo': 'chomba', 'talle': 'XL'}
post = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)  
print(post.status_code)

# Desafío XV: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
'''Respuestas: Infobae, Pagina12, La Nacion - UNQ, UCEMA - Github'''

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
# Listo
# Desafio IV: Buscá qué otras etiquetas semánticas existen
'''Otras etiquetas semánticas: 
<aside> = marca un trozo de contenido que está relacionado con el contenido de la página web, pero que no es parte del mismo (ex. glosario)
<main> = representa el contenido predominante de la página.'''
# Desafio V: Buscá qué otros atributos existen y dale estilo al documento HTML creado en el Desafío II
# Listo
# Desafío VI: Investigá en la documentación de ipywidgets qué otros elementos HTML podés mostrar y probalos

'''
Requisitos para el exámen: 
url: http://miapp.com/...
http: protocolo
miapp.com: dominio 
... : ruta 

'''