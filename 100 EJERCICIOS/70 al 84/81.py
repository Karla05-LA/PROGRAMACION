try:
    frase = input("Escribe una frase para agregar al archivo: ")

    with open("registro.txt", "a") as archivo:
        archivo.write(frase + "\n")

    print("Frase agregada correctamente a 'registro.txt'.")
except Exception as e:
    print("Ocurrió un error al escribir en el archivo:", e)
