# Faça um programa que tenha uma função que teste se uma frase digitada é um
# palíndromo. Um palíndromo é uma palavra ou frase que pode ser lida no seu sentido
# normal, da esquerda para a direita, bem como no sentido contrário, da direita para a
# esquerda. A função deve retornar TRUE se a frase fornecida for um palíndromo, e o
# programa deve informar ao usuário se a frase ou palavra é um palíndromo.

# Entrada -> uma frase qualquer

frase = str(input("Digite uma frase qualquer para verificar se é um palíndromo: "))

# Função para verificar a frase

def verificar_palindromo(frase):
    # Iremos reservar todas as letras da frase em uma lista, para depois inverter ela
    frase_inversa = []

    # Por fim, iremos comparar as duas frases, utilizando essas variáveis
    frase_comparacao1 = frase
    frase_comparacao2 = ""

    # Loop para adicionar todas as letras da frase na lista acima
    for i in frase:
        # Remover os bytes vazios
        if type(i) != "None":
            # Adiciona na lista
            frase_inversa.append(i)

    # Agora, com o método reverse, iremos reveter todos os item da lista da frase
    # inversa
    frase_inversa.reverse()

    # Loop para montar a string de verificação da segunda frase
    for j in frase_inversa:
        frase_comparacao2 += j

    # Por fim, comparando as duas frases para saber se são iguais de trás para frente
    # Deixaremos as frases todas em caixa baixa (minúscula) utilizando o método lower()
    if frase_comparacao1.lower() == frase_comparacao2.lower():
        return True
    else:
        return False

# Verificação se é ou não um palíndromo
# Essa função irá retornar true ou false, true para sim e false para não
verificar = verificar_palindromo(frase)

if verificar:
    print(f"A frase: {frase} é um palíndromo! ")
else:
    print(f"A frase: {frase} não é um palíndromo :/")