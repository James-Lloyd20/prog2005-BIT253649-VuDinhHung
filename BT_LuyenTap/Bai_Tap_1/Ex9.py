'''
Thêm phương thức `display()` vào lớp `Student` để in thông tin theo format: "Sinh viên A có điểm là 10"
'''

class Student:
    def __init__(stu, name, score):
        stu.name = name
        stu.score = score
        
    def display(stu):
        print(f'Sinh viên {stu.name} có điểm là {stu.score}')