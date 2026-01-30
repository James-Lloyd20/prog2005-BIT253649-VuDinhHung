# Bài 15: Yêu cầu: Nhập thông tin 3 sinh viên (Tên và điểm 3 môn - Toán, Lý, Hóa). In ra tên sinh viên, và điểm trung bình tương ứng.

for i in range(1, 4):
    print(f"VUI LONG NHAP THONG TIN SINH VIEN {i}")

    ten_sv = input("Ho va ten: ")
    toan = float(input("Toan: "))
    ly = float(input("Ly: "))
    hoa = float(input("Hoa: "))
    diem_tb = (toan + ly + hoa) / 3

    print(f"Sinh vien{i}: {ten_sv}; Diem trung binh la: {round(diem_tb, 2)}")