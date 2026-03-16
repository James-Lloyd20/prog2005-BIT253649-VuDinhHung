'''Viết chương trình tính chỉ số cơ thể BMI'''

cannang = float(input('Vui lòng nhập số cân nặng của bạn (KG): '))
chieucao = float(input('Vui lòng nhập số chiều cao của bạn (M): '))
bmi = cannang / (chieucao * chieucao)
print(f'Chỉ số cơ thể BMI của bạn là: {bmi:.2f}')