'''
Viết hàm count_vowels(s) để đếm số lượng nguyên âm (a, e, i, o, u) xuất hiện trong một chuỗi, không 
phân biệt chữ hoa hay chữ thường
'''

def count_vowels(s):
    count = 0
    vowels = 'ueoaiUEOAI'
    for char in s:
        if char in vowels:
            count += 1
    return count

user_input = input('Vui lòng nhập một chuỗi: ')
print(f'Số lượng nguyên âm trong chuỗi là: {count_vowels(user_input)}')