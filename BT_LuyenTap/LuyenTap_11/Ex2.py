'''
Từ các chuỗi ký tự đã được sắp xếp từ bài 1. Viết chương trình tìm kiếm sử dụng Binary search, 
Tìm kiếm 1 chuỗi bất kỳ (Nhập từ bàn phím) trong 5 chuỗi ở trên, trả về vị trí và in ra màn hình.
'''

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
    return -1



arr = ['9', '6', '5', '4', '2'] 
print(f'Arr của bài 1 là: {arr}')
target = input('Vui lòng nhập 1 chuỗi bạn đang cần tìm: ').strip()
vi_tri = binary_search(arr, target)

if vi_tri != -1:
    print(f'Chuỗi bạn đang cần tìm {target} nằm tại vị trí index {vi_tri}')
else:
    print(f'Chuỗi bạn vừa nhập {target} không có trong arr bạn muốn tìm')