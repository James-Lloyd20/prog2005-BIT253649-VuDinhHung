'''
Yêu cầu người dùng nhập vào một số trong khoảng từ 1 đến 9, sau đó hiển thị bảng cửu chương của số đó từ 1 đến 9
'''

num = int(input('Vui lòng nhập vào 1 số trong khoảng (1-9): '))

try:
    if num >= 1 and num <= 9:
        for i in range(1, 10):
            print(f'{num} x {i} = {num * i}')
            
    else:
        print('Vui lòng nhập lại 1 số (1-9)')
except ValueError:
    print('Vui lòng nhập 1 số hợp lệ')