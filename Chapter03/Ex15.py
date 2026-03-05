#Bài 15:
s = input("Nhập chuỗi cần đảo ngược: ")

reversed_slicing = s[::-1]
print(f"Đảo ngược chuỗi bằng kĩ thuật 'Slicing': {reversed_slicing}")

reversed_loop = ""
for i in range(len(s) - 1, -1, -1): # Duyệt ngược từ cuối về đầu
    reversed_loop += s[i]
print(f"Đảo ngược chuỗi không sử dụng kĩ thuật 'Slicing': {reversed_loop}")