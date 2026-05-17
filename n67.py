numeros = []
quadrados = []

# Lendo os 7 números
for i in range(7):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Calculando os quadrados
for n in numeros:
    quadrados.append(n ** 2)

print("Lista original:", numeros)
print("Lista dos quadrados:", quadrados)