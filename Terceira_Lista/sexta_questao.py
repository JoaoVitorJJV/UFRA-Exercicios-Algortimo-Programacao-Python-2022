# Aproveitando a função anterior, crie uma função que receba um número inteiro como
# parâmetro e imprima na tela o próximo numero primo maior que ele

# Utilizaremos a mesma função, mas com algumas adaptações novamente
def verificacao_primo(n):
    if n > 1:
        # Usaremos o laço for para verificar se é primo
        multiplos = 0

        for i in range(2, n):
            if n % i == 0:
                multiplos += 1

        # Se houver um múltiplo além de 1 e o próprio número, o número não é primo
        if multiplos == 0:
            return True
        else:
            return False
    else:
        return False

# Entrada -> qualquer número inteiro

n = int(input("Digite um número inteiro: "))

# Loop para descobrirmos os próximos números inteiros
incremento = n

while True:
    # Utilizando a função acima, iremos verificar todos os números primos a partir
    # do número de entrada
    valor = verificacao_primo(incremento)

    # Se o número for primo, ele irá entrar nesse if
    if valor:
        # Se o número for primo, ele deve ser maior que o número da entrada
        if incremento > n:
            print(f"O próximo número primo maior que: {n} é {incremento}")
            break
        else:
            incremento += 1
    else:
        incremento += 1

