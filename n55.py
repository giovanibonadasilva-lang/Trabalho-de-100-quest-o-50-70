n = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, n + 1):
    if n % i == 0:
        soma += i

print("Soma dos divisores:", soma)