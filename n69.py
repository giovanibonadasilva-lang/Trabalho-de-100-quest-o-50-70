numeros = []

# Lendo os 10 números
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Removendo repetidos
sem_repetidos = []

for n in numeros:
    if n not in sem_repetidos:
        sem_repetidos.append(n)

print("Lista original:", numeros)
print("Sem repetidos:", sem_repetidos)