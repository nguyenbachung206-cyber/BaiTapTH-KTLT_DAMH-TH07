# Nguyễn Bá Chung, mssv 245752021610143
# 6. Viết chương trình sau và giải thích việc truyền tham số của hàm

def get_sum(*num): #định nghĩa hàm get_sum
    # *num để nhận nhiều giá trị
    tong = 0  #biến tổng ban đầu
    #duyệt các tham số từ i đến num
    for i in num:
        tong += i  #tổng đc cộng dồn cho đến số cuối cùng
    return tong

result = get_sum( 6,4,3,2,1) #khai báo hàm để in kết quả
print('tong la:  ',result)
    
    
