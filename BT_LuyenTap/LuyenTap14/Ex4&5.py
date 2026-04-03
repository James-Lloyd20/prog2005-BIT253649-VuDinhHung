'''
Tạo một class Book có thuộc tính name và price, và getter/setter của các thuộc tính
Khởi tạo 1 đối tượng Book. In ra giá trị price của đối tượng
'''
class Book:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            print('Giá không hợp lệ, mặc định gán bằng 0')
            self._price = 0
sach_cuaa = Book('Python', 150000)
print(f'Giá của sách vừa tạo: {sach_cuaa.price}')


'''
Tạo file txt lưu các thông tin ở bài 4 theo format
Book 1;30000
Book 2;50000
Book 3;100000
Tong;900000
'''
danh_sach_sach = []
try:
    so_luong = int(input("Bạn muốn nhập bao nhiêu cuốn sách? "))
    for i in range(so_luong):
        print(f"\n=== Vui lòng nhập thông tin sách thứ {i+1} ===")
        ten_sach = input("Nhập tên sách (vd: Book 1): ")
        gia_sach = int(input("Nhập giá tiền: "))
        
        sach_moi = Book(ten_sach, gia_sach)
        danh_sach_sach.append(sach_moi)
    with open("data_book.txt", "w", encoding="utf-8") as file:
        tong_tien = 0
        for sach in danh_sach_sach:
            ten = sach.name
            gia = sach.price
            file.write(f"{ten};{gia}\n")
            tong_tien += gia
        file.write(f"Tong;{tong_tien}")
    print("\nĐã lưu thông tin bạn vừa nhập vào file 'data_book.txt'")

except ValueError:
    print("Lỗi: Số lượng và giá tiền phải là 1 số nguyên")