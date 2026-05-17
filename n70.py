notas = []

# Lendo as notas
for i in range(10):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

# Calculando a média da turma
media = sum(notas) / len(notas)

# Contando quantos estão acima da média
acima_media = 0

for nota in notas:
    if nota > media:
        acima_media += 1

print(f"\nMédia da turma: {media:.2f}")
print(f"Quantidade de alunos acima da média: {acima_media}")