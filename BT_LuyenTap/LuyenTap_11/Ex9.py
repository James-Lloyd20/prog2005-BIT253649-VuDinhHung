def nhap_ma_tran(ten_ma_tran, so_hang, so_cot):
    print(f"Nhập dữ liệu cho ma trận {ten_ma_tran}")
    ma_tran = []
    
    for i in range(so_hang):
        hang = []
        for j in range(so_cot):
            gia_tri_nhap = input(f"Nhập phần tử [{i}][{j}]: ").strip()
            if gia_tri_nhap == "":
                raise ValueError("Lỗi: Bạn vừa nhập vào một giá trị trống")
            hang.append(int(gia_tri_nhap))
        ma_tran.append(hang)
    return ma_tran

try:
    print("CHƯƠNG TRÌNH CỘNG 2 MA TRẬN")
    so_hang_str = input("Nhập số hàng của ma trận: ").strip()
    so_cot_str = input("Nhập số cột của ma trận: ").strip()
    if so_hang_str == "" or so_cot_str == "":
        raise ValueError("Lỗi: Kích thước ma trận không được để trống")
    so_hang = int(so_hang_str)
    so_cot = int(so_cot_str)
    ma_tran_A = nhap_ma_tran("A", so_hang, so_cot)
    ma_tran_B = nhap_ma_tran("B", so_hang, so_cot)
    ma_tran_C = []
    for i in range(so_hang):
        hang_ket_qua = []
        for j in range(so_cot):
            tong = ma_tran_A[i][j] + ma_tran_B[i][j]
            hang_ket_qua.append(tong)
        ma_tran_C.append(hang_ket_qua)
    print("KẾT QUẢ: MA TRẬN C (A + B)")
    for hang in ma_tran_C:
        print(hang)
except ValueError as e:
    print(f"\n[!] THÔNG BÁO: {e}")