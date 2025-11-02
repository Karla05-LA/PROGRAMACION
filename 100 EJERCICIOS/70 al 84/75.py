
import sys

if len(sys.argv) != 3:
    print("Uso: python lector.py <archivo.txt> <número>")
    sys.exit(1)

nombre_archivo = sys.argv[1]
try:
    n = int(sys.argv[2])
except ValueError:
    print("El segundo argumento debe ser un número entero.")
    sys.exit(1)

try:
    with open(nombre_archivo, 'r', encoding='utf-8') as f:
        for i in range(n):
            linea = f.readline()
            if not linea:
                break
            print(linea.strip())
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no existe.")
