n = int(input("Enter the number of terms: "))

a, b = 0, 1

fib = lambda a, b: (b, a + b)

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = fib(a, b)
