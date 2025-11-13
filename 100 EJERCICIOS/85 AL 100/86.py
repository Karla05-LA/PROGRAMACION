
import re

correo = input("Ingrese un correo electrónico: ")

patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(patron, correo):
    print("Válido")
else:
    print("Inválido")
