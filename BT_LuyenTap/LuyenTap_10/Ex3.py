'''
**Yêu cầu**: Viết một hàm đệ quy để tính giai thừa của một số do người dùng nhập vào.
'''

def giai_thua(n):
    if n <= 1:
        return 1
    return n * giai_thua(n - 1)

try:
    num = int(input('Vui lòng nhập một số nguyên dương: '))
    if num < 0:
        print('Số nhập vào phải lớn hơn hoặc bằng 0')
    else:
        print(f'Số "{num} có giai thừa là: {giai_thua(num)}')
except ValueError:
    print('Lỗi: sô nguyên bạn vừa nhập không  hợp lệ')