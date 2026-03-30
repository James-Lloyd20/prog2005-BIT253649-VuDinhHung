'''
Viết hàm sắp xếp các phần tử của một dãy sử dụng thuật toán selection sort
'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

user_input = input('Vui lòng nhập 1 dãy số được ngăn cách nhau bởi dấu phẩy: ')
arr = list(map(int, user_input.split(',')))
print(f'Dãy số sau khi đã được sắp xếp là: {selection_sort(arr)}')