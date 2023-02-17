# Escreva um programa que o usuário digite um numero inteiro n qualquer e gere os n
# primeiros termos da série de Fibonacci. Nesta série, os dois primeiros termos são 1 e os
# próximos são a soma dos dois anteriores. Serie de Fibonacci: 1, 1, 2, 3, 5, 8, 13,...

# Entrada -> número n qualquer que será o fim da sequêcia

n = int(input("Digite um número inteiro maior que 1: "))

fim_sequencia = n

# Loop for para criar a sequência fibonnaci

penultimo_valor = 1
ultimo_valor = 1
for i in range (n):
    # Os primeiros dois termos da sequência fibonnaci são 1, então faremos
    # uma condição para isso
    if i < 2:
        print(1)
    else:
        # Então, temos a sequência fibonnaci
        valor_sequencia = ultimo_valor + penultimo_valor
        penultimo_valor = ultimo_valor
        ultimo_valor = valor_sequencia
        print(valor_sequencia)