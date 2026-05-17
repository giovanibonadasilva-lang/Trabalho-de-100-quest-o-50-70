n = int(input("Digite um número inteiro: "))

if n <= 1:
    print("Não é primo")
else:
    primo = True
    
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    
    if primo:
        print("É primo")
    else:
        print("Não é primo")

        