#Bài 9: Yêu cầu: Yêu cầu người dùng nhập vào một số nguyên dương 5 chữ số và tìm chữ số lớn nhất trong số đó.
n = int(input("Vui lòng nhập số có 5 chữ số: "))
so_max = 0
if n != 5:
    print("Vui lòng nhập đúng một số nguyên dương 5 chữ số")
if n < 10000 or n > 99999:
    print("Số bạn vừa nhập vào không phải số nguyên dương 5 chữ số")
elif n >= 10000 or n <= 99999:
    while n > 0:
        so = n % 10
        if so > so_max:
            so_max = so
        n //= 10
    print(f"Chữ số lớn nhất trong số nguyên dương {n} là: {so_max} ")