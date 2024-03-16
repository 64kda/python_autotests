import requests
Host = "https://api.pokemonbattle.me/v2"
Trainer_ID = "2022"
Trainer_token = "890b930ee2d8311051d0a20a47216f15"
HEADERS = {"Content-Type" :"application/json",
           "trainer_token" :Trainer_token  }

body = {
    "name": "generate",
    "photo": "generate"
}

response = requests.post(url= f'{Host}/pokemons', headers = HEADERS, json = body)

print(response.text)



body = {
    "pokemon_id": "14124",
    "name": "БашмаKK",
}

response = requests.patch(url= f'{Host}/pokemons', headers = HEADERS, json = body)

print(response.text)


body = {
    "pokemon_id": "14124"
}

response = requests.post(url= f'{Host}/trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)