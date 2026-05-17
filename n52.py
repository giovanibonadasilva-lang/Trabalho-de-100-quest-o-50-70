maior = None
menor = None

for i in range(1, 11):
    num = int(input(f"Digite o {i}º número: "))
    
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print("\nMaior número:", maior)
print("Menor número:", menor)