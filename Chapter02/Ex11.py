#Bài 11: Yêu cầu: Viết chương trình nhập điểm trung bình và in ra xếp loại: Giỏi (>=8), Khá (6.5 - 7.9), Trung bình (5.0 - 6.4), Yếu (<5)
diem_tb = float(input("Vui lòng nhập điểm trung bình: "))
if diem_tb >= 8:
    xep_hang = "Giỏi"
elif diem_tb >= 6.5 and diem_tb <= 7.9:
    xep_hang = "Khá"
elif diem_tb >= 5 and diem_tb <= 6.4:
    xep_hang = "Trung bình"
elif diem_tb < 5:
    xep_hang = "Yếu"
print(f"Điểm trung bình bạn vừa nhập vào xếp hạng {xep_hang}")