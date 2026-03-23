'''
- Khởi tạo một danh sách các số nguyên
- Thêm phần tử vào danh sách
- Nhập giá trị k và kiểm tra số lần xuất hiện của nó trong danh sách
- Tính tổng tất cả các số nguyên tố trong danh sách
- Sắp xếp danh sách
- Xóa danh sách
'''

danh_sach = [5, 8, 3, 9, 1]
print(f'Danh sách ban đầu là: ')

danh_sach.append(6)
danh_sach.append(2)
print(f'Danh sách sau khi đã được thêm phần tử là: {danh_sach}')

k = int(input('Vui lòng nhập 1 giá trị mà bạn muốn kiểm tra số lần xuất hiện: '))
count_xuathien = danh_sach.count(k)
print(f'Giá trị {k} xuất hiện {count_xuathien} trong danh sách')

def ktr_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

tong_nguyen_to = 0
for so in danh_sach:
    if ktr_nguyen_to(so):
        tong_nguyen_to += so
print(f'Tổng của các số nguyên tố trong danh sách là: {tong_nguyen_to}')

danh_sach.sort()
print(f'Kết quá danh sách sau khi đã được sắp xếp tăng dần là: {danh_sach}')

danh_sach.clear()
print(f'Kết quả danh sách sau khi đã bị xóa là: {danh_sach}')