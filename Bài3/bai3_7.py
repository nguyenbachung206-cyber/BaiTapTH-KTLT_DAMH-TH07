# Nguyễn Bá Chung, mssv 245752021610143
# 7. Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn"
# nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ.
def chan_or_le(n):
 if n%2 == 0: #ktra điều kiện chia hết cho 2 
   print ("Đây là một số chẵn")
 else:
   print ("Đây là một số lẻ")
#đầu vào của n
n = int(input('nhap n tu ban phim: '))
chan_or_le(n)