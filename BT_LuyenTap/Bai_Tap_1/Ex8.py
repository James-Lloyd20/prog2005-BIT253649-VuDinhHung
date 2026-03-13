'''Xác thực điểm sinh viên nằm trong khoảng `0-10`'''

try:
    score = float(input('Vui lòng nhập điểm của vinh viên nằm trong (0-10): '))
    if 0 <= score <= 10:
        print(f'Điểm của sinh viên vừa được nhập là: {score}')
    else:
        print('Điểm số bạn vừa nhập không năm trong (0-10)')
except ValueError:
    print('Giá trị bạn vừa nhập không hợp lệ')