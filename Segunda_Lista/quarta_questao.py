# Faça um programa para ler um valor inteiro positivo até 100. Se o usuário digitar
# um valor fora dessa faixa mandar mensagem de erro e pedir novo valor, assim que
# o usuário digitar um valor valido, calcular a soma dos números entre 1 e o valor
# digitado.

# Entrada -> valor postivo até 100

# Loop que deixa o programa ficar executando e pedindo novos valores, caso o usuário
# digite um valor errado (negativo)
while True:
    n = int(input("Digite um valor positivo até 100: "))

    # Verificação se o número é positivo
    if n > 0:
        # Verificação se o número é menor ou igual a 100
        if n <= 100:
            # Soma dos números positivos utilizando for
            resultado = 0
            for i in range(1, n + 1):
                # += nesse caso aqui, ele faz a conta, pega o valor antigo da variável
                # Soma e reserva o novo valor somado com o valor antigo
                resultado += i

            print(f"A soma dos números de 1 até {n} é de: {resultado}")
            break
        else:
            print("O número precisa ser menor ou igual a 100")
    else:
        print("O número precisa ser positivo")