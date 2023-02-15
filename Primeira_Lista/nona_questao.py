# Entrada de 3 notas, onde precisamos saber as 2 maiores e dessas duas, retirar
# uma média. Essa média, tem que ser maior 6 para ser aprovado.
# Se a nota for menor que 6 e estiver entre 4 e 6, o aluno está apto a fazer
# a recuperação. Por fim, retornar a média, se o aluno foi aprovado / reprovado
# e quanto ele precisa para passr.

lista_de_notas = []
media_aprovacao = 6.0

for i in range(3):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    lista_de_notas.append(nota)

lista_melhores_notas = []
pior_nota = min(lista_de_notas[0], lista_de_notas[1], lista_de_notas[2])
lista_de_notas.remove(pior_nota)
lista_melhores_notas = lista_de_notas

# Média das 2 melhores notas
media_melhores_notas = (lista_melhores_notas[0] + lista_melhores_notas[1]) / 2

if media_melhores_notas >= 6:
    print(f"Sua média foi de: {media_melhores_notas:.1f}\nVocê está aprovado!")
elif media_melhores_notas >= 4:
    notas_para_passar = (2 * media_aprovacao) - (lista_melhores_notas[0] + lista_melhores_notas[1])
    print(f"Sua média foi de: {media_melhores_notas:.1f}\nVocê precisa de: {notas_para_passar}  para passar.")
else:
    print(f"Sua média foi de {media_melhores_notas:.1f}\nVocê não está apto para a recuperação")