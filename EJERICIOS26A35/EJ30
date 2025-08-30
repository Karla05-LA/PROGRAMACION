precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
egresos = float(input("Total de egresos de la empresa: "))

ingresos = precio_unitario * cantidad_vendida

print(f"\nIngresos totales: ${ingresos:,.2f}")
print(f"Egresos totales: ${egresos:,.2f}")

if ingresos > egresos:
    ganancia = ingresos - egresos
    print(f" La empresa genera ganancias: ${ganancia:,.2f}")
elif ingresos < egresos:
    perdida = egresos - ingresos
    print(f" La empresa está en pérdidas: ${perdida:,.2f}")
else:
    print(" La empresa está en punto de equilibrio")
