# Consigna 1
import re
def entre_X_Y_con_ab(string): 
    patron = 'X(.*?ab.*?)Y'
    return re.findall(patron, string)

# Consigna 2
import glob, re
def filtrar(archivo): 
    lista_txt = glob.glob('.txt')

    with open(archivo, 'a') as arch: 
        for f in lista_txt: 
            with open(f, 'r') as archivo_secreto: 
                texto = archivo_secreto.read()
                lista = re.findall('[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]+@[a-zA-Z]{2,9}(\.[a-zA-z]{2,4})', texto)
                for email in lista: 
                    arch.write(email + ',')


