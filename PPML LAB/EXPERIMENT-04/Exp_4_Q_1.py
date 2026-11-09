"""WAP to print the second largest and second smallest element in a list of 10 integers without using sort function."""
num = []
for i in range(10):
    n = int(input("Enter a integer :"))
    num.append(n)
largest = num[0]
smallest = num[0]
for n in num:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
second_largest = None
second_smallest = None
for n in num:
    if n != largest:
        if second_largest is None or n > second_largest:
            second_largest = n
    if n != smallest:
        if second_smallest is None or n < second_smallest:
            second_smallest = n
print("Second Largest =",second_largest)
print("Second Smallest =",second_smallest)
