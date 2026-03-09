n = int(input('Vui lòng nhập cỡ của mảng: '))

arr = []
for i in range(n):
    num = int(input(f'Vui lòng nhập phần tử thứ {i + 1}: '))
    arr.append(num)

for i in range(n):
    max_index = i
    for j in range(i + 1, n):
        if arr[j] > arr[max_index]:
            max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    print(f'Kết quả sắp xếp mảng ở bước thứ {i + 1} là: {arr}')