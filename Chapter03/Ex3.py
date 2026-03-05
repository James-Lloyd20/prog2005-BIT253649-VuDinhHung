#Bài 3:
colors = ["Red", "Blue", "Black", "Gray", "Purple"]

try:
    colors.remove("Green")
except ValueError:
    print("Lỗi: Màu 'Green' không có trong danh sách")

print("Danh sách sau thao tác:", colors)