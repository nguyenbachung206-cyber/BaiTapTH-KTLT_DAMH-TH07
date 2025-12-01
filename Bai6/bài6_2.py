# Nguyễn Bá Chung, mssv 245752021610143
"""2. Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều
rộng. Class Hinhchunhat có method để tính diện tích."""

import math

# khai báo 1 lớp class mang tinh Hinhchunhat
class Hinhchunhat:
    def __init__(self,dai,rong):
        self.dai = dai     # thuộc tính chiều dài
        self.rong = rong   # thuộc tính chiều rộng

    def dientich(self):
        return self.dai * self.rong  # công thức tính diện tích: S=dai * rong

# đầu vào input cho chiều dài và rôngk
a = int(input('Nhập chiều dài a từ bàn phím: '))
b = int(input('nhập chiều rộng b từ bàn phím: '))   
# sử dụng class
hcn = Hinhchunhat(a,b)
print('Dien tich hinh chu nhat là:', hcn.dientich())