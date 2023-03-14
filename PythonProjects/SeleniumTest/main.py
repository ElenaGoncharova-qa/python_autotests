import requests

token = '39fc18234f3d2d01d92996f6fb164324'

response_add_pokemon = requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, json = {
    "name": "pytest1",
    "photo": "https://dolnikov.ru/pokemons/albums/020.png"
})
print(response_add_pokemon.text) 

response_change_pokemons_name = requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, json = {
    "pokemon_id": 6230,
    "name": "Lenki",
    "photo": ""
})
print(response_change_pokemons_name.text)

response_add_pokemon2pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', headers = {'Content-Type' : 'application/json', 'trainer_token' : token}, json = {
    "pokemon_id": "6233"
})
print(response_add_pokemon2pokeball.text) 