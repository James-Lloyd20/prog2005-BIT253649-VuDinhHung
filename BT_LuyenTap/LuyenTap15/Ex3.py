'''
Viết một hàm đệ quy để tính giai thừa của một số do người dùng nhập vào.
'''

n = int(input('Vui lòng nhập vào 1 số: '))
tong = 1

for i in range(1, n+1):
    tong = tong*i

print(f'Giai thừa của {n} là: {tong}')
