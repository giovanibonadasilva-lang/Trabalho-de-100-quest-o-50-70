numeros = []

for i in range(8):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = numeros[0]
posicao = 0

for i in range(1, 8):
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i

print(f"Maior valor: {maior}")
print(f"Posição: {posicao + 1}")