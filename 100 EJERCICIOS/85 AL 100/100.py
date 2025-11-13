
import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Primeros 5 Pokémon:")
    for pokemon in data["results"]:
        print("-", pokemon["name"].capitalize())
else:
    print("Error al consultar la PokéAPI.")
