#Bài 15: Yêu cầu: Tính tổng các chữ số của một số nguyên dương (ví dụ 123 -> 1+2+3=6) bằng vòng lặp while?
n = int(input("Vui lòng nhập số nguyên dương: "))
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(f"Tổng của các chữ số là: {tong}")