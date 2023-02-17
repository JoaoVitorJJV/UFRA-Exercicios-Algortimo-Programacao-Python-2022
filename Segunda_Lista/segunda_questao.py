# Faça um algoritmo para ler dois valores em um intervalo, a seguir o programa deve
# imprimir todos os números pares nesse intervalo, para saber se um numero é par ,
# use o operador % , veja o exemplo abaixo:

# Utilizaremos o for combinado com o range novamente, para esse intervale
# Porém, iremos deixar o usuário escolher o intervalo, tendo no máximo 100

comeco = int(input("Escolha um número de 1 a 100"))
fim = int(input("Agora escolha um número de 1 a 100 porém maior que o anterior"))

# Criaremos também uma lista com todos os números pares
numeros_pares = []

for i in range(comeco, fim):
    numero = i

    # Fórmula para saber se o número é par, utilizando o operador de resto de
    # divisao = %
    if numero % 2 == 0:
        numeros_pares.append(i)


# Imprimir todos os números pares após o loop, utilizando a lista criada
print(f"Os números pares do intervalo de {comeco} à {fim} são: ")
for j in numeros_pares:
    print(j)