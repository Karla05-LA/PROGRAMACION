def promedio (lista):
    if not (lista):
        return 0
    suma = sum(lista)
    cantidad = len(lista)
    return suma / cantidad
   
#Ejemplo
calificaciones = [97,97]
resultado = promedio(calificaciones)
print("El promedio de las calificaciones es: ", resultado)



