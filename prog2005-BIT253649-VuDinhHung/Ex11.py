# Bài 11: Yêu cầu: Chuyển độ C sang độ F Viết một chương trình chuyển nhiệt độ từ độ C sang độ F. Yêu cầu người dùng nhập nhiệt độ theo độ C (kiểu float). Sử dụng công thức: F = C × 9/5 + 32. In kết quả ra dạng chuỗi định dạng.

do_c = float(input("Vui long nhap nhiet do (do C): "))
do_f = do_c * 9/5 + 32

print(f"{do_c} do C = {do_f} do F")