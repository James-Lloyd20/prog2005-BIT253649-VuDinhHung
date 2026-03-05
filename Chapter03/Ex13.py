#Bài 13:
s = input("Vui lòng nhập chuỗi bạn cần kiểm tra: ")
if s == s[::-1]:
    print("Chuỗi bạn vừa nhập là đối xứng")
else:
    print("Chuỗi bạn vừa nhập không phải là đối cứng")