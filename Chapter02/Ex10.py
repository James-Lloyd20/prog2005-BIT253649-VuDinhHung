#Bài 10: Yêu cầu: Viết một hàm đệ quy để tính tổng của tất cả các số nguyên từ 1 đến n, trong đó n được nhập bởi người dùng.
try:
    def tinh_tong(n):
        if n == 1:
            return 1
        return n + tinh_tong(n - 1)
    n = int(input("Vui lòng nhập một số 'n': "))
    if n <= 0:
        print("Số bạn nhập vào ko hợp lệ, số nhập vào phải lớn hơn/bằng 1")
    elif n >= 1:
        print(f"Tổng của tất cả các số nguyên bạn nhập vào là: {tinh_tong(n)}")
except ValueError:
    print("Dữ liệu mà bạn nhập vào không hợp lệ")