''' Bài 5: Yêu cầu: Khai báo, xử lý và hiển thị thông tin cá nhân
•	Tạo các biến name, age và average_score
•	Sử dụng hàm type() để hiển thị kiểu dữ liệu của từng biến
•	Tạo biến age_next_year bằng cách cộng 1 vào age, và doubled_score bằng cách nhân đôi average_score
•	In ra tất cả thông tin và kiểu dữ liệu của chúng
'''

name = "Vu Dinh Hung"
age = 18
average_score = 9
print(f'Kieu du lieu cua name: {type(name)}')
print(f'Kieu du lieu cua age: {type(age)}')
print(f'Kieu du lieu cua average_score: {type(average_score)}')

age_next_year = age + 1
doubled_score = average_score * 2
print(f'Ho va ten: {name}; Kieu du lieu: {type(name)}')
print(f'Tuoi cua nam sau: {age_next_year}; Kieu du lieu: {type(age_next_year)})')
print(f'Diem sau khi nhan doi: {doubled_score}; Kieu du lieu: {type(doubled_score)})')




