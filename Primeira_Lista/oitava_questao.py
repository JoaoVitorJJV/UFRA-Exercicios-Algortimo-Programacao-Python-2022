# Faça um algoritmo para ler uma temperatura em célsius e converter essa temperatura
# para Fahrenheit.

c = float(input("Informe a temperatura em graus Celsius: "))

# Fórmula de conversão c x 9 / 5 + 32
f = c * (9/5) + 32

print(f"Temperatura em {c:.1f}°C\nTemperatura em {f:.1f}°F")