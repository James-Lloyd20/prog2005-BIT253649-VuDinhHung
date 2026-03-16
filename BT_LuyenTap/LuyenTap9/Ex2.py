'''Người dùng nhập vào 1 số và tính tổng các chữ số của số đó'''

num = input('Vui lòng nhập vào một số: ')
tong = 0

for i in num:
    tong = tong + int(i)
   
print(f'Tổng các chữ số của "{num}" là: {tong}')