# Faça um programa para ler dois valores inteiro positivo
# quaisquer. Se o usuário digitar um valor negativo mandar
# mensagem de erro e pedir novo valor, assim que o usuário
# digitar valores validos, criar uma lista com somente os
# números PARES e outra lista com os números IMPARES entre
# esses dois números informados , ao final imprimir a soma dos
# números em cada lista bem como o conteúdo da lista.

# Entrada -> Dois valores inteiros positivos qualquer

# Loop que deixará o programa em execução caso aconteça algum erro de entrada
while True:
    primeiro_numero = int(input("Digite um número inteiro positivo: "))
    segundo_numero = int(input("Digite um númrero inteiro postivio maior que o anterior: "))

    # Verificação se o número é positivo
    if primeiro_numero > 0 and segundo_numero > 0:
        # Lista dos números pares e impares
        pares = []
        impares = []


        # Loop para percorrer entre os números digitados
        for i in range(primeiro_numero, segundo_numero + 1):

            # Condição para saber se o número é par ou impar, utilizando o operador %
            if i % 2 == 0:
                # É par, logo, entra na lista de números pares
                pares.append(i)
            else:
                # É ímpar, entra na lista de números impares
                impares.append(i)

        # Soma dos valores das duas listas
        resultado_par = 0
        resultado_impar = 0

        for i in pares:
            resultado_par += i

        for j in impares:
            resultado_impar += j

        print("Lista números pares: ", pares)
        print("Lista números impares: ", impares)
        print(f"Soma números pares: {resultado_par}")
        print(f"Soma números impares: {resultado_impar}")
        break
    else:
        print("Os números precisam ser positivos")