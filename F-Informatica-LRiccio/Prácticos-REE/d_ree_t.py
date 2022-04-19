# 🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?
# 🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?
# 🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?
import re
texto = "absurdo es estar abajo en la terraza"
patron = "ab"
re.findall(patron , texto)