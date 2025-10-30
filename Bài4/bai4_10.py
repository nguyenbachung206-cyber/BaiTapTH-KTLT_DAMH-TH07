# Nguyễn Bá Chung, mssv 245752021610143
# bài 10. Cắt list: lấy list nhưng bỏ phần tử đầu và cuối
#đầu vào
chuoi = input('nhập từ bàn phím chuỗi: ')
S = chuoi.split() #tách chuỗi
# bỏ phần tử đầu và cuối
x = S[1:-1]
# xét các phần từ còn lại của x và in ra trêm mỗi ptu 1 dong
for i in x: 
    print(i)
