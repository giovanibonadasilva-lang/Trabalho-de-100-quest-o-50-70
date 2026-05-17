for n in range(1, 101):
    if n <= 1:
        continue

    primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primo = False
            break

    if primo:
        print(n)
