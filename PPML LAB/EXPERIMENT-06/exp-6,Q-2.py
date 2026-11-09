matrix = []
print("Enter 3 numbers for each row, separated by spaces:")

for i in range(3):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    matrix.append(row)

print("\n--- Matrix and Sums ---")
for row in matrix:
    row_sum = sum(row)
    print(f"{row}  --> Row Sum: {row_sum}")


col_sums = [sum(matrix[i][j] for i in range(3)) for j in range(3)]
print("-" * 25)
print(f"Col Sums: {col_sums}")
