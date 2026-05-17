n = int(input("Digite um número inteiro: "))

invertido = 0

while n != 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10

print("Número invertido:", invertido)