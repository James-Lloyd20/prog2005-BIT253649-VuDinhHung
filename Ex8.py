# Bài 8: Yêu cầu: Hàm với đối số mặc định Viết một hàm greet(name="Student") in ra “Hello, Student!”. Gọi hàm có và không có đối số.

def greet(name="Student"):
    print(f"Hello, {name}!")

greet()
greet("Hung")