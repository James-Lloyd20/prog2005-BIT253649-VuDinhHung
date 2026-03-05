#Bài 11:
arr = [15, 3, 9, 25, 1, 8]

if not arr:
    print("Mảng rỗng không có giá trị")
else:
    max_val = arr[0]
    min_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x

    print(f"Giá trị lớn nhất: {max_val}")
    print(f"Giá trị nhỏ nhất: {min_val}")