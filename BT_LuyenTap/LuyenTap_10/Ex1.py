'''
**Yêu cầu**: Trích xuất tên bài hát từ đường dẫn. Cho một chuỗi biểu thị đường dẫn đến tệp nhạc, ví dụ: `d:\\music\\muabui.mp3`, viết hai hàm:
- Hàm để trích xuất "muabui.mp3"
- Hàm để trích xuất "muabui"
**Lưu ý**: Đường dẫn có thể là bất kỳ đường dẫn bài hát nào, nên hàm phải trả về kết quả chính xác cho mọi đầu vào.
'''

def file_name(path):
    return path.split("\\")[-1]

def name(path):
    parts = path.split("\\")
    base_name = parts[-1].split(".")[0]
    return base_name

full_music_path = "d:\\music\\muabui.mp3"
print(file_name(full_music_path))
print(name(full_music_path))