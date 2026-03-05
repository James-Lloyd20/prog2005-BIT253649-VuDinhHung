#Bài 8:
user_input = input("Vui lòng nhập danh sách số (được cách nhau bởi dấu cách): ")
numbers = [float(x) for x in user_input.split()]
found = False

for num in numbers:
    if num > 10:
        print(f"Số đầu tiên lớn hơn 10 trong danh sách là: {num}")
        found = True
        break

if not found:
    print("Không có số nào lớn hơn 10 trong danh sách")