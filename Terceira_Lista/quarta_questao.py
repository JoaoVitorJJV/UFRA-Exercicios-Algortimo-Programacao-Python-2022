# Um número primo é um número inteiro maior que 1 que só é divisível por 1 e por ele
# mesmo. Escreva um programa que leia um numero inteiro do usuário e exiba uma
# mensagem indicando se ele é ou não primo

# Entrada -> qualquer número inteiro

n = int(input("Digite um número para saber se é primo: "))

# Verificação se o número é maior que 1

if n > 1:
    # Usaremos o laço for para verificar se é primo
    multiplos = 0

    for i in range(2, n):
        if n % i == 0:
            multiplos += 1

    #Se houver um múltiplo além de 1 e o próprio número, o número não é primo
    if multiplos == 0:
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")
else:
    print("O número precisa ser maior que 1")