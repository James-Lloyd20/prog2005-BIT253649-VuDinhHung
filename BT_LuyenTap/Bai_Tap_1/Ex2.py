'''
Viết chương trình nhập hai số, tính các giá trị: lũy thừa, căn bậc 2, 
chia lấy phần nguyên, chia lấy phần dư, làm tròn số. '''

num1 = float(input('Vui lòng nhập số thứ nhất: '))
num2 = float(input('Vui lòng nhập số thứ hai: '))

luy_thua = num1 ** num2
print(f'Lũy thừa của {num1} và {num2} là: {luy_thua}')

can_bac2_1 = num1 ** 0.5
can_bac2_2 = num2 ** 0.5
print(f'Căn bậc 2 của {num1} là: {can_bac2_1} \n Căn bậc 2 của {num2} là: {can_bac2_2}')

chialayphannguyen = num1 // num2
print(f'Chia lấy phần nguyên của {num1} và {num2} là: {chialayphannguyen}')

chialayphandu = num1 % num2
print(f'Chia lấy phần dư của {num1} và {num2} là: {chialayphandu}')

lamtronso = round(num1 / num2)
print(f'Làm tròn số của {num1} chia cho {num2} là: {lamtronso}')