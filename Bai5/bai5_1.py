# Nguyễn Bá Chung, mssv 245752021610143
# Bài 1: Sử dụng module. Định nghĩa một module toán học gọi là mymath và sử dụng module này từ một tập lệnh riêng biệt.

import mymath5_1   #gọi hàm mymat5_1.py vừa tạo để khởi chạy chương trình
# đầu vào của chương trình
a = int(input('nhập a từ bàn phím: '))
b = int(input('nhập b từ bàn phím: '))
x = float(input('nhập x từ bàn phím: '))
# in ra các kết quả
print ('tổng: ', mymath5_1.cong(a,b))
print ('hiệu: ', mymath5_1.tru(a,b))
print ('Nhân: ', mymath5_1.nhan(a,b))
print (' thương', mymath5_1.chia(a,b))
print ('mũ', mymath5_1.binh_phương(x))
