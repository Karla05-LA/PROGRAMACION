
import re

texto = input("Ingrese un texto: ")

palabras_prohibidas = ["tonto", "feo", "malo", "tonta", "idiota"]

for palabra in palabras_prohibidas:
    patron = re.compile(palabra, re.IGNORECASE)
    texto = patron.sub("*" * len(palabra), texto)

print("Texto censurado:")
print(texto)
