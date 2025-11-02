
import pandas as pd

data = {'Producto': ['bimbo', 'alpura', 'suavitel', 'pachoncito'],
    'Precio': [45, 27, 72, 103],
    'Cantidad': [400, 350, 273, 321]}

df = pd.DataFrame(data)
print("\n=== DataFrame ===")
print(df)

print("\n=== Estadísticas ===")
print(df.describe())
