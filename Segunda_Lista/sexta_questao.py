# Faça um programa para ler um valor inteiro positivo até 100. Se o usuário digitar
# um valor fora dessa faixa mandar mensagem de erro e pedir novo valor, assim que
# o usuário digitar um valor valido, calcular a soma dos números PARES entre 1 e o
# valor digitado.

# Entrada -> Valor positivo até 100

# Loop que deixa o programa em execução em caso de erro na entrada de dados
while True:
    n = int(input("Digite um número postivo até 100: "))

    # Verificação se o número é positivo
    if n > 0:
        # Verificação se o número é menor ou igual a 100
        if n <= 100:
            resultado = 0
            # Loop para somarmos os números pares
            for i in range(1, n + 1):
                # Utilizaremos o mesmo operador "%" da segunda questão
                if i % 2 == 0:
                    resultado += i
                    print("Numero: ", i)

            print(f"A soma dos números pares de 1 à {n} foi de: {resultado}")
            break
        else:
            print("O número precisa estar entre 1 e 100")
    else:
        print("O número precisa ser positivo")