#Bài 1: Yêu cầu: Yêu cầu người dùng nhập vào một số trong khoảng từ 1 đến 9, sau đó hiển thị bảng cửu chương của số đó từ 1 đến 9.
try:
    n = int(input("Vui lòng nhập một số từ 1-9: "))
    if 1 <= n <= 9:
        for i in range(1, 10):
            print(f"{n} x {i} = {n * i}")
    elif n<1 or n>9:
        print("Số bạn vừa nhập ko hợp lệ, số phải từ 1-9.")
except:
    print("Bạn vừa nhập một string, bạn phải nhập số nguyên")