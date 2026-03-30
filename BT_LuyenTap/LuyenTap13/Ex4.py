'''
Viết một hàm đệ quy để tính tổng 1+2+..+n, với  n của một số do người dùng nhập vào
'''

def tinhtong(n):
    tong=0
    if n==0:
        return 0
    else:
        return n + tinhtong(n-1)

user_input = int(input('Vui lòng nhập 1 số n: '))
print(f'Tổng của các số n là: {tinhtong(user_input)}')

