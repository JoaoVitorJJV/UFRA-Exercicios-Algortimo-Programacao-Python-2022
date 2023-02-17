# Desenvolva um programa para calcular o fatorial de um valor que será digitado.
# Este valor não pode ser negativo, em caso de valor inadequado o programa deve
# enviar mensagem de erro e pedir um valor valido.

# Entrada -> Qualquer número positivo

# Fazer o programa continuar rodando e pedindo os números

while True:
    numero = int(input("Digite um número postiivo para calcular o fatorial: "))
    # Verificação do número positivo
    if numero >= 0:
       fatorial = 1
       # Cálculo do fatorial utilizando loop com range
       for i in range(1, numero + 1):
           fatorial = fatorial * i

       print(f"O Fatorial de {numero} é = {fatorial}")
       # Quebra a execução do loop
       break
    else:
        print("Só aceitamos números positivos, por favor, tente novamentoe")