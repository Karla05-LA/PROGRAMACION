
try:
    with open("numeros.txt", "r") as archivo:
        lineas = archivo.readlines()

    numeros = []
    for linea in lineas:
        try:
            numeros.append(float(linea.strip()))
        except ValueError:
            print(f"Línea no válida ignorada: {linea.strip()}")

    if len(numeros) == 0:
        print("No hay números válidos para calcular el promedio.")
    else:
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números es: {promedio:.2f}")

except FileNotFoundError:
    print("El archivo 'numeros.txt' no existe.")
except ZeroDivisionError:
    print("No se puede dividir entre cero (archivo vacío).")
except Exception as e:
    print("Ocurrió un error:", e)
