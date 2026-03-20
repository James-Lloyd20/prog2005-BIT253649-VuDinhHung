'''
**Yêu cầu**: Subplots
- Tạo một Figure gồm 1 hàng, 2 cột
- Subplot bên trái: vẽ đồ thị y=x^2
- Subplot bên phải: vẽ đồ thị y=sqrt(x)
- Thêm tiêu đề và nhãn cho từng subplot
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, y1, color='blue')
ax1.set_title('Đồ thị y = x^2')
ax1.set_xlabel('Trục x')
ax1.set_ylabel('Trục y')

ax2.plot(x, y2, color='red')
ax2.set_title('Đồ thị y = sqrt(x)')
ax2.set_xlabel('Trục x')
ax2.set_ylabel('Trục y')

plt.tight_layout()
plt.show()