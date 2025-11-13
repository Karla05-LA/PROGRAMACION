
import re

texto = input("Ingrese un texto con direcciones de correo: ")

usuarios = re.findall(r'([\w\.-]+)@[\w\.-]+\.\w+', texto)

print("Nombres de usuario encontrados:")
print(usuarios)
