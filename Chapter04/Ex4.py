'''
Tạo lớp Hoa có các thuộc tính: Tên, Màu . 
Tạo một đối tượng và in thông tin Hoa bằng hàm print() sử dụng đối tượng vừa tạo.
'''

class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

#Test
hoa1 = Hoa('Hoa cúc', 'Vàng và trắng')
print(f'Tên: {hoa1.ten} \nCó màu: {hoa1.mau}')