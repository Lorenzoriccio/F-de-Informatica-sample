import re
patern = 'X(ab)*Y' 
def funcion_1(string): 
    print(re.findall(patern, string))   

funcion_1('XbaaaYjXababYqXbabbbbaaYqXffeeY') 
