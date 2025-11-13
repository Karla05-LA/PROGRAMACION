
import requests
import json

url = "http://numbersapi.com/random/trivia?json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    with open("respuesta.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ Respuesta guardada en 'respuesta.json'")
else:
    print("❌ Error al hacer la petición:", response.status_code)
