# Faça um algoritmo para o usuário informar o peso e a altura de uma determinada
# pessoa. Apos a digitação calcular o IMC ( índice de massa corporal ) da pessoa a Informar
# em que faixa ela se enquadra segundo a tabela a seguir : IMC = peso / altura²

# Entrada: peso e altura

peso = float(input("Informe o seu peso: "))
altura = float(input("Infomr a sua altura: "))

imc = peso / (altura ** 2)

# Se a pessoa tiver imc menor que 20 -> abaixo do peso
# Se a pessoa tiver um imc maior ou igual a 25 acima do peso
# Se estiver entre 20 e 25 -> está no peso normal

if imc < 20:
    print("Você está abaixo do peso!")
elif imc < 25 and imc >= 20:
    print("Você está no peso ideal!")
else:
    print("Você está acima do peso!")

print(f"O seu IMC foi de: {imc:.1f}")
