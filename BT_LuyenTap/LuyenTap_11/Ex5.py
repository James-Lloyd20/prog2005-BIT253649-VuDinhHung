'''Viết chương trình kiểm tra một `key` có tồn tại trong dictionary hay không.
'''

thong_tin = {
    'ho_ten': 'Nguyen Van A',
    'chuyen_nganh': 'Maketing',
    'lop': 'N19'
}

ktr_key = input('Vui lòng nhập key bạn cần kiểm tra: ')

if ktr_key in thong_tin:
    print(f'Key mà bạn cần kiểm tra có trong dictionary')
else:
    print(f'Key bạn vừa nhập không có trong dictionary')