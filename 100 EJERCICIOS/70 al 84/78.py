
try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        num_lineas = len(lineas)
        num_palabras = 0
        num_caracteres = 0

        for linea in lineas:
            palabras = linea.split()
            num_palabras += len(palabras)
            num_caracteres += len(linea)

        print(f"Total de líneas: {num_lineas}")
        print(f"Total de palabras: {num_palabras}")
        print(f"Total de caracteres: {num_caracteres}")

except FileNotFoundError:
    print("Error: El archivo 'datos.txt' no existe.")
