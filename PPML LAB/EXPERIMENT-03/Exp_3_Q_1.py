N = int(input("Enter a number: "))

for i in range(2, N):
    d = 0

    for j in range(1, i + 1):
        if i % j == 0:
            d += 1

    if d == 2:
        n = i + 2
        d = 0

        for j in range(1, n + 1):
            if n % j == 0:
                d += 1

        if d == 2:
            print(i, n)
