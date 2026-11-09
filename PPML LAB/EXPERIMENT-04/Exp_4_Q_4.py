def Fibonacci(n):
    a = 0
    b = 1

    print("First", n, "terms of Fibonacci series:")

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter the number of terms: "))
Fibonacci(n)
