
import requests

numero = input("Introduce un número: ")
url = f"http://numbersapi.com/{numero}?json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"\n Dato curioso sobre el número {numero}:")
    print(data["text"])
else:
    print(" Error al consultar la API.")
