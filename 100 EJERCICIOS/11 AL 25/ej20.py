horas_extra = float(input("Ingrese las horas extra trabajadas: "))
horas_normales = 40
salario_normal = horas_normales * 63
salario_extra = horas_extra * 80
salario_total = salario_normal + salario_extra
print(f"Salario semanal total: ${salario_total:.2f}")
print(f" - Horas normales (40): ${salario_normal:.2f}")
print(f" - Horas extra ({horas_extra}): ${salario_extra:.2f}")
