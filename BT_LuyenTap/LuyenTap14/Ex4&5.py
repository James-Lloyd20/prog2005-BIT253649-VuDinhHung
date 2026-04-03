'''
Tạo một class Book có thuộc tính name và price, và getter/setter của các thuộc tính
Khởi tạo 1 đối tượng Book. In ra giá trị price của đối tượng
'''
class Book:
    def __init__(self,name,price):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_price(self):
        return self._price
    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            print('Giá không hợp lệ')

sach_cuaa = Book('Python', 150000)
print(f'Giá của sách: {sach_cuaa.get_price()}')



'''
Tạo file txt lưu các thông tin ở bài 4 theo format
Book 1;30000
Book 2;50000
Book 3;100000
Tong;900000
'''
danh_sach_book = [
    Book("Book 1", 30000),
    Book("Book 2", 50000),
    Book("Book 3", 100000)
]
with open("data_book.txt", "w", encoding="utf-8") as file:
    tong_tien = 0
    for sach in danh_sach_book:
        ten = sach.get_name()
        gia = sach.get_price()
        file.write(f"{ten};{gia}\n")
        tong_tien += gia

    file.write(f"Tong;{tong_tien}")
print("\nĐã tạo và ghi thành công file 'data_book.txt'")