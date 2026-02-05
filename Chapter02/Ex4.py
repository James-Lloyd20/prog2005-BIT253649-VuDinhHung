#Bài 4: Yêu cầu: Yêu cầu người dùng nhập vào một số và tính tổng các chữ số của số đó.
try:
    n = int(input("Vui lòng nhập vào một số: "))
    if n < 0:
        n = n * -1
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    print(f"Tổng các chữ số trong số được nhập là: {tong}")
except ValueError:
    print("Dữ liệu input ko hợp lệ, bạn phải nhập chữ số")
