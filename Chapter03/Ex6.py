#Bài 6:

def bubble_sort_count(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
                swapped = True
        if not swapped:
            break
    print(f"Số lần sắp xếp: {swap_count}")

arr_int = [90, 35, 55, 26, 36, 18, 99]
bubble_sort_count(arr_int)
print("Danh sách sau khi đã sắp xếp:", arr_int)