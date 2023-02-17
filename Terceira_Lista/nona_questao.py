# Desenvolva um programa para entrar com dois números inteiros quaisquer, a seguir o
# programa deve informar quais são os números primos presentes no intervalo formado
# por esses dois números, caso os números digitados sejam inadequados mandar
# mensagem de erro e pedir os números novamente .

# Entrada -> dois números inteiro qualquer, adequeados para um intervalo (um tem que ser
# maior que o outro)

primeiro_numero = int(input("Digite um número maior que 1: "))
segundo_numero = int(input("Digite um segundo número maior que o anterior: "))

# Loop para o programa não parar caso algum número seja inserido incorretamente

while True:
    # Verificação se são maiores que 1
    if primeiro_numero > 1 and segundo_numero > 1:
        # Verificação se o primeiro é menor que o segundo
        if primeiro_numero < segundo_numero:
            # Loop para calcularmos em sequência, os números primos entre o intervalo
            # Reservaremos os primos em uma lista
            numeros_primos = []

            for i in range(primeiro_numero, segundo_numero + 1):
                multiplos = 0
                for j in range(2, i):
                    if i % j == 0:
                        multiplos += 1

                # Se houver um múltiplo além de 1 e o próprio número, o número não é primo
                if multiplos == 0:
                    numeros_primos.append(i)

            print(f"Os números primos de {primeiro_numero} à {segundo_numero} são: {numeros_primos}")
            break
        else:
            print("O segundo número precisa ser maior que o primeiro")
    else:
        print("Os números precisam ser maiores que 1")