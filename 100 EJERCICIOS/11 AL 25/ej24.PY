capital_inicial = float(input("Capital inicial: $"))
tasa_interes = float(input("Tasa de interés anual (%): "))
periodos = int(input("Número de periodos (años): "))

# Conversión de porcentaje a decimal
tasa_decimal = tasa_interes / 100

# Interés simple
interes_simple = capital_inicial * tasa_decimal * periodos
capital_final_simple = capital_inicial + interes_simple

# Interés compuesto
capital_final_compuesto = capital_inicial * (1 + tasa_decimal) ** periodos
interes_compuesto = capital_final_compuesto - capital_inicial

print(f"\n Capital inicial: ${capital_inicial:,.2f}")
print(f" Tasa de interés: {tasa_interes}% anual")
print(f" Periodos: {periodos} años")

print("INTERÉS SIMPLE:")
print(f"Interés ganado: ${interes_simple:,.2f}")
print(f"Capital final: ${capital_final_simple:,.2f}")

print("INTERÉS COMPUESTO:")
print(f"Interés ganado: ${interes_compuesto:,.2f}")
print(f"Capital final: ${capital_final_compuesto:,.2f}")
