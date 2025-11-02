
try:
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    carrera = input("Ingresa tu carrera: ")

    with open("perfil.txt", "w") as archivo:
        archivo.write(nombre + "\n")
        archivo.write(edad + "\n")
        archivo.write(carrera + "\n")

    print("Datos guardados correctamente en 'perfil.txt'.")
except Exception as e:
    print("Ocurrió un error al guardar el archivo:", e)
