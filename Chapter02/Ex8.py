#Ba 8: Yêu cầu: Yêu cầu người dùng nhập vào một số dương và đảo ngược các chữ số của nó (ví dụ: nhập 1234 → xuất ra 4321).
n = int(input("Vui lòng nhập một số dương: "))
dao_nguoc = 0
while n > 0:
    num = n % 10
    dao_nguoc = dao_nguoc * 10 + num
    n //= 10
print(f"Kết quả sau khi đảo ngược là: {dao_nguoc}")