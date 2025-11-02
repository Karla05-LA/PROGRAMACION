
import os

carpeta = input("Ingresa el nombre de la carpeta: ")

if os.path.isdir(carpeta):
    archivos_csv = [f for f in os.listdir(carpeta) if f.endswith('.csv')]
    archivos_csv.sort()
    
    print("\nArchivos .csv encontrados:")
    for archivo in archivos_csv:
        print(archivo)
else:
    print("La carpeta no existe.")
