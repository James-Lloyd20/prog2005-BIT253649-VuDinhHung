print('=== Các số lẻ từ 17 - 111 theo thứ tự giảm dần là ===')
for i in range(111, 16, -1):
    if i % 2 != 0:
        print(i)

print('=== Các số nguyên tố trong khoảng từ 17 - 111 là ===')
for i in range(17, 112):
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i)