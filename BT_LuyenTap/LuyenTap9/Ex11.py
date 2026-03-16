'''
Tạo class method của class SinhVien đếm số đối tượng được tạo ra.
Chạy ví dụ
'''

class SinhVien:
    count = 0
    def __init__(self, name):
        self.name = name
        SinhVien.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
def main():
    sv1 = SinhVien('James')
    sv2 = SinhVien('Alex')
    sv3 = SinhVien('Stella')
    print(f'Số lượng sinh viên được tạo ra là: {SinhVien.get_count()}')
if __name__ == "__main__":
    main()