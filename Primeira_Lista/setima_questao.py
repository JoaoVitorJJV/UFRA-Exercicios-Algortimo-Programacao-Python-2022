# A partir dos valores dos lados de um triangulo faca um algoritmo que calcule se esses
# lados podem realmente formar um triangulo. Para existir um triangulo é necessário que
# a soma de dois lados quaisquer (tem que testar todas as combinações possíveis) seja
# maior ou igual que o outro lado. Apos esse calculo o algoritmo ainda deve informar se
# o triangulo é escaleno (todos os lados diferentes), Isósceles (dois lados iguais ) ou
# equilátero ( todos os lados iguais).

primeiro_lado = int(input("Digite o primeiro lado: "))
segundo_lado = int(input("Digite o segundo lado: "))
terceiro_lado = int(input("Digite o terceiro lado: "))

# Condição para saber se é um triângulo ( a soma dos primeiros dois lados precisa ser
# diferente do terceiro lado

if primeiro_lado + segundo_lado != terceiro_lado:
    if primeiro_lado != segundo_lado != terceiro_lado:
        print("O Triângulo é escaleno")
    elif primeiro_lado == segundo_lado == terceiro_lado:
        print("O Triângulo é equilátero")
    else:
        print("O Triângulo é isósceles")
else:
    print("Não é um triângulo")