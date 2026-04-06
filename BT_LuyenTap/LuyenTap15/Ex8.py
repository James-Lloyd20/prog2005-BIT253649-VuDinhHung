'''
Tạo lớp Product với thuộc tính price và getter/setter. Kiểm tra và báo lỗi nếu price < 0
'''

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Giá sản phẩm không được âm')
        self._price = value 

try:
    user_input = float(input('Vui lòng nhập giá sản phẩm: '))
    product = Product(user_input)
    print(f'Giá sản phẩm đã được thiết lập là: {product.price}')
except ValueError as loi:
    print(f'Đã xảy ra lỗi: {loi}')