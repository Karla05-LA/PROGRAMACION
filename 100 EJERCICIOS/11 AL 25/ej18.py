num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número:"))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir por cero"
potenciacion = num1 ** num2
raiz_cuadrada = num1 ** 0.5
modulo = num1 % num2 if num2 != 0 else "No se puede calcular módulo con cero"

print(f"La suma de los números es: {suma}")
print(f"La resta de los números es: {resta}")
print(f"La multiplicación: {multiplicacion}")
print(f"La división: {division}")
print(f"La potenciación: {potenciacion}")
print(f"La raíz cuadrada del primer número es: {raiz_cuadrada}")
print(f"El módulo: {modulo}")
