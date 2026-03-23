'''
- Nhập thông tin Nhân viên, tuổi, id
- Lưu thông tin vào file text
- Lưu thông tin vào file csv
- Chụp ảnh nội dung file vừa tạo
'''

import csv
import os

thu_muc_hien_tai = os.path.dirname(os.path.abspath(__file__))
duong_dan_txt = os.path.join(thu_muc_hien_tai, 'nhan_vien.txt')
duong_dan_csv = os.path.join(thu_muc_hien_tai, 'nhan_vien.csv')

ten = input('Vui lòng nhập tên nhân viên: ').strip()
tuoi = input('Vui lòng nhập tuổi: ').strip()
id_nv = input('Vui lòng nhập ID: ').strip()

with open(duong_dan_txt, 'w', encoding='utf-8') as f_txt:
    f_txt.write('THÔNG TIN NHÂN VIÊN\n')
    f_txt.write(f'ID  : {id_nv}\n')
    f_txt.write(f'Tên : {ten}\n')
    f_txt.write(f'Tuổi: {tuoi}\n')
print('Đã tạo và lưu thành công vào file "nhan_vien.txt"')

with open(duong_dan_csv, 'w', newline='', encoding='utf-8') as f_csv:
    writer = csv.writer(f_csv)
    writer.writerow(['ID', 'Tên', 'Tuổi'])
    writer.writerow([id_nv, ten, tuoi])
print('Đã tạo và lưu thành công vào file "nhan_vien.csv"')