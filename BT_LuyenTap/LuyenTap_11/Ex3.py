'''
Viết chương trình nhận vào một danh sách số từ người dùng và in ra tất cả các số chẵn, 
đồng thời tính tổng của các số chẵn đó.
'''

input_user = input('Vui lòng nhập vào 1 danh sách số (được ngăn cách nhau bởi dấu phẩy: ')
list_chuoi = input_user.split(',')
list_so_chan = []
tong_so_chan = 0

for i in list_chuoi:
    so = float(i.strip())
    if so % 2 == 0:
        list_so_chan.append(so)
        tong_so_chan = tong_so_chan + so

print(f'Danh sách số chẵn ở list bạn vừa nhập là: {list_so_chan}')
print(f'Tổng của các số chẵn trong danh sách là {tong_so_chan}')