import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ТОКЕН_ТРЕНЕРА'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Max",
    "photo_id": 5
}

body_change_name = {
    "pokemon_id": "163048",
    "name": "MaxoN",
    "photo_id": 5
}

body_add_pokeball = {
    "pokemon_id": "163048"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''message = response_create.json()['message']
print(message)'''

'''response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)'''

'''message = response_change_name.json()['message']
print(message)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)