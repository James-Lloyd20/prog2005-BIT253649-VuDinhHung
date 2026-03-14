'''
Viết hàm nhận vào một tuple các số nguyên và trả về:
• Tổng
• Giá trị lớn nhất
• Giá trị nhỏ nhất
'''

def tuple(numbers):
    tong = sum(numbers)
    max_value = max(numbers)
    min_value = min(numbers)
    return tong, max_value, min_value

# Test
numbers = (5, 7, 9, 3, 6, 8)
ketqua = tuple(numbers)
print(f'Tổng: {ketqua[0]} \nGiá trị lớn nhất: {ketqua[1]} \nGiá trị nhỏ nhất: {ketqua[2]}')