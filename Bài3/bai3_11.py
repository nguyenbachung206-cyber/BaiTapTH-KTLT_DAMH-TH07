# Nguyễn Bá Chung, mssv 245752021610143
def benefit(t, n, k):
    return n * (1 + t/100) **k
t = float(input('nhập lãi suất (%/tháng): '))
n = float(input('nhập số vốn ban đầu: '))
k = int(input('nhập số tháng gửi: '))

tong_tien = benefit(t, n, k)
print('số tiền nhận được sau {k} tháng là: ', float(tong_tien))