# Bài 3: Yêu cầu: Thực hiện các phép toán cơ bản với hai số. Nhập hai số nguyên từ người dùng. Tính và in ra tổng, hiệu, tích và thương của chúng

num1 = int(input('Vui long nhap so nguyen dau tien: '))
num2 = int(input('Vui long nhap so nguyen thu hai: '))

tong = num1 + num2
hieu = num1 - num2
tich = num1 * num2
thuong = num1 / num2

print(f'Tong = {tong}')
print(f'Hieu = {hieu}')
print(f'Tich = {tich}')
print(f'Thuong = {thuong}')
