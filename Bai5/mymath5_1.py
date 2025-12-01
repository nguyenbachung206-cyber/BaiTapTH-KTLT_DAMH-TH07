# Nguyễn bá chung: 245752021610143
# mymath.py
# module toán hc tự định nghĩa

def cong(a,b):
    # hàm cộng 2 số
    return a+b
def tru(a,b):
    # hàm trừ 2 số
    return a-b
def nhan(a,b):
    # hàm nhân 2 số
    return a*b
def chia(a,b):
    if b == 0:
        print('ko chia đc')
    # hàm chia 2 số
    return a / b 
def binh_phương(x):
    # hàm tính tổng
    return x ** 2