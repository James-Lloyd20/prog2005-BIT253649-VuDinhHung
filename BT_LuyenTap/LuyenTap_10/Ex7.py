'''
**Yêu cầu**: Viết chương trình sử dụng while để yêu cầu người dùng nhập mật khẩu cho đến khi đúng từ khóa "python123"
'''

mat_khau = ''
while mat_khau != 'python123':
    mat_khau = input('Vui lòng nhập mật khẩu: ')
    if mat_khau != 'python123':
        print('Mật khẩu bạn vừa nhập vào không đúng, vui lòng nhập lại')

print('Mật khẩu đúng')