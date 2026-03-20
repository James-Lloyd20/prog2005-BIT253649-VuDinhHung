'''
**Yêu cầu**: Viết chương trình đảo ngược một chuỗi nhập từ bàn phím bằng vòng lặp
'''

chuoi = input('Vui lòng nhập vào 1 chuỗi bạn muốn đảo ngược: ')
chuoi_daonguoc = ''

for i in chuoi:
    chuoi_daonguoc = i + chuoi_daonguoc

print(f'Chuỗi sau khi được đảo ngược: {chuoi_daonguoc}')