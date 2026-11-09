numbers = [2, 3, 4, 5]

result = list(map(lambda x, i: x ** i, numbers, range(len(numbers))))

print("Result:", result)
