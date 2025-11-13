
import requests
import json

palabra = input("Introduce una palabra en inglés: ").strip()
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{palabra}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    definicion = data[0]["meanings"][0]["definitions"][0]["definition"]
    print(f"\n Definición de '{palabra}': {definicion}\n")

    with open("definicion.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
else:
    print("No se encontró la palabra o error en la petición.")
