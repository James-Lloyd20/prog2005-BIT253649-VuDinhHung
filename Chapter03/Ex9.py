#Bài 9:
user_input = input("Vui lòng nhập danh sách số \n(các số được ngăn cách nhau bởi dấu cách) \nDanh sách: ")
numbers = [int(x) for x in user_input.split()]

odd_numbers = [num for num in numbers if num % 2 != 0]
print("Các số lẻ:", odd_numbers)