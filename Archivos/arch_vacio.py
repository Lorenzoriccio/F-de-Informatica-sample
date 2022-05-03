import re
str = input("ingrese una cadena de caracteres: ")
patron = "^3"
def funcion_5(str):
    if re.match(patron, str) is not None:
        print("el string comienza con el numero 3")
    else:
        print("el string no emieza con el numero 3")

funcion_5(str) 