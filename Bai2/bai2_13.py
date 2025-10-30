# Nguyễn Bá Chung, mssv 245752021610143
#lm bài tập 13 Viết chương trình giải phương trình bậc 2
import math
a = int(input('nhập a vào từ bàn phím:  '))
b = int(input('nhập b vào từ bàn phím:  '))
c = int(input('nhập c vào từ bàn phím:  '))

# ax^2 + bx +c =0
if a != 0: #kiểm tra điều kiện  a khác 0
    detal = b**2 - 4 * a * c
    # xét các trường hợp detal
    if detal < 0:
        print('pt trên vô nghiệm')
    elif detal == 0:
        x = -b/ (2*a)
        print('pt có nghiệm kép là:  ', x)
    else:
        x1 = (-b + math.sqrt(detal)) / (2*a)
        x2 = (-b + math.sqrt(detal)) / (2*a)
        print('pt có 2 nghiệm x1={0},x2={1}'.format(x1,x2))
else:  # nếu a = 0 thì là pt bậc nhất và có nghiệm
    x3 = -c / b
    print('ko phải là phương trình bậc 2 thành bậc nhất và có nghiệm là:  ', x3)
