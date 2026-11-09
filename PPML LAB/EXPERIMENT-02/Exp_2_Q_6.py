n = int(input("Enter a 3-digit number: "))

factors = []

i = 2

while n > 1:
    if n % i == 0:
        factors.append(i)
        n = n // i
    else:
        i = i + 1

print("Prime factors are:", factors)
