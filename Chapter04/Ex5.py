'''
Tạo lớp Product với thuộc tính _price và getter/setter kiểm tra giá > 0. 
Viết hàm __str__ để in thông tin price của product
'''

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá của sản phẩm phải lớn hơn 0")

    def __str__(self):
        return f'Giá của sản phẩm là: {self.price:,.0f} VNĐ'
    
# Test
if __name__ == "__main__":
    try:
        product1 = Product(100000)
        print(product1)
        
        product1.price = 150000
        print(product1)
        
        product1.price = -30000
        print(product1)
        
    except ValueError as e:
        print(f'Lỗi: {e}')