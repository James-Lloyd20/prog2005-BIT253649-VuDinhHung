'''
Viết chương trình nhập điểm 3 môn, tính trung bình và in ra xếp loại: Giỏi (>=8), Khá (6.5 - 7.9), 
Trung bình (5.0 - 6.4), Yếu (<5)
'''

a = float(input('Vui lòng nhập điểm môn 1: '))
b = float(input('Vui lòng nhập điểm môn 2: '))
c = float(input('Vui lòng nhập điểm môn 3: '))

diemTB = (a+b+c)/3
if diemTB < 5:
    print(f'Điểm trung bình {diemTB:.2f} xếp loại Yếu')
elif diemTB < 6.5:
    print(f'Điểm trung bình {diemTB:.2f} xếp loại Trung bình')
elif diemTB < 8:
    print(f'Điểm trung bình {diemTB:.2f} xếp loại Khá')
else:
    print(f'Điểm trung bình {diemTB:.2f} xếp loại Giỏi')

