'''
Yêu cầu: Biểu đồ Cột Ngang - Xếp hạng Diện tích Thành phố Viết chương trình hiển thị 
Top 10 thành phố lớn nhất theo diện tích ở California bằng biểu đồ cột ngang

Gợi ý:
• Sử dụng cột area_total_km2
• Sắp xếp dữ liệu theo diện tích giảm dần
• Dùng plt.barh()
'''

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:\Data\Python\Class_Project\Homework\Chapter_5\california_cities.csv')
df_sorted = df.sort_values(by='area_total_km2', ascending=False)
top_10 = df_sorted.head(10)
top_10 = top_10.sort_values(by='area_total_km2', ascending=True)
ten_tp = top_10['city']
dien_tich = top_10['area_total_km2']

plt.barh(ten_tp, dien_tich, color='orange')
plt.title('Top 10 thành phố lớn nhất theo diện tích ở California')
plt.xlabel('Diện tích (km2)')
plt.ylabel('Tên của các thành phố')
plt.show()
