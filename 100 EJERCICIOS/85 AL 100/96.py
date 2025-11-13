
import requests

url = "https://pokeapi.co/api/v2/pokemon/25"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    nombre = data["name"].capitalize()
    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    
    print("Nombre del Pokémon:", nombre)
    print("Tipos:", ", ".join(tipos))
else:
    print("Error al obtener datos del Pokémon. Código:", response.status_code)
