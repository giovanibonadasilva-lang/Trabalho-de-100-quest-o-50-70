lista1 = []
lista2 = []
lista3 = []

# Lendo a primeira lista
print("Digite os valores da lista 1:")
for i in range(5):
    lista1.append(int(input(f"Valor {i+1}: ")))

# Lendo a segunda lista
print("\nDigite os valores da lista 2:")
for i in range(5):
    lista2.append(int(input(f"Valor {i+1}: ")))

# Somando os elementos
for i in range(5):
    lista3.append(lista1[i] + lista2[i])

print("\nLista 1:", lista1)
print("Lista 2:", lista2)
print("Lista soma:", lista3)