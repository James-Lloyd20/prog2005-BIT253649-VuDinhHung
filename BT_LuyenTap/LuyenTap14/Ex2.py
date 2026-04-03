'''
- Tạo một danh sách chứa tên của 5 người nhập từ bàn phím. 
- Xóa tên người ở vị trí thứ hai trong danh sách
- In danh sách sau mỗi thao tác
'''

list = []
for i in range(5):
    ten = input(f'Vui lòng nhập tên của người thứ {i+1}: ')
    list.append(ten)
    print(f'Danh sách hiện tại: {list}')
if len(list)>=2:
    xoa_ten=list.pop(1)
    print(f'\nĐã xóa tên người ở vị trí 2: {xoa_ten}')
else:
    print('\nDanh sách không đủ người để xóa')
print(f'Kết quả sau khi xóa người thứ 2 là: {list}')