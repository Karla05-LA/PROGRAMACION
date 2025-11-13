
import re

texto = input("Ingrese un párrafo: ")

oraciones = re.split(r'[.!?]', texto)

print("Oraciones encontradas:")
for oracion in oraciones:
    if oracion.strip():  # Ignorar líneas vacías
        print(oracion.strip())
