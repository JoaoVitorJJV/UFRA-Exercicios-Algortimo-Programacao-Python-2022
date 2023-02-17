# Escreva um programa em que o usuário informe o valor dos dois catetos de um triangulo
# retângulo e o programa calcule o valor da hipotenusa

# Entrada -> número qualquer
from math import sqrt

n = int(input("Escreva o número que você deseja calcular a raiz quadrada: "))

# Método sqrt, da biblioteca math que retorna a raiz quadrada de qualquer número
raiz = sqrt(n)

print(f"A raiz quadrada de {n} é: {raiz}")