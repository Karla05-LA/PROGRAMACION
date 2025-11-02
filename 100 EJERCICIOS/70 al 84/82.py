
try:
    with open("a.txt", "r") as archivo_a:
        contenido_a = archivo_a.read()
    with open("b.txt", "r") as archivo_b:
        contenido_b = archivo_b.read()

    with open("combinado.txt", "w") as combinado:
        combinado.write(contenido_a + "\n" + contenido_b)

    print("Archivos combinados correctamente en 'combinado.txt'.")
except FileNotFoundError as e:
    print("Uno de los archivos no existe:", e)
except Exception as e:
    print("Ocurrió un error al combinar los archivos:", e)
