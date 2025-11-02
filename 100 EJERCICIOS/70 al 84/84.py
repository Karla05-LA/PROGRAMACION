
try:
    nombre_archivo = input("Ingresa el nombre del archivo: ")

    if len(nombre_archivo) < 5:
        raise ValueError("El nombre del archivo debe tener al menos 5 caracteres.")

    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read(5) 

    numero = int(contenido)
    print(f"Los primeros 5 caracteres convertidos a número son: {numero}")

except FileNotFoundError:
    print("Error: El archivo no existe.")
except ValueError as e:
    print("Error de valor:", e)
except Exception as e:
    print("Ocurrió un error inesperado:", e)
