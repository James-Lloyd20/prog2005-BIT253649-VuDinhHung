#Bài 13: Yêu cầu: Viết chương trình sử dụng while để yêu cầu người dùng nhập mật khẩu cho đến khi đúng từ khóa “python123”
mat_khau_goc = "python123"
mat_khau = ""
while mat_khau != mat_khau_goc:
    mat_khau = input("Vui lòng nhập mật khẩu của bạn vào đây: ")
    if mat_khau == mat_khau_goc:
        print("Mật khẩu chính xác")
        break
    else:
        print("Mật khẩu bạn vừa nhập chưa chính xác, vui lòng nhập lại")