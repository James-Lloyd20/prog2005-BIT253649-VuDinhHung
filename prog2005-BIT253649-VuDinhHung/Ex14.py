# Bài 14: Yêu cầu: Nhập một số và tính căn bậc hai của nó. Nếu số nhập vào âm, hiển thị thông báo lỗi.

try:
    number = float(input("Vui long nhap so ma ban muon tinh can bac hai: "))
    if number < 0:
        print("So ma ban muon tinh can bac hai phai la so nguyen duong")
    else:
        can_bac_hai = number ** 0.5
        print(f"Dap an can bac hai cua {number} la: {can_bac_hai}")
except ValueError:
    print("Loi: vui long nhap so nguyen duong hop le")