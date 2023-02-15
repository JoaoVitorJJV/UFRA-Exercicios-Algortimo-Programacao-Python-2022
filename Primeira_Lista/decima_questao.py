# Faça um algoritmo para ler o ano de nascimento de uma pessoa e informar quantos
# anos ela tem. Após isso o algoritmo deve imprimir uma mensagem segundo a tabela
# abaixo:

# Se a idade for menor que 18 anos -> menor de idade
# Se a idade estiver entre 18 e 50 -> maior de idade
# Se a idade for maior que 50 > sênior

idade = int(input("Informe sua idade: "))

if idade < 18:
    print("Menor de idade")
elif 18 <= idade <= 50:
    print("Maior de idade")
else:
    print("Sênior")