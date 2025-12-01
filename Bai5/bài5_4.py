# Nguyễn Bá Chung, mssv 245752021610143
"""Bài 4: Viết chương trình để tạo một mảng với các giá trị nằm trong khoảng từ 12 đến 38 
 và đảo ngược mảng đã tạo"""

# gọi thư viện xử lý mảng
import numpy as np
# đầu vào
a = int(input('nhập a từ bàn phím: '))
b = int(input('nhập b từ bàn phím: '))
# mảng với giá trị nằm trong khoảng a,b
mp = np.arange(a,b) #tạo mảng từ a đến b
# Đảo ngược mảng
arr_reversed = mp[::-1]  # đảo ngược mảng
print("\nMảng sau khi đảo ngược:")
print(arr_reversed)

