# Faça um programa para encher uma lista de 100 posições com números entre 1 e
# 20, para isso use a função randint para gerar números aleatórios dentro desse
# intervalo, depois que a lista estiver cheia imprima quantas vezes cada numero
# aparece na lista, veja a figura abaixo para ver como usar o randint e como deve
# ficar a saída do programa .

from random import randint

# lista com os números aleatórios
numeros = []

# Loop que adiciona os números aleatórios a lista
for i in range(100):
    numero_aleatorio = randint(1, 20)

    # Função que adiciona itens em uma lista "append"
    numeros.append(numero_aleatorio)

# String onde irá conter os números aleatórios - quantidade de vezes que se repete
# exemplo: 1 - 6 -> Nesse exemplo, o número 1 se repete 6 vezes na lista de números
str_repeticoes = ""

# lista com números repetidos
numeros_repetidos = []

# Primeiro loop que irá percorrer todo a lista de números
for j in numeros:
    # Variável que contabiliza quantas repetições o número j tem
    repeticoes = 0

    # Segundo loop que também irá percorrer a lista de números, mas
    # irá comparar com o primeiro loop, acima dele, passando para
    # ver se o número é repetido
    for k in numeros:
        # Verifica se o número é repetido
        if j == k:
            repeticoes += 1

    # Essa verificação é para o retorno da str_repeticoes, onde ele irá evitar
    # repetir o mesmo número
    if j not in numeros_repetidos:
        str_repeticoes += f"{j} - {repeticoes}\n"
        numeros_repetidos.append(j)

print(numeros)
print(str_repeticoes)

