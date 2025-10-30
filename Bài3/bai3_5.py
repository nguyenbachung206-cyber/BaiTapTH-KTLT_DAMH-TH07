# Nguyễn Bá Chung, mssv 245752021610143
# 5. Viết chương trình sau và xem sự thay đổi của biến
a = "Hello Guy!"

def say():
 #global a báo cho Python biết rằng ta đang dùng và thay đổi biến a toàn cục,
 #chứ không phải tạo một biến mới cục bộ.
 global a 
 a = " Vinh University " # gán biến a 
 print(a)
say() # gọi hàm
print(a)