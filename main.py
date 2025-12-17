import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "YOUR_TOKEN_HERE"
HEADER = {"Content-Type": "application/json",
          "trainer_token": TOKEN}
BODY_POKE_CREATE = {
    "name": 'Печенька',
    "photo_id": 27}
BODY_POKE_CATCH = {
    "pokemon_id": "YOUR_ID_HERE"}

response = requests.post(url = f"{URL}/pokemons", headers = HEADER, json = BODY_POKE_CREATE)
print(response)

response = requests.post(url = f"{URL}/trainers/add_pokeball", headers = HEADER, json = BODY_POKE_CATCH)

print(response.text)
