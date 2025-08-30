nombre = input("Ingrese el nombre del vendedor: ")
ventas = float(input("Volumen de ventas en pesos: $"))

print(f"\nVendedor: {nombre}")
print(f"Ventas: ${ventas:,.2f}")

if ventas < 1000:
    print("Situación laboral: Despedido")
elif ventas < 5000:  # 1000 a 4999.99
    print("Situación laboral: En periodo de prueba")
elif ventas < 10000:  # 5000 a 9999.99
    bono = ventas * 0.05
    print(f"Situación laboral: Bono del 5% (${bono:,.2f})")
else:  # 10000 o más
    bono = ventas * 0.10
    print(f"Situación laboral: Bono del 10% (${bono:,.2f})")
