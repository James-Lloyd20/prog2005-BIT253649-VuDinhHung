'''
Yêu cầu: Nhiều đồ thị trên cùng một biểu đồ
• Vẽ 2 hàm số: y=x^2 (màu xanh), y=x^3 (màu đỏ)
• Hiển thị cả hai trên cùng một biểu đồ
• Thêm chú thích (legend) để phân biệt từng đường
'''

import matplotlib.pyplot as plt
x = []
y1 = []
y2 = []

for i in range(-10, 11):
    x.append(i)
    y1.append(i ** 2)
    y2.append(i ** 3)

plt.plot(x, y1, color='blue', label='y = x^2')
plt.plot(x, y2, color='red', label='y = x^3')
plt.legend()
plt.title('Đồ thị hàm số của y = x^2 và y = x^3')
plt.show()