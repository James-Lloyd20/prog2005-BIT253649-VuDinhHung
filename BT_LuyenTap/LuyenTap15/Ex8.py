'''
Tạo lớp Product với thuộc tính price và getter/setter. Kiểm tra và báo lỗi nếu price < 0
'''

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Giá sản phẩm không được âm')
        self._price = value 