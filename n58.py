soma = 0
quantidade = 0

while True:
    num = int(input("Digite um número (ou 0 para sair): "))
    
    if num == 0:
        break
    
    if num % 2 == 0:  # verifica se é par
        soma += num
        quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"Média dos números pares: {media:.2f}")
else:
    print("Nenhum número par foi digitado.")