# Bài 13: Yêu cầu: Nhập hai số nguyên từ bàn phím và in ra kết quả phép chia của chúng. Xử lý chia cho 0 và dữ liệu không hợp lệ.

try:
    num1 = int(input("Vui long nhap so bi chia: "))
    num2 = int(input("Vui long nhap so chia: "))
    ket_qua = num1 / num2
    print(f"Dap an sau khi chia la: {ket_qua}")
except ZeroDivisionError:
    print("Loi: so nay khong the chia cho 0")
except ValueError:
    print("Loi: du lieu duoc nhap vao phai la so nguyen")