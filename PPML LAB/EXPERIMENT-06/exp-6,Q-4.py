numbers = list(map(int, input("Enter the list elements: ").split()))

value = int(input("Enter the value to search: "))

check = lambda x: x in numbers

if check(value):
    print("Value is present in the list")
else:
    print("Value is not present in the list")
