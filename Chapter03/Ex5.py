#Bài 5:
input_str = input("Vui lòng nhập các số thực cách nhau bởi dấu phẩy \n(VD: 2.3, 5.6, 8.9)\nDanh sách:")

try:
    arr_float = [float(x.strip()) for x in input_str.split(",")]

    def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    insertion_sort(arr_float)
    print("Kết quả sau khi được sắp xếp giảm dần:", arr_float)

except ValueError:
    print("Lỗi: Vui lòng nhập đúng định dạng số thực được ngăn cách nhau bởi dấu phẩy!")