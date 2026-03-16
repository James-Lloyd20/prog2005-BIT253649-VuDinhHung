'''Xử lý chuỗi với các hàm cơ bản. Viết chương trình cho phép nhập một chuỗi. Chương trình phải xuất ra:
- Số lượng chữ cái in hoa
- Số lượng chữ cái in thường
- Số lượng chữ số
- Số lượng ký tự đặc biệt
- Số lượng ký tự khoảng trắng
- Số lượng nguyên âm
- Số lượng phụ âm
'''

string = input('Vui lòng nhập vào 1 chuỗi: ')
count_upper = 0
count_lower = 0
count_so = 0
count_KTDB = 0
count_space = 0
count_nguyenam = 0
count_phuam = 0

for i in string:
    if i.isupper():
        count_upper = count_upper + 1
    elif i.islower():
        count_lower = count_lower + 1
    elif i.isdigit():
        count_so = count_so + 1
    elif i.isspace():
        count_space = count_space + 1
    else:
        count_KTDB = count_KTDB + 1

nguyenam = "ueoaiUEOAI"
for i in string:
    if i in nguyenam:
        count_nguyenam = count_nguyenam + 1
    elif i.isalpha():
        count_phuam = count_phuam + 1

print('=== SAU KHI XỬ LÝ CHUỖI ===')
print(f'Số lượng chữ cái in hoa: {count_upper}')
print(f'Số lượng chữ cái in thường: {count_lower}')
print(f'Số lượng chữ số: {count_so}')
print(f'Số lượng ký tự đặc biệt: {count_KTDB}')
print(f'Số lượng ký tự khoảng trắng: {count_space}')
print(f'Số lượng nguyên âm: {count_nguyenam}')
print(f'Số lượng phụ âm: {count_phuam}')