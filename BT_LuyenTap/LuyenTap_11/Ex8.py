'''
Tạo một tuple chứa thông tin sinh viên gồm: `tên`, `tuổi`, `điểm trung bình`. In ra từng giá trị bằng cách unpack tuple.
'''

thong_tin_sv = ('James', 19, 1.3)

print(f'Tuple ban đầu: {thong_tin_sv}')
ten, tuoi, diem_tb = thong_tin_sv

print(f'Tên của sinh viên là: {ten}')
print(f'Tuổi: {tuoi}')
print(f'Điểm trung bình: {diem_tb}')