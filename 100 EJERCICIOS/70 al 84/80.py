
try:
    with open("origen.txt", "r") as archivo_origen:
        contenido = archivo_origen.read()

    with open("copia.txt", "w") as archivo_destino:
        archivo_destino.write(contenido)

    print("El archivo se copió correctamente a 'copia.txt'.")
except FileNotFoundError:
    print("El archivo 'origen.txt' no existe.")
except Exception as e:
    print("Ocurrió un error al copiar el archivo:", e)
