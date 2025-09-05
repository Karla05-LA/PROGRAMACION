calificacion = float(input("Ingresa la calificación (0-10): "))

if calificacion < 0 or calificacion > 10:
    print("Error: La calificación debe estar entre 0 y 10")
else:
    if calificacion < 7:
        print("Situación académica: Irregular")
    elif calificacion < 10:  # 7 a 9.999...
        print("Situación académica: Regular")
    else:  # exactamente 10
        print("Situación académica: Excelencia")
