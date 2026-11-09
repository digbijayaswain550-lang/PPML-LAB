arr = list(map(int, input("Enter the elements: ").split()))

positive = len(list(filter(lambda x: x > 0, arr)))
negative = len(list(filter(lambda x: x < 0, arr)))
zero = len(list(filter(lambda x: x == 0, arr)))

n = len(arr)

print("Ratio of positive numbers:", positive / n)
print("Ratio of negative numbers:", negative / n)
print("Ratio of zeroes:", zero / n)
