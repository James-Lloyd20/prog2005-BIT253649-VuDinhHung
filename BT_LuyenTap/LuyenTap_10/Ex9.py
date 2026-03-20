'''
**Yêu cầu**: Tạo một 2 class bất kỳ bao gồm
- constructor
- getter
- setter
- __str__
- phương thức đối tượng
- phương thức lớp
- static method
- có xác thực thuộc tính sử dụng ValueError bằng 2 cách
- Nạp chồng toán tử `==`
- 1 trong 2 class có kế thừa từ class kia
Chạy ví dụ in ra màn hình tất cả các thành phần của class ở trên
'''

class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price 

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Lỗi: giá tiền cho điện thoại không thể là số âm')
        self._price = value

    def __str__(self):
        return f'Smartphone[{self.brand} {self.model}, có giá: {self.price}]'

    def play_music(self):
        return f'Chiếc {self.model} này đang phát một bản nhạc'

    @classmethod
    def create_budget_phone(cls, brand, model):
        return cls(brand, model, 199)

    @staticmethod
    def is_valid_brand(brand):
        valid_brands = ['SamSung', 'Apple', 'Pixel', 'OnePlus']
        return brand in valid_brands

    def __eq__(self, other):
        if isinstance(other, Smartphone):
            return self.brand == other.brand and self.model == other.model
        return False

class IPhone(Smartphone):
    def __init__(self, model, price, ios_version):
        super().__init__('Apple', model, price)
        
        if not isinstance(ios_version, float):
            raise ValueError('Lỗi (Cách 2): Phiên bản iOS phải là số thập phân (ví dụ: 18.1, 26.3)!')
        self.ios_version = ios_version

    def __str__(self):
        return f'iPhone[{self.model}, iOS: {self.ios_version}, Giá: {self.price}$]'


def vi_du():
    print('=== IN RA CÁC THÀNH PHẦN CLASS ===')
    try:
        my_phone = IPhone('15', 450, 26.3)
        another_phone = Smartphone('Apple', '15', 450)
        
        print('1. In ra đối tượng:')
        print(my_phone)
        
        print('\n2. Phương thức của đối tượng:')
        print(my_phone.play_music())
        
        print('\n3. Nạp chồng toán tử:')
        print(f'Kết quả: {my_phone == another_phone}')
        
        budget_phone = Smartphone.create_budget_phone('Pixe;', '7 Pro')
        print('\n4. Phương thức lớp:')
        print(budget_phone)
        
        print('\n5. Phương thức tĩnh:')
        print(f'Hãng "Apple" hợp lệ không? -> {Smartphone.is_valid_brand("Apple")}')
        print(f'Hãng "OnePlus" hợp lệ không? -> {Smartphone.is_valid_brand("OnePlus")}')
        
        print('\n6. Kiểm tra Validate Cách 1:')
        error_phone_1 = Smartphone('Samsung', 'Galaxy', -50)
        
    except ValueError as e:
        print(f'Lỗi: {e}')
        
    try:
        print('\n7. Kiểm tra Validate Cách 2:')
        error_phone_2 = IPhone('16 Pro', 999, 'Mười Tám')
    except ValueError as e:
        print(f'Lỗi: {e}')

if __name__ == '__main__':
    vi_du()