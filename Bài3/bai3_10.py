# Nguyễn Bá Chung, mssv 245752021610143
import math
def Tinh_ChuVi_DienTich():
    # 1. Nhập và kiểm tra tính hợp lệ của bán kính R
    while True:
            # Nhận giá trị nhập từ bàn phím
            R_input = input("Nhập bán kính R của hình tròn: ")
            # Chuyển đổi sang số thực (float)
            R = float(R_input)
            # Kiểm tra R phải là số dương
            if R <= 0:
                print("Lỗi: Bán kính phải là số dương.")
                continue 
            break   
    # Công thức Chu vi: C = 2 * pi * R
    chu_vi = 2 * math.pi * R    
    # Công thức Diện tích: S = pi * R^2
    dien_tich = math.pi * (R ** 2)   
    print('chu vi hinh tron la: ', round(chu_vi))
    print('dien tich hin tron la: ', round(dien_tich)) 
Tinh_ChuVi_DienTich()