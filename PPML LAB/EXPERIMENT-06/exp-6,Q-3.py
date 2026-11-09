def transpose(matrix, n):
    print("Transpose of the matrix:")
    for i in range(n):
        for j in range(n):
            print(matrix[j][i], end=" ")
        print()


n = int(input("Enter the order of matrix: "))

matrix = []
print("Enter the elements:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose(matrix, n) 
