# Faça um programa para ler dois valores inteiro positivo quaisquer. Se o usuário
# digitar um valor negativo mandar mensagem de erro e pedir novo valor, assim que
# o usuário digitar valores validos, calcular a soma dos números entre esses dois
# números informados

# Entrada -> dois números postivos qualquer

# Loop para o programa pedir, em caso de erro, um novo número
while True:
    primeiro_numero = int(input("Digite um número positivo: "))
    segundo_numero = int(input("Digite um número positivo maior que o segundo: "))
    # Verificação se os números são positivos
    if primeiro_numero and segundo_numero > 0:
        # Loop for para a soma dos números
        resultado = 0
        for i in range(primeiro_numero, segundo_numero + 1):
            resultado += i

        print(f"A soma dos números positivos de {primeiro_numero} à {segundo_numero} foi de = {resultado}")
        break
    else:
        print("Os números precisam ser positivos,")