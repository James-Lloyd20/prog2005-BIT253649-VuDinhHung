user_input = input("Nhập các số (cách nhau bởi dấu cách): ")
mang = []
for i in user_input.split():
    mang.append(int(i))

so_le = []
so_NT = []
for n in mang:
    if n % 2 != 0:
        so_le.append(n)
    la_snt = True
    if n < 2:
        la_snt = False
    else:
        for j in range(2, n): 
            if n % j == 0:
                la_snt = False
                break    
    if la_snt == True:
        so_NT.append(n)

print(f'Danh sách có {so_le} số lẻ và có {len(so_le)} số lượng số lẻ')
print(f'Danh sách có {so_NT} số nguyên tố')