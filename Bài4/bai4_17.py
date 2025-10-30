# Nguyễn Bá Chung, mssv 245752021610143 
# bài 17: Nhập số n, in ra các số dương nhỏ hơn n có tổng các ước số lớn hơn chính nó.

n = int(input('nhập số nguyên dương từ bàn phím: '))
# Duyệt qua từng số từ 1 đến n-1
for i in range (1,n):
    tong = 0 #khai báo tổng ban đầu = 0 
    # Duyệt qua tất cả các số nhỏ hơn i để kiểm tra xem số nào là ước của i.
    for j in range(1,i): 
        if i % j == 0: # nếu i chia hết cho j thì đó là ước 
            tong += j  #tổng sẽ cộng dồn
 # Kiểm tra điều kiện
    if tong > i:
        print(f"{i} → Tổng ước = {tong}")
