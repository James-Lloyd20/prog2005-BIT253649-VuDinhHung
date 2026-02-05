#Bài 7: Yêu cầu: Yêu cầu người dùng nhập vào hai số nguyên dương và tính ước số chung lớn nhất của chúng bằng cách sử dụng vòng lặp.
try:
    a = int(input("Vui lòng nhập số nguyên dương a: "))
    b = int(input("Vui lòng nhập số nguyên dương b: "))
    if a <= 0 or b <= 0:
        print("Vui lòng nhập số nguyên dương")
    else:
        while b != 0:
            a, b = b, a % b
        print(f"Ước số chung lớn nhất là: {a}")
except:
    print("Dữ liệu input ko hợp lệ")