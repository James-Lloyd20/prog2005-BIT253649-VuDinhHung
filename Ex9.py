# Bài 9: Yêu cầu: Kiểm tra đầu vào tuổi. Yêu cầu người dùng nhập tuổi. Kiểm tra xem tuổi có nằm trong khoảng 1 đến 120 không. In ra thông báo phù hợp.

age = int(input("Vui long nhap tuoi cua ban: "))
if age >= 1 and age <= 120:
    print("Tuoi cua ban hoan toan nam trong tu 1-120 tuoi")
elif age > 120 or age < 1:
    print("So tuoi ban vua nhap khong hop le (so nhap vao phai tu 1-120).")
else:
    print("Gia tri nhap vao khong hop le, phai la so nguyen")