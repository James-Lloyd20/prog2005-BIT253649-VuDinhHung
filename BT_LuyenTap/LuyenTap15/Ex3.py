'''
Viết một hàm đệ quy để tính giai thừa của một số do người dùng nhập vào.
'''

n = int(input('Vui lòng nhập vào 1 số: '))
def giaithua(n):
    if n ==0:
        return 1
    else:
        return n * giaithua(n-1)
print(f'Giai thừa của {n} là: {giaithua(n)}')
