n = int(input("Digite um número inteiro: "))
if n == 0:
   print("Binário: 0")
else:
   binario = ""

while n > 0:
    resto = n % 2
    binario = str(resto) + binario
    n = n // 2

print("Binário:", binario)