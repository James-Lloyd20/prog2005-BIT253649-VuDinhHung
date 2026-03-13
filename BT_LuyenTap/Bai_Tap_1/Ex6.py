'''
Tách và xử lý chuỗi. Cho một chuỗi như "`5; 7; 8; -2; 8; 11; 13; 9; 10`" (có thể nhập từ bàn phím):
- In từng số trên một dòng riêng
- In ra có bao nhiêu số chẵn
- In ra có bao nhiêu số âm
- In ra có bao nhiêu số nguyên tố
- Tính và in giá trị trung bình
'''

user_input = input('Vui lòng nhập vào 1 chuỗi số được cách nhau bởi dấu ";": ')
str_number = user_input.split(';')
numbers = [int(num.strip()) for num in str_number]
print('Các số đã được nhập là: ')
for num in numbers:
    print(num)

so_chan = sum(1 for num in numbers if num % 2 == 0)
print(f'Trong chuỗi đã nhập có {so_chan} số là số chẵn')

so_am = sum(1 for num in numbers if num <0)
print(f'Trong chuỗi đã nhập có {so_am} số là số âm')

def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
dem_so_nguyen_to = sum(1 for num in numbers if so_nguyen_to(num))
print(f'Trong chuỗi đã nhập có {dem_so_nguyen_to} số là số nguyên tố')

gtr_tb = sum(numbers) / len(numbers)
print(f'Giá trị trung bình của các số đã được nhập trong string là: {gtr_tb}')