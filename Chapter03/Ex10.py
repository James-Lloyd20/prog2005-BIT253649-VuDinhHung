#Bài 10:
user_input = input("Vui lòng nhập danh sách số \n(các số được ngăn cách nhau bởi dấu cách) \nDanh sách: ")
numbers = [int(x) for x in user_input.split()]

even_numbers = [num for num in numbers if num % 2 == 0]
total_even = sum(even_numbers)
print("Các số chẵn trong danh sách là:", even_numbers)
print("Tổng các số chẵn trong danh sách là:", total_even)