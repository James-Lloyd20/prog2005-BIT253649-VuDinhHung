# Bài 6: Yêu cầu: Kiểm tra một số chẵn. Viết một hàm is_even(n) trả về True nếu n là số chẵn, ngược lại trả về False.

def is_even(n):
    if n % 2 == 0:
        return True
    elif n % 2 != 0:
        return False

number1 = 14
number2 = 17
print(f'So {number1} co phai la so chan khong? {is_even(number1)}')
print(f'So {number2} co phai la so chan khong? {is_even(number2)}')