
import re

texto = input("Ingrese un texto con fechas (formato dd/mm/aaaa): ")

fechas = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', texto)

print("Fechas encontradas:")
print(fechas)
