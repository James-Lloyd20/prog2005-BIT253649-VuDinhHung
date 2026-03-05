#Bài 4:
numbers = [9, 2, 8, 5, 6, 5]
print("Danh sách gốc:", numbers)

numbers.sort()
print("Danh sách sắp xếp theo thứ tự tăng dần: \n", numbers)

numbers.reverse()
print("Danh sách sắp xếp theo thứ tự đảo ngược: \n", numbers)

solan_xh = numbers.count(5)
print(f"Số 5 xuất hiện {solan_xh} lần")