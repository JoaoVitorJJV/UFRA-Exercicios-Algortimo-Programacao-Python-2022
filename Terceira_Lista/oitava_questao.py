# Um ponto em um plano cartesiano pode ser representado pela sua coordenada X e Y. A
# distancia entre dois pontos no plano cartesiano pode ser calculada pela seguinte
# equação:

# Faça um programa que tenha uma função que receba essas coordenadas e calcule a
# distancia entre esses dois pontos

from math import sqrt

# O programa não recebe entrada, então faremos manualmente

# Coordenadas do plano
x1 = 1
x2 = 2
y1 = 3
y2 = 2

# Função que calcula a distância
def distancia (x1, x2, y1, y2):
    # Cálculo da distância utilizando o método sqrt da biblioteca math
    d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    return d

valor_distancia = distancia(x1, x2, y1, y2)
print(f"A distância das coordenadas: x1 = {x1}, x2 = {x2}, y1 = {y1}, y2 = {y2} é de: {valor_distancia}")