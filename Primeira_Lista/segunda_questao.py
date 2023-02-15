# Faça um programa para calcular o volume de um cone, o volume de um cilindro e o
# volume de uma esfera , ao final diga qual tem maior volume e qual tem menor volume.
# Para um melhor resultado use a constante pi presente no modulo math do python, Veja
# abaixo o exemplo do uso da constante pi.

from math import pi

print("Volumes Àreas Circulares - 2\n")
# Vamos deixar o usuário escolher o que ele quer calcular primeiro
# após, faremos os cálculos de acordo com sua escolha

escolha = str(input("Qual volume você deseja calcular primeiro?: (cone, cilindro, esfera)"))

# Condicional para vermos o que o usuário deseja calcular
if escolha == "cone":
    # Precisaremos da altura e raio do cone
    raio = int(input("Informe o raio do cone: "))
    altura = int(input("Informe a Altura do cone: "))

    # Fórmula volume cone -> Ab x h / 3
    # Fórmula da àrea da base -> pi x r x r ou pi x r²

    area_base_cone = float(pi * (raio * raio))

    volume_cone = float(area_base_cone * altura / 3)

    # Saída
    print(f"O Volume do cone é de: {volume_cone:.2f}")
elif escolha == "cilindro":
    # Precisamos do raio e altura do cilindro
    raio_cilindro = int(input("Informe o raio do cilindro: "))
    altura_cilindro = int(input("Informe a altura do cilindro: "))

    # Fórmula do volume cilintro -> Ab x h
    area_base_cilindro = float(pi * (raio_cilindro ** 2))

    volume_cilindro = float(area_base_cilindro * altura_cilindro)

    print(f"O volume do cilindro é de: {volume_cilindro:.2f}")

elif escolha == "esfera":
   # Precisamos somente do raio
   raio_esfera = int(input("Informe o raio da esfera: "))

   # Fórmula volume esfera -> 4 x pi x r³ / 3
   volume_esfera = float((4 * pi * raio_esfera ** 3) / 3)

   print(f"Volume esfera: {volume_esfera:.2f}")