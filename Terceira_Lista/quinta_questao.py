# Escreva um programa que contenha uma função que receba um número inteiro como
# parâmetro e retorne se ele é primo ou não

# Entrada -> qualquer numero inteiro

# Primeiro, vamos criar uma função para verificar se o número é primo

def verificacao_primo(n):
    # Basta copiar todo o código da questão 4 e fazer algumas alterações
    msg = ""
    if n > 1:
        # Usaremos o laço for para verificar se é primo
        multiplos = 0

        for i in range(2, n):
            if n % i == 0:
                multiplos += 1

        # Se houver um múltiplo além de 1 e o próprio número, o número não é primo
        if multiplos == 0:
            msg = f"{n} é primo"
        else:
            msg = f"{n} não é primo"
    else:
        msg = "O número precisa ser maior que 1"

    return msg

n = int(input("Digite qualquer número maior que um: "))

print( verificacao_primo(n) )


