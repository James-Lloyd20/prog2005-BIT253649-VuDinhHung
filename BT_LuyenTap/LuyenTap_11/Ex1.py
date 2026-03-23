'''
Nhập 5 chuỗi bất kỳ từ bàn phím, sử dụng insertion sort để sắp xếp đồ dài các chuỗi theo thứ tự giảm dần. 
In ra màn hình từng bước sắp xếp. 
'''

def insertion_sort(arr):
    num = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
        num = num + 1
        print(f'Bước sắp xếp thứ {num}: {arr}')

user_input = input('Vui lòng nhập 5 chuỗi bất kì từ bàn phím (ngăn cách nhau bởi dấu phẩy): ')
arr = [s.strip() for s in user_input.split(',')]
insertion_sort(arr)
print(f'Kết quả sau khi đã sắp xếp giảm dần là:\n{arr}')