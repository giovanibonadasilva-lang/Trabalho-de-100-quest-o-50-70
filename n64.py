numeros = []
pares = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)
    
    if num % 2 == 0:
        pares.append(num)

print("Números digitados:", numeros)
print("Números pares:", pares)