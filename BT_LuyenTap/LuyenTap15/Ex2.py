'''
Viết hàm với đối số mặc định Viết một hàm greet(name="Student") in ra “Hello, Student!”. 
Gọi hàm trong trường hợp có và không có đối số.
'''

def greet(name="Student"):
    return f'Hello, {name}!'

user_input = input('Vui lòng nhập tên: ')
print(greet())
print(greet(user_input))
