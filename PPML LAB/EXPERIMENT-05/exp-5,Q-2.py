d = {
    "A": [1, 2, 3, 4],
    "B": [1, 2],
    "C": [5, 6, 7, 8, 9]
}

max_key = None
max_count = 0

for key in d:
    unique_values = set(d[key])

    if len(unique_values) > max_count:
        max_count = len(unique_values)
        max_key = key

print("Key with maximum unique values:", max_key)
print("Number of unique values:", max_count)
