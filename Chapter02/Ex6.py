#Bài 6: Yêu cầu: Viết một hàm đệ quy để tính giai thừa của một số do người dùng nhập vào.
def factorial(n):
    if n < 0:
        raise ValueError("Số nguyên âm không có giai thừa, vui lòng nhập số nguyên dương")
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Vui lòng nhập một số mà bạn muốn tính giai thừa: "))
print(f"Giai thừa của số {n} là: {factorial(n)}")