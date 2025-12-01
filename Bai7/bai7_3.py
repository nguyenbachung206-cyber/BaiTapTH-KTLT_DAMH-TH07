# Nguyễn Bá Chung, mssv 245752021610143
"""3. Viết chương trình Python để đọc toàn bộ tệp văn bản"""

# mở file ta cần đọc
input_file = open(r'c:\Users\HH\Downloads\chungg.txt', 'r')

# duyệt qua các phần tử trong file
for line in input_file:
    print(line.split()) #in ra và tách chuỗi
