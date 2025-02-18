import resquests
import json

print('---- GitHub Users ----')

username = input('Qual o nome do usuário?')

url = f'https://api.github.com/user/{username}'

response = requests.get(url) # pegar os dados da minha requisicao
data = response.json() # transforma os dados da minha requisicao para o formato json = dicionari

if response == 200:
    print(f'Nome Completo: {data["name"]}')
    print(f'Localização: {data["location"]}')
else: 
    print('Não foi possível encontrar o usuário!!')