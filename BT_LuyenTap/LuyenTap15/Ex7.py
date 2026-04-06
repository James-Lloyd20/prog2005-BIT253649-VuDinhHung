'''
Tạo dictionary lưu tên sinh viên làm key và điểm số làm value. Viết hàm tính điểm trung bình của các sinh viên 
(Ví dụ: Nếu có 3 sinh viên thì sẽ tính tổng số điển chia cho 3).
'''

students = {
    'Nguyen Van A': 8,
    'Tran Thi B': 7,
    'Le Van C': 9
}

def diemTB(student_dict):
    tong = sum(student_dict.values())
    TB = tong / len(student_dict)
    return TB

print(f'Điểm trung bình của các sinh viên là: {diemTB(students):.2f}')