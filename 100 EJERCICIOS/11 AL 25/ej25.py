print("Ingresa las coordenadas del primer punto:")
x1 = float(input("x₁ = "))
y1 = float(input("y₁ = "))

print("Ingresa las coordenadas del segundo punto:")
x2 = float(input("x₂ = "))
y2 = float(input("y₂ = "))

# Cálculo de la pendiente (m)
if x1 == x2:
    print("Error: Los puntos tienen la misma coordenada x (recta vertical)")
    print("La pendiente es indefinida y no se puede calcular la ecuación y = mx + b")
else:
    m = (y2 - y1) / (x2 - x1)  # Pendiente
    
    # Cálculo del intercepto (b) usando y = mx + b → b = y - mx
    b = y1 - m * x1
    
    print(f"\n Pendiente (m): {m:.2f}")
    print(f" Intercepto (b): {b:.2f}")
    
    # Formatear la ecuación de manera más legible
    signo_b = "+" if b >= 0 else "-"
    b_abs = abs(b)
    
    print(f"La ecuación de la recta: y = {m:.2f}x {signo_b} {b_abs:.2f}")
    
    # Mostrar ecuación con valores exactos si son enteros
    if m.is_integer() and b.is_integer():
        print(f"           (forma exacta): y = {int(m)}x {signo_b} {int(b_abs)}")
