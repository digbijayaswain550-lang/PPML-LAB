def even_values(numbers):
    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    return even


numbers = [10, 15, 20, 25, 30, 35, 40]

new_list = even_values(numbers)

print("Even values:", new_list)
