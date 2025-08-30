a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
c = int(input("ingrese el tercer número: "))

print("Los números ordenados de mayor a menor son:")

# Encontrar el mayor
if a >= b and a >= c:
    mayor = a
    if b >= c:
        medio = b
        menor = c
    else:
        medio = c
        menor = b
elif b >= a and b >= c:
    mayor = b
    if a >= c:
        medio = a
        menor = c
    else:
        medio = c
        menor = a
else:  # c es el mayor
    mayor = c
    if a >= b:
        medio = a
        menor = b
    else:
        medio = b
        menor = a

print(f"{mayor}, {medio}, {menor}")
