'''
Tạo class Vector, có thuộc tính x và y. Nạp chồng toán tử add (+) cho lớp Vector
Chạy ví dụ
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
def main():
    v1 = Vector(9, 6)
    v2 = Vector(8, 4)
    v3 = v1 + v2
    print(v3)
if __name__ == "__main__":
    main()