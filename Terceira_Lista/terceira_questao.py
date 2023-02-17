# Vamos supor que você faz parte de um grupo de amigos que toda semana sai para jantar
# fora, faça um programa que o usuário informe o valor total da conta, quantos amigos
# estão presentes no jantar, e quanto pretendem dar de gorjeta ( 10 % de gorjeta por
# exemplo) , o programa deve calcular o valor da gorjeta e quanto sai para cada amigo.

# Entrada -> quantidade de amigos, valor total da conta, porcentagem da gorjeta

valor_conta = float(input("Informe o valor total da conta: "))
qtd_amigos = int(input("Informe a quantidade de amigos: "))
gorjeta_porcentagem = int(input("Informe quanto querem dar de gorjeta, em %: "))

# Cálculo da porcentagem = dividir o valor total por 100 e depois multiplicar
# pela porcentagem

gorjeta_valor = (valor_conta / 100) * gorjeta_porcentagem

# Como a gorjeta é um valor a mais, iremos somar com o valor total depois dividir
# para saber quanto cada um vai pagar
valor_para_cada = (valor_conta + gorjeta_valor) / qtd_amigos

print(f"Valor total da conta: {valor_conta}")
print(f"Gorjeta de {gorjeta_porcentagem} = {gorjeta_valor}")
print(f"Valor total com gorjeta: {valor_conta + gorjeta_valor}")
print(f"Quanto cada um deve dar: {valor_para_cada}")