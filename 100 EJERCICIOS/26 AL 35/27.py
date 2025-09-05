print("¿Qué desea calcular?")
print("1. Área")
print("2. Perímetro")
opcion = input("Elige una opción (1 o 2): ")

lado = float(input("Ingresa la longitud del lado del cuadrado (positivo): "))

if lado <= 0:
    print("Error: El lado debe ser un número positivo")
else:
    if opcion == "1":
        area = lado * lado
        print(f"El área del cuadrado es: {area:.2f}")
    elif opcion == "2":
        perimetro = 4 * lado
        print(f"El perímetro del cuadrado es: {perimetro:.2f}")
    else:
        print("Error: Opción no válida. Debe ser 1 o 2")
