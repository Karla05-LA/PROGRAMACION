
import re

texto = input("Ingrese una cadena de texto: ")

palabras = re.findall(r'\b[A-Z][a-zA-Z]*\b', texto)

print("Palabras que comienzan con mayúscula:")
print(palabras)
