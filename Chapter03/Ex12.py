#Bài 12:
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
rows = len(matrix_a)
cols = len(matrix_a[0])
result = [[0 for _ in range(cols)] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        result[i][j] = matrix_a[i][j] + matrix_b[i][j]

print("Kết quả sau khi cộng hai ma trận là:")
for row in result:
    print(row)