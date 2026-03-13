'''
Xử lý danh sách đa chiều. Viết chương trình cho phép:
- Khởi tạo và nhập một ma trận M x N với các phần tử ngẫu nhiên
- Hiển thị bất kỳ hàng nào dựa trên đầu vào của người dùng (ví dụ: yêu cầu hiện thị hàng 3)
- Hiển thị bất kỳ cột nào dựa trên đầu vào của người dùng (ví dụ: yêu cầu hiện thị cột 2)
- Hiển thị giá trị lớn nhất trong ma trận
'''

import random
M = int(input('Vui lòng nhập số hàng của ma trận: '))
N = int(input('Vui lòng nhập số cột của ma trận: '))

matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(1, 100))
    matrix.append(row)

print('Ma trận đã được tạo là: ')
for row in matrix:
    print(row)

row_index = int(input(f'Vui lòng nhập số hàng bạn muốn hiển thị (1-{M}): ')) - 1
if 0 <= row_index < M:
    print(f'Hàng {row_index + 1} của ma trận là: {matrix[row_index]}')  
else:
    print('Số hàng không hợp lệ')

col_index = int(input(f'Vui lòng nhập số cột bạn muốn hiển thị (1-{N}): ')) - 1
if 0 <= col_index < N:
    print(f'Cột {col_index + 1} của ma trận là: {[row[col_index] for row in matrix]}')
else:
    print('Số cột không hợp lệ')

max_value = max(max(row) for row in matrix)
print(f'Giá trị lớn nhất trong ma trận là: {max_value}')