a = list(map(int, input("Enter elements of first array: ").split()))
b = list(map(int, input("Enter elements of second array: ").split()))

intersection = lambda x: x in b

result = list(filter(intersection, a))

print("Intersection of two arrays:", result)
