numeros = []

for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    numeros.append(num)

soma = sum(numeros)
media = soma / len(numeros)

print("Soma:", soma)
print(f"Média: {media:.2f}")