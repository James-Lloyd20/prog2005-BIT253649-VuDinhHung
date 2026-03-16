'''
Viết chương trình chuẩn hóa tên người dùng: Loại bỏ khoảng trắng thừa ở hai đầu, 
giữa các từ chỉ để lại một khoảng trắng và viết hoa chữ cái đầu mỗi từ.'''

name = input('Vui lòng nhập tên người dùng: ')
name = name.strip()
name = ' '.join(name.split())
name = name.title()
print(f'Tên người dùng sau khi chuẩn hóa là: {name}') 