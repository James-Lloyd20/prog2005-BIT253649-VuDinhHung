# Bài 7: Yêu cầu: Tìm số lớn nhất trong ba số. Nhập ba số và in ra số lớn nhất

a = int(input("Vui long nhap so thu nhat: "))
b = int(input("Vui long nhap so thu hai: "))
c = int(input("Vui long nhap so thu ba: "))

if a >= b and a >= c:
    print("So lon nhat trong ba so la:", a)
elif b >= a and b >= c:
    print("So lon nhat trong ba so la:", b)
else:
    print("So lon nhat trong ba so la:", c)