# Faça um programa que o usuário digite o valor de um ângulo em graus e o programa
# calcule os seguintes valores :
# a. O valor do ângulo em radianos
# b. O seno do ângulo
# c. O cosseno do ângulo
# d. A tangente do angulo

import math

# Entrada -> ângulo em grau

angulo = int(input("Informe um ângulo em graus: "))

# Usaremos funções da biblioteca math para ângulos
angulo_radiano = math.radians(angulo)
seno = math.sin(angulo_radiano)
cos = math.cos(angulo_radiano)
tg = math.tan(angulo_radiano)

# Obs: Valores em radianos
print(f"Ângulo {angulo} em radianos: {angulo_radiano}")
print(f"Seno: {seno}")
print(f"Cosseno: {cos}")
print(f"Tangente: {tg}")