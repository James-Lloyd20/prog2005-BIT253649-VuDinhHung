#Bài 14: Yêu cầu: Viết chương trình kiểm tra một số n có phải là số nguyên tố bằng cách sử dụng vòng lặp.
n = int(input("Vui lòng nhập vào một số: "))
so_nt = True
if n < 2:
    so_nt = False
else:
    for i in range(2, n):
        if n % i == 0:
            so_nt = False
            break
if so_nt:
    print(f"Số {n} là một số nguyên tố")
else:
    print(f"Số {n} không phải là một số nguyên tố")