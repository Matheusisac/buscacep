import requests
import json

cep = input("digite o seu cep\n")
cep = cep.replace("-","").replace(".", "").replace(" ","")
#Leitura dos dados e armazenamento dos dados em listas
request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
todos = json.loads(request.content)
uf = todos["uf"]
logradouro = todos["logradouro"]
bairro = todos["bairro"]
cidade = todos['localidade']
ddd = todos["ddd"]
complemento = todos["complemento"]

print(f"""Informações sobre o cep {cep}:
UF: {uf}
DDD: {ddd}
cidade: {cidade}
bairro: {bairro}
logradouro: {logradouro}
complemento: {complemento}
""")
