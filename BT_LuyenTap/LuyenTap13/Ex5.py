'''
- Tạo một class có tên là Flower, có thuộc tính color
- Viết getter và setter cho thuộc tính trên
- Khởi tạo ví dụ 1 đối tượng và sử dụng getter, setter ở trên 
'''

class Flower:
    def __init__(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

flower = Flower("red")
print(f'Màu sắc của hoa là: {flower.get_color()}')

flower.set_color("blue")
print(f'Màu sắc của hoa sau khi được thay đổi là: {flower.get_color()}')