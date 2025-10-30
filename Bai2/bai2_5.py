# Nguyễn Bá Chung , msv 245752021610143
# Viết chương trình nhập vào một số tự nhiên n > 0, in ra màn hình các số tự nhiên giảm dần từ n đến 0, mỗi ký tự in trên 1 hàng

n = int(input('nhập n từ bàn phím vào:  '))

while n >= 0: #Khi n còn lớn hơn hoặc bằng 0, tiếp tục lặp
    print(n) #in ra giá trị n hiện tại
    n = n - 1 # Mỗi vòng giảm n đi 1 đơn vị → tiến dần đến 0
