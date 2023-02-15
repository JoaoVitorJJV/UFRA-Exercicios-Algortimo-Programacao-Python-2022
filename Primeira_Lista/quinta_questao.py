# Faça um algoritmo para, a partir de o diâmetro de um circulo calcular sua área, ou seja
# o usuário deve informar o diâmetro do circulo e seu programa deve calcular a área do
# circulo

from math import pi
# Precisamos do diâmetro como entrada

diametro = int(input("Digite o diâmetro do círculo: "))

# Obtendo o raio de um círculo
raio = diametro / 2

area_circulo = float((raio * raio) * pi)

print(f"A àrea do círculo é igual a: {area_circulo:.2f}")