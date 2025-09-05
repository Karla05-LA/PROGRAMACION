total_preguntas = int(input("Ingrese el total de preguntas del examen: "))
preguntas_correctas = int(input("Ingrese las preguntas contestadas correctamente: "))

if total_preguntas <= 0:
    print("Error: El total de preguntas debe ser mayor a 0")
else:
    calificacion = (preguntas_correctas / total_preguntas) * 10
    print(f"Calificación final: {calificacion:.2f}/10")
    
    # Mensaje adicional según calificación
    if calificacion >= 7:
        print("¡Aprobado!")
    else:
        print("Reprobado")
