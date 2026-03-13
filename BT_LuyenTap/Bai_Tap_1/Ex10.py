'''
Quản lý sản phẩm - Tệp văn bản
• Viết chương trình nhập thông tin sản phẩm gồm:
• Mã sản phẩm (Code): kiểu chuỗi (String)
• Tên sản phẩm (Name): kiểu chuỗi (String)
• Giá (Price): kiểu số (Number)

Mỗi sản phẩm sau khi nhập thành công sẽ được nối thêm (append) vào tệp theo định dạng:
ProductCode;ProductName;Price

Ví dụ dữ liệu trong tệp sau khi thêm:
sv1;Cocacolala;15.5
sp2;Bưởi 5 Roi;18.0
sp3;Bia 333;14.5

Chương trình cần thực hiện hai chức năng chính:
• Hiển thị danh sách sản phẩm từ tệp.
• Sắp xếp sản phẩm theo giá giảm dần và hiển thị kết quả.
'''

import os
def add_product():
    code = input('Vui lòng nhập mã sản phẩm: ')
    name = input('Vui lòng nhập tên sản phẩm: ')
    price = float(input('Vui lòng nhập giá sản phẩm: '))
    
    with open('products.txt', 'a') as file:
        file.write(f'{code};{name};{price}\n')
    print('Sản phẩm đã được thêm thành công')

def display_products():
    if not os.path.exists('products.txt'):
        print('Chưa có sản phẩm nào được thêm vào')
        return
    
    with open('products.txt', 'r') as file:
        products = [line.strip().split(';') for line in file]
    
    print('Danh sách sản phẩm là:')
    for code, name, price in products:
        print(f'Code: {code}, Name: {name}, Price: {price}') 

def sort_products_by_price():
    if not os.path.exists('products.txt'):
        print('Chưa có sản phẩm nào được thêm vào')
        return
    
    with open('products.txt', 'r') as file:
        products = [line.strip().split(';') for line in file]
    
    products.sort(key=lambda x: float(x[2]), reverse=True)
    
    print('Danh sách sản phẩm đã được sắp xếp theo giá giảm dần là:')
    for code, name, price in products:
        print(f'Code: {code}, Name: {name}, Price: {price}')

while True:
    print('\n==== VUI LÒNG CHỌN ====')
    print('1. Thêm sản phẩm mới')
    print('2. Hiển thị danh sách sản phẩm')
    print('3. Sắp xếp sản phẩm theo giá giảm dần')
    print('4. Thoát')
    
    choice = input('Vui lòng chọn một chức năng bạn muốn thực hiện (1-4): ')
    
    if choice == '1':
        add_product()
    elif choice == '2':
        display_products()
    elif choice == '3':
        sort_products_by_price()
    elif choice == '4':
        print('Đang thoát...')
        break
    else:
        print('Bạn vừa nhập lựa chọn không hợp lệ, vui lòng nhập lại')