# Nguyễn Bá Chung, mssv 245752021610143
#bài 5: Chỉnh sửa ví dụ ở bài 4: nhập 1 danh sách các từ từ bàn phím, in ra các từ đó theo thứ tự ngược lại thứ tự vừa nhập 
chuoi = input('nhập chuỗi từ bàn phím: ')
# tách chuỗi
S = chuoi.split()
# đảo ngược danh sách tại chỗ
S.reverse()
for ch in S: 
    print(ch)