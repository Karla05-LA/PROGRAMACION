
import re

texto = input("Ingrese una cadena de texto: ")

numeros = re.findall(r'\d+(?:\.\d+)?', texto)

numeros = [float(num) for num in numeros]

print("Números encontrados:", numeros)
