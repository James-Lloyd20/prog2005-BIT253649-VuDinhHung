#Bài 14:
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    # Chuyển về chữ thường để đếm không phân biệt hoa thường (slide 42)
    s_lower = s.lower()
    for char in s_lower:
        if char in vowels:
            count += 1
    return count

text = input("Vui lòng nhập chuỗi bạn muốn kiểm tra: ")
print(f"Số lượng nguyên âm tìm thấy là: {count_vowels(text)}")