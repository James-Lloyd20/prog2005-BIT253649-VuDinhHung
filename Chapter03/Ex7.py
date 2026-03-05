#Bài 7:
input_str = input("Vui lòng nhập danh sách các số (cách nhau bởi dấu cách): ")
try:
    user_list = [int(x) for x in input_str.split()]
    target = int(input("Vui lòng nhập số bạn muốn tìm index của nó: "))
    found_index = -1

    for i in range(len(user_list)):
        if user_list[i] == target:
            found_index = i
            break

    if found_index != -1:
        print(f"Số {target} được tìm thấy tại index: {found_index}")
    else:
        print(f"Số {target} không có trong danh sách")

except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng số nguyên!")