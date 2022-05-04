import re
# def sin_c(string): 
#   return re.findall('aa[^c]*?gg', string)

# sin_c('ttaatatggttaacatgg') 

def funcion_1_2(string): 
    aa_gg = re.findall('aa[^c]*?gg', string)
    print(aa_gg)
funcion_1_2('ttaatatggttaacatgg') 