'''
Tạo dictionary lưu tên sinh viên làm key và điểm số làm value. 
Viết hàm tính điểm trung bình của các sinh viên 
(Ví dụ: Nếu có 3 sinh viên thì sẽ tính tổng số điển chia cho 3).
'''

def average_score(students):
    total = sum(students.values())
    average = total / len(students)
    return average

#Test
students = {
    'Alex': 9,
    'James': 7,
    'Anna': 8
    }
average = average_score(students)
print(f'Điểm trung bình của {len(students)} sinh viên là: {average}')