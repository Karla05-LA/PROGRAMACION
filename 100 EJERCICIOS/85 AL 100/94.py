
import requests

url = "https://api.github.com"

response = requests.get(url)

print("Código de estado:", response.status_code)

if response.status_code == 200:
    print("Todo bien")
else:
    print("Error")
