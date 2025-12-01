# Nguyễn Bá Chung, mssv 245752021610143
"""Viết chương trình sử dụng thư viện NumPy để tạo một mảng với các giá trị nằm
trong khoảng từ 12 đến 38"""

import numpy as np # gọi thư viện xử lý mảng
# đầu vào
a = int(input('nhập a từ bàn phím: '))
b = int(input('nhập b từ bàn phím: '))
# mảng với giá trị nằm trong khoảng a,b
mp = np.arange(a,b) #tạo mảng từ a đến b
# in ra kết quả
print('Mảng có giá trị từ {0} đến {1} là: '.format(a,b ))
print(mp)