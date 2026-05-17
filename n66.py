numeros = []

# Lendo os 10 números
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Valor a ser buscado
valor = int(input("Digite o valor que deseja contar: "))

# Contagem
contador = numeros.count(valor)

print(f"O valor {valor} aparece {contador} vez(es) na lista.")