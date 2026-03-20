'''
**Yêu cầu**: Nhập một chuỗi và in ra độ dài của nó. 
Xử lý trường hợp người dùng nhập chuỗi rỗng bằng cách hiển thị thông báo lỗi.
'''

chuoi = input('Vui lòng nhập vào 1 chuỗi mà bạn muốn tính độ dài: ')
try:
    if chuoi == '':
        raise ValueError('Lỗi: bạn vừa nhập vào 1 chuỗi rống')
    print(f'Chuỗi bạn vừa nhập có độ dài bằng: {len(chuoi)}')
except ValueError as e:
    print(e)