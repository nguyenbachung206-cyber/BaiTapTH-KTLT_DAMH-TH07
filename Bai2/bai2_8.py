# Nguyễn Bá Chung , msv 245752021610143
# Viết chương trình in ra màn hình dãy số Fibonacci nhỏ hơn 4.000.000, 
# tìm tổng các số chẵn trong dãy đã in

#khởi tạo 2 số đàu tiên của dãy Fib
a , b = 0 , 1
# khai báo biến tổng ban đầu
tong_chan = 0
print('Dãy số fib ban đầu là: ')

while (a <= 4000000 ): #đảm bảo chỉ lấy số nhỏ hơn 4.000.000.
    print( a , end = " ") #được gọi trước khi cập nhật a, b, nên số in ra là chính xác.
    if a % 2 == 0:   # Kiểm tra số chẵn
        tong_chan += a
    a , b = b , a + b  #  Cập nhật số tiếp theo

print("\nTổng các số chẵn trong dãy:", tong_chan)



