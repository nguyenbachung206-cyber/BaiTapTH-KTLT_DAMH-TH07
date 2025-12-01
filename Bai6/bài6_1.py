# Nguyễn Bá Chung, mssv 245752021610143
"""1. Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có
một method có thể tính diện tích.
"""
import math
# khai báo 1 lớp class mang tên Circle
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi *( self.radius ** 2) # 𝑆 = pi * (r **2)
    
r = int(input('nhập n từ bàn phím: '))
aCircle = Circle(r) # tạo 1 đói tượng có bán kính n
print(aCircle.area())  #gọi công thức area() tính S