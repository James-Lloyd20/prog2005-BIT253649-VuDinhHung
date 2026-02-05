#Bài 3:
n = int(input("Vui lòng nhập số n: "))
if n <= 0:
    print("Số n bạn nhập bắt buộc phải > 0")
else:
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        sothu_n = a + b
        a = b
        b = sothu_n
        count += 1