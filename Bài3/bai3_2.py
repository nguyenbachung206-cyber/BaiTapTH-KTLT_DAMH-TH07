# Nguyễn Bá Chung, mssv 245752021610143
# 2. Viết hàm sum() với kết quả trả về
#tạo hàm tính tổng
def sum(a,b):
    return ( a + b)
# biến vào
a = int(input('nhập a từ bàn phím:  '))
b = int(input('nhập b từ bàn phím:  '))
#Gọi hàm c để kết quả trả về c
c = sum(a , b)
print('tổng của 2 số là: ', c)