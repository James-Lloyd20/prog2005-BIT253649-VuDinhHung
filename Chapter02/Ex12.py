#Bài 12: Yêu cầu: Viết đoạn mã tính tổng các số lẻ từ 1 đến n bằng vòng lặp for.
n = int(input("Vui lòng nhập số bạn muốn tính tổng số lẻ: "))
tong = 0
for i in range(1, n + 1, 2):
    tong += i
print(f"Tổng của các số lẻ bạn vừa nhập là: {tong}")
