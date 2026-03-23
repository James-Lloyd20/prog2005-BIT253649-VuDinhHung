'''
- Nhập tên và tuổi từ bàn phím 
- Lưu thông tin trên thông qua Dict với key là tên và value là tuổi. 
- Tính tuổi trung bình 
'''

thong_tin = {}

print('Vui lòng nhập thông tin sau để tính tuổi trung binh (gõ 0 để thoát và tính TB)')
while True:
    ten = input('Vui lòng nhập Họ và Tên: ').strip()
    if ten == '0':
        break
    tuoi_str = input(f'Vui lòng nhập tuổi của {ten}: ').strip()
    tuoi = int(tuoi_str)
    thong_tin[ten] = tuoi
    print(f'Đã lưu: {ten} - {tuoi} tuổi')

if len(thong_tin) > 0:
    print(f'Thông tin của danh sách hiện tại là: {thong_tin}')
    tong_tuoi = 0
    for i in thong_tin.values():
        tong_tuoi += i
    tuoi_trung_binh = tong_tuoi / len(thong_tin)
    
    print(f'Số tuổi trung bình của cả nhóm là: {tuoi_trung_binh}')
else:
    print('Bạn chưa nhập thông tin của ai cả')