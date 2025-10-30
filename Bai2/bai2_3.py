#  Nguyễn BÁ Chung , mssv 245752021610143
# Viết chương trình nhập vào một số và kiểm tra số đó là chẵn hay lẻ, in thông báo ra màn hình\\

n = int(input('nhập n từ bàn phím:  '))

#kiếm tra số chẵn hay lẻ bằng cách kiểm tra nó cs chia hết cho 2 hay ko
if n % 2 == 0:
    print('số này là số chẵn')
else:
    print('số lẻ')
