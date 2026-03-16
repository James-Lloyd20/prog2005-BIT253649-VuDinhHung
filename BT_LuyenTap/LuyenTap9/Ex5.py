'''
Tạo lớp `User`, có thuộc tính id. Sử dụng `property` để chỉ cho phép đọc (read-only) thuộc tính id.
'''

class User:
    def __init__ (self, id):
        self._id = id

    @property
    def id(self):
        return self._id

def main():
    user1 = User(123456)
    print(f"ID là: {user1.id}")
    try:
        user1.id = 789000
    except AttributeError as e:
        print(f"Lỗi: ID không thể thay đổi được - {e}")
if __name__ == "__main__":
    main()