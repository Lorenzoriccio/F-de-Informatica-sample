import json, requests
prendas = requests.get('https://macowins-server.herokuapp.com/prendas')
data = {'id': 21}
prendas = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
prendas = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
print(prendas.status_code)
print(prendas.json()) 