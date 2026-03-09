# Với n nhập từ bàn phím, in ra các hình tam giác (ví dụ với n = 5)

n = int(input('Vui lòng nhập số n mà bạn muốn tạo hình tam giác: '))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

n = int(input('Vui lòng nhập số của kí tự "*" mà bạn muốn tạo hình tam giác cho nó: '))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(1, i + 1):
        print('*', end=' ')
    print()