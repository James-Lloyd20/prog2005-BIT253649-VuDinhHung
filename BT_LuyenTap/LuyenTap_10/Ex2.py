'''
**Yêu cầu**: Yêu cầu người dùng nhập vào một chuỗi và một ký tự, sau đó đếm xem ký tự đó xuất hiện bao nhiêu lần trong chuỗi.
'''

chuoi = input("Vui lòng nhập vào một chuỗi bạn muốn đếm: ")
ky_tu = input("Vui lòng nhập vào một ký tự bạn muốn đếm: ")
dem = chuoi.count(ky_tu)
print(f'Ký tự "{ky_tu}" xuất hiện {dem} lần trong chuỗi')