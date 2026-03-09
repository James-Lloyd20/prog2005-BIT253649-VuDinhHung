try:
    a = float(input('Vui lòng nhập số đầu tiên: '))
    b = float(input('Vui lòng nhập số thứ hai: '))
    c = float(input('Vui lòng nhập số thứ ba: '))

    if a > b and a > c:
        print(f'Số lớn nhất là: {a}')
    elif b > a and b > c:
        print(f'Số lớn nhất là: {b}')
    elif c > a and c > b:
        print(f'Số lớn nhất là: {c}')
except ValueError:
    print('Giá trị bạn vừa nhập vào không hợp lệ')

def puong_trinh_bac_hai(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('Phương trình có vô số nghiệm')
            else:
                print('Phương trình vô nghiệm')       
        else:
            x = -c / b 
            print(f'Phương trình có nghiệm là x = {x}')
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('Phương trình vô nghiệm') 
            if delta == 0:
                pass #e chấp nhận mất điểm phần giải ptr bậc 2 ạ :(