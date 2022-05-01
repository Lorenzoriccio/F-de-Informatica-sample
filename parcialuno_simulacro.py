# Práctica de repaso! Simulacro!
# EJERCICIO 1
'''Consigna N°1 (RE) Escribir funciones que, dado un String, permitan obtener 
1.a. cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios. 
1.b. la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’. P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.'''

# EJERCICIO 2
'''Consigna N°2 (POO)
Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor. El prototipo de motor tiene 5 cambios (de primera a quinta), 
y soporta hasta 5000 rpm. La velocidad del auto se calcula así: (rpm / 100) * (0.5 + (cambio / 2)). Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40. También nos interesa controlar el 
consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes:

2.a. Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
2.b. Si el motor está en primera, entonces se multiplica por 3.
2.c. Si el motor está en segunda, entonces se multiplica por 2.
Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km. El modelo debe entender estos mensajes:'''

# EJERCICIO 3
'''Consigna N°3 (Manejo de exepciones) Ejecutá el script_misterioso.py y realizá resolvé: 
1. ¿Qué tipo de exepción arroja la corrida del script? 
2. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error 
3. ¿Qué otras excepciones deberias considerar?'''

# EJERCICIO 4
'''Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada Resultado y, 
por otro, que lea todos los archivos con extensión .txt y escriba el contenido de todos en un único archivo llamado 
texto_completo.txt, que tiene que estar dentro de la carpeta Resultado. NO se pueden usar rutas absolutas'''
