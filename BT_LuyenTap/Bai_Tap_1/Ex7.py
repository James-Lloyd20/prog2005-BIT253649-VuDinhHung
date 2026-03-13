'''
Tạo lớp `Student` có `tên` và `điểm`. Khởi tạo 2 đối tượng sinh viên khác nhau.
'''

class Student:
    def __init__(stu, name, score):
        stu.name = name
        stu.score = score

stu1 = Student('Alex', 8)
stu2 = Student('Sander', 9)
print(f'=== SINH VIÊN 1 === \n Tên: {stu1.name} \n Điểm: {stu1.score}')
print(f'=== SINH VIÊN 2 === \n Tên: {stu2.name} \n Điểm: {stu2.score}')