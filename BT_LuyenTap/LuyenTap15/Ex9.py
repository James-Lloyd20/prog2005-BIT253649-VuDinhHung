'''
Viết hàm nhập 1 chuỗi ký tự từ bàn phím, lưu ký tự này vào file txt
'''

user_input = input('Vui lòng nhập một chuỗi ký tự: ')

with open('user_input.txt', 'w') as f:
    f.write(user_input)