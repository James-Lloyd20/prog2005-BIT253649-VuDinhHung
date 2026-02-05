#Bài 5: Yêu cầu: Yêu cầu người dùng nhập vào một chuỗi và một ký tự, sau đó đếm xem ký tự đó xuất hiện bao nhiêu lần trong chuỗi.
chuoi = input("Vui lòng nhập chuỗi mà bạn muốn đếm: ")
ki_tu = input("Vui lòng nhập kí tự bạn cần đếm: ")
if len(ki_tu) != 1:
    print("Bạn vừa nhập 2 kí tự cần tìm trở lên. Vui lòng chỉ nhập 1 kí tự")
else:
    count = 0
    for n in chuoi:
        if n == ki_tu:
            count += 1
    print(f"Kí tự '{ki_tu}' xuất hiện {count} lần trong chuỗi")