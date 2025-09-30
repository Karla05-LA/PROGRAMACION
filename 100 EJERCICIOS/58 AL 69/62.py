def calificacion_final(cal1, cal2, cal3):
   promedio_cal = (cal1 + cal2 + cal3) / 3
   if promedio_cal < 6.0:
       return f"{promedio_cal:.2f} - te vas a extra"
   return f"{promedio_cal:.2f}"

#ejemplo
calificaciones = [65,100,75]
Promedio = calificacion_final(*calificaciones)
print(f"El promedio final es {Promedio}")
