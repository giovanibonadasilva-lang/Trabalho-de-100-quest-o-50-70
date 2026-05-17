nomes = []

for i in range(6):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

nomes.sort()

print("\nNomes em ordem alfabética:")
for nome in nomes:
    print(nome)