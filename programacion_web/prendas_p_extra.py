import requests 
prendas = requests.get('https://macowins-server.herokuapp.com/prendas') 
print(len(prendas.json())) #21
print(prendas.status_code) #200 (funciona)
print(prendas.headers) #'Content-Type': 'application/json

prenda5 = requests.get('https://macowins-server.herokuapp.com/prendas/5') 
print(prenda5.json()) #{'id': 5, 'tipo': 'pantalon', 'talle': 39}

path = (r'C:\Users\Usuario\Desktop\UNIVERSIDAD\fund_info\F-de-Informatica-sample\programacion_web\prenda5.txt')
with open(path, 'w') as f: 
    f.write(str(prenda5))   