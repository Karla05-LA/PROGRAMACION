
try:
    with open("entrada.txt", "r", encoding="utf-8") as archivo:
        for num, linea in enumerate(archivo, start=1):
            print(f"Línea {num}: {linea.strip()}")
except FileNotFoundError:
    print("Error: El archivo 'entrada.txt' no existe.")
