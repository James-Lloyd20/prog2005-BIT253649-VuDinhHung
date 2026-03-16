'''
Tạo đối tượng Person có thuộc tính name và age, có class method tạo đối tượng Person từ chuỗi "name-age" 
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split('-')
        return cls(name, int(age))
    
def main():
    person1 = Person.from_string('James-18')
    print(f'Tên: {person1.name} \nTuổi: {person1.age}')
if __name__ == "__main__":
    main()