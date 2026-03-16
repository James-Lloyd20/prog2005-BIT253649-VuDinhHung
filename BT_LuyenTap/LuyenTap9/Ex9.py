'''
Tạo lớp `Animal` có thuộc tính name và phương thức sound() 
- Tạo lớp con `Dog` kế thừa và ghi đè phương thức `sound()` (Mô phỏng phương thức sound()  bằng hàm print() in ra một tiếng bất kỳ).
- Dùng super trong lớp con để khai khởi tạo tên
- Chạy thử bằng cách tạo một đối tượng của lớp Dog
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f'{self.name} phát ra âm thanh')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print(f'{self.name} sủa gâu gâu')

def main(): 
    dog1 = Dog('Vitamin gâu gâu')
    dog1.sound()
if __name__ == "__main__":    
    main()