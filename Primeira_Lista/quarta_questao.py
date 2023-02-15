# Equação linear
# Entrada: valores de: a, b, c, d, e, f

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
d = int(input("Valor de d: "))
e = int(input("Valor de e: "))
f = int(input("Valor de f: "))

x = (c * e - b * f ) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

print(f"O valor de x é: {x} e o valor de y é de: {y}")