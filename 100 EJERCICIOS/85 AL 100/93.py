
import requests

url = "https://numbersapi.com/42?json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Trivia sobre el número 42:")
    print(data["text"])
else:
    print("Error al obtener la información. Código:", response.status_code)
