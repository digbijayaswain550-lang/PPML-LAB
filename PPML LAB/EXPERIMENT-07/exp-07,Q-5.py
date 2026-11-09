list1 = [1, 2, 3, 4]
tuple1 = (5, 6, 7, 8)

result_list = list(map(int, list1))
result_tuple = list(map(int, tuple1))

print("List:", result_list)
print("Tuple converted to list:", result_tuple)
