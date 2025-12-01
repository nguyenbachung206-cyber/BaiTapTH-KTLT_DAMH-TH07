# Nguyễn Bá Chung, mssv 245752021610143
"""6. Chương trình Python để đọc n dòng cuối cùng của tệp"""

import os
def file_read_from_tail(fname, lines):
    bufsize = 8192 
    # Lấy kích thước tổng của file
    try:
        fsize = os.stat(fname).st_size 
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{fname}'")
        return
    iter = 0
    data = []
    # Mở file và bắt đầu đọc
    with open(fname, 'r') as f:
        # Nếu bufsize lớn hơn kích thước file, đặt bufsize bằng kích thước file
        if bufsize > fsize:
            bufsize = fsize
        # Bắt đầu vòng lặp đọc ngược
        while True:
            iter += 1  
            # Tính toán vị trí seek: lùi về cuối file từng bước (bufsize * iter)
            # Dùng max(0, fsize - bufsize * iter) để đảm bảo không seek lùi quá đầu file (vị trí 0)
            position = max(0, fsize - bufsize * iter)
            f.seek(position)   
            # Đọc các dòng từ vị trí seek đến cuối buffer hiện 
            data.extend(f.readlines())
            # 1. Đã tìm đủ số dòng yêu cầu (len(data) >= lines)
            # 2. Đã đọc hết file (f.tell() == 0, con trỏ file đang ở đầu)
            if len(data) >= lines or f.tell() == 0:
                # In ra 'lines' dòng cuối cùng đã thu thập được
                # data[-lines:] lấy ra n phần tử cuối cùng của list data
                print(''.join(data[-lines:]), end='')
                break 
print(r"--- Kết quả đọc 2 dòng cuối cùng từ 'c:\Users\HH\Downloads\chungg.txt' ---")
file_read_from_tail(r'c:\Users\HH\Downloads\chungg.txt', 2)
