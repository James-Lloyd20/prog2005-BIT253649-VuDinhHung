''' Bài 12:
Yêu cầu: Tính BMI (Chỉ số khối cơ thể)
Viết một chương trình tính và hiển thị BMI:
•	Nhập cân nặng (kg) và chiều cao (m)
•	Công thức: BMI = weight / (height * height), sử dụng kiểu float và các toán tử số học.
•	Hiển thị BMI làm tròn 2 chữ số thập phân
•	Ví dụ: nếu weight = 60kg và height = 1.65m → BMI ≈ 22.04
'''

print("Luu y: dau phay phai duoc thay bang dau cham (.)")
can_nang = float(input("Vui long nhap so can nang (kg): "))
chieu_cao = float(input("Vui long nhap so chieu cao (m): "))
bmi = can_nang / (chieu_cao * chieu_cao)
bmi_rounded = round(bmi, 2)

print(f"Chi so khoi co the BMI cua ban la: {bmi_rounded}")