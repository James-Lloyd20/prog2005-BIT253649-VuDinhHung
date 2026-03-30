'''
- Nhập một số và tính phần dư của nó khi chia cho 2
- Nếu số nhập vào âm, in thông báo lỗi
'''

num = int(input('Vui lòng nhập 1 số: '))
if num<0:
    print('Số bạn vừa nhập là 1 số âm')
else:
    ketqua = num%2
    print(f'Số bạn vừa nhập có phần dư là: {ketqua}')