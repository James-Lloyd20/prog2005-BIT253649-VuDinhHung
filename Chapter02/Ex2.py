#Bài 2: Yêu cầu: Yêu cầu người dùng nhập vào một số dương và kiểm tra xem số đó có phải là số nguyên tố hay không.
n = int(input("Vui lòng nhập một s nguyên dương: "))
if n < 2:
    print(f"Số {n} không phải là một số nguyên tố")
else:
    so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(f"Số {n} chính là số nguyên tố")
    else:
        print(f"Số {n} không phải là số nguyên tố")