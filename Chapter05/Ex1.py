'''
Yêu cầu: Biểu đồ cột
• Một lớp có kết quả học tập như sau: Xuất sắc: 6, Giỏi: 10, Trung bình: 12, Yếu: 4, Kém: 1
• Vẽ biểu đồ cột thể hiện dữ liệu trên
• Thêm tiêu đề và nhãn cho các trục
'''

import matplotlib.pyplot as plt
xep_loai = ['Xuất sắc', 'Giỏi', 'Trung bình', 'Yếu', 'Kém']
score_xeploai = [6, 10, 12, 4, 1]

plt.bar(xep_loai, score_xeploai, color='skyblue')
plt.title('Biểu đồ về k quả học tập của lớp')
plt.xlabel('Xếp loại học sinh')
plt.show()