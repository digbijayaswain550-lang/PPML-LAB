from collections import Counter

def group_matrix(matrix):
    flat_list = [item for row in matrix for item in row]

    counts = Counter(flat_list)
    grouped_matrix = [[element] * count for element, count in counts.items()]
   
    return grouped_matrix

input_matrix = [
    [1, 2, 1],
    [3, 2, 1],
    [4, 3, 2]
]

print("Grouped Matrix:")
for row in group_matrix(input_matrix):
    print(row)
