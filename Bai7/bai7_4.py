# Nguyễn Bá Chung, mssv 245752021610143
"""4. Chương trình Python để đọc n dòng đầu tiên của tệp"""

# Chương trình đọc n dòng đầu tiên của tệp
file_path = r"c:\Users\HH\Downloads\chungg.txt"

# Nhập số dòng cần đọc
n = int(input("Nhập số dòng cần đọc: "))

try:
    # Mở tệp ở chế độ đọc với encoding UTF-8
    # 'with' đảm bảo file sẽ tự động đóng sau khi thoát khối
    with open(file_path, "r", encoding="utf-8") as f:
        # Lặp tối đa n lần để đọc n dòng
        for i in range(n):
            line = f.readline() # đọc 1 dòng từ file
            if not line:      # Nếu hết file thì dừng
                break
            # Loại bỏ ký tự xuống dòng ở cuối và in ra màn hình
            print(line.rstrip("\n"))
            
# Bắt lỗi khi file không tồn tại
except FileNotFoundError:
    print("Không tìm thấy tệp. Hãy kiểm tra lại đường dẫn!")
# Bắt mọi lỗi khác, in thông báo lỗi
except Exception as e:
    print("Lỗi:", e)
