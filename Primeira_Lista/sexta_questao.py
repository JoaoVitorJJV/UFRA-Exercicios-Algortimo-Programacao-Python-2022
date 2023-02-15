# Faça um algoritmo para ler 4 valores e informar qual o menor , qual o maior , a soma
# dos valores e a média aritmética dos números digitados

# Entrada de 4 valores
primeiro_val = int(input("Informe o primeiro valor: "))
segundo_val = int(input("Informe o segundo valor: "))
terceiro_val = int(input("Informe o terceiro valor: "))
quarto_val = int(input("Informe o quarto valor: "))

maior_valor = 0
menor_valor = 0

# Condições de MAIOR VALOR
if primeiro_val > segundo_val and primeiro_val > terceiro_val and primeiro_val > quarto_val:
    maior_valor = primeiro_val
elif segundo_val > primeiro_val and segundo_val > terceiro_val and segundo_val > quarto_val:
    maior_valor = segundo_val
elif terceiro_val > primeiro_val and terceiro_val > segundo_val and terceiro_val > quarto_val:
    maior_valor = terceiro_val
elif quarto_val > primeiro_val and quarto_val > segundo_val and quarto_val > terceiro_val:
    maior_valor = quarto_val

# Condições de MENOR VALOR
if primeiro_val < segundo_val and primeiro_val < terceiro_val and primeiro_val < quarto_val:
    menor_valor = primeiro_val
elif segundo_val < primeiro_val and segundo_val < terceiro_val and segundo_val < quarto_val:
    menor_valor = segundo_val
elif terceiro_val < primeiro_val and terceiro_val < segundo_val and terceiro_val < quarto_val:
    menor_valor = terceiro_val
elif quarto_val < primeiro_val and quarto_val < segundo_val and quarto_val < terceiro_val:
    menor_valor = quarto_val

soma_valores = primeiro_val + segundo_val + terceiro_val + quarto_val
media_valores = soma_valores / 4

print(f"MAIOR VALOR: {maior_valor}\nMENOR VALOR: {menor_valor} \nSOMA: {soma_valores}\nMÉDIA: {media_valores}")



