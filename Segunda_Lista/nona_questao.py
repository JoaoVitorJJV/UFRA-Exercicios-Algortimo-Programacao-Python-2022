# Faça um algoritmo para que o usuário informe um numero inteiro entre 1 e 10 , e
# calcule a tabuada de multiplicação ( intervalo de 1 a 10 ) do numero informado,
# caso o numero não atenda a restrição, emitir uma mensagem de erro e pedir novo
# número.

# Entrada -> número inteiro entre 1 e 10

# Loop que deixará o programa em execução, como nas questões anteriores
while True:
    n = int(input("Digite um número positivo entre 1 e 10: "))

    # Verificação se o número é positivo
    if n > 0:
        # Verificação se o número está entre 1 e 10
        if 1 <= n <= 10:
            # Loop for que irá desenhar a tabuada na tela e somar

            print(f"___ TABUADA DO {n} ___")
            for i in range(10):
                # Esse seria um jeito mais complexo e resumido, então vou deixar comentado
                #print(f"{n} * {i + 1} = {n * (i + 1)}")

                # Jeito simples

                # Valor da conta
                multiplicacao = n * (i + 1)
                tabuada = f"{n} x {i + 1} = {multiplicacao}"
                print(tabuada)

            break
        else:
            print("O número precisa estar entre 1 e 10")
    else:
        print("O número precisa ser positivo")