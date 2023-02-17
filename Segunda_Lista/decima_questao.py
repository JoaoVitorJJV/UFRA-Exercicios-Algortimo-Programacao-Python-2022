# Desenvolva um programa para usando o randint encher duas lista de 10 posições
# com números entre 1 e 20 , ao final seu programa deve informar quais números
# estão presentes em ambas as listas e imprimir o conteúdo das duas listas.

from random import randint

# Listas
lista_1 = []
lista_2 = []

# Loop para preencher as duas listas
for i in range(20):
    # Como só existe um for e ele irá ser executado 20x, ao encher uma listam
    # passaremos para a outra

    numero_aleatorio = randint(1, 20)
    if len(lista_1) == 10:
        lista_2.append(numero_aleatorio)
    else:
        lista_1.append(numero_aleatorio)


# Vamos juntar as duas listas para saber quais números se repetem em ambas
# Utilizando o método extend

lista_3 = []
lista_3.extend(lista_1)
lista_3.extend(lista_2)

numeros_repetidos = []

# Evita que repita os números no print
numeros_repetidos_print = []
# Laço que irá preencher os números das duas listas e verificar quais se repetem
# em ambas
for j in lista_3:
    if j in lista_1 and j in lista_2 and j not in numeros_repetidos_print:
        numeros_repetidos.append(j)
        numeros_repetidos_print.append(j)

print("Lista 1: ", lista_1)
print("Lista 2: ", lista_2)
print("Os seguintes números aparecem nas duas listas: ", numeros_repetidos)


