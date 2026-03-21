'''
Yêu cầu: Biểu đồ tròn (Pie Chart)
• Thể hiện phần trăm doanh số của 5 sản phẩm: A: 30%, B: 25%, C: 15%, D: 20%, E: 10%
• Vẽ biểu đồ tròn có kèm nhãn
'''

import matplotlib.pyplot as plt

san_pham = ['A', 'B', 'C', 'D', 'E']
phan_tram = [30, 25, 15, 20, 10]

plt.pie(phan_tram, labels=san_pham, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ về phần trăm doanh số của 5 sản phẩm')
plt.show()