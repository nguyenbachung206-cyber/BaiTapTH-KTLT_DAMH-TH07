# Nguyễn Bá Chung, mssv 245752021610143
"""2. Chương trình đọc một file, tính số ký tự, số từ và số dòng của file"""
# Mở file
f = open(r'c:\Users\HH\Downloads\chungg.txt', 'r')
# Tạo biến đếm
char = 0   # số ký tự
wc = 0     # số từ
lc = 0     # số dòng
# Đọc từng dòng và cập nhật số liệu
for line in f:
    lc += 1                     # tăng số dòng mỗi khi đọc 1 dòng
    char += len(line)           # đếm số ký tự trong dòng
    wc += len(line.split())     # split() → tách dòng thành các từ
f.close() #đóng tệp để giải phóng tài nguyên.
print("The number of chars is %d" % char)
print("The number of words is %d" % wc)
print("The number of lines is %d" % lc)