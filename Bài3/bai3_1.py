# Nguyễn Bá Chung, mssv 245752021610143
#1. Viết hàm sum() tính tổng hai số
def tinh_tong(a , b):
    """hàm nhận 2 giá trị là a và b và trả về giá trị tổng"""
    tong = a + b
    return tong

# biến đầu vào của a và b\
a = int(input('nhap tu ban phim a = '))
b = int(input('nhap tu ban phim b = '))
# gọi hàm để tính tổng
ket_qua = tinh_tong(a,b)
# in kết quả ra màn hình
print('tổng của 2 số là: ',ket_qua)



