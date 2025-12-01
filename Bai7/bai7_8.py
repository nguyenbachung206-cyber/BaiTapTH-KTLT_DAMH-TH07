# Nguyễn Bá Chung, mssv 245752021610143
"""8. Viết chương trình Python để viết nội dung danh sách vào tệp.
"""

# Bước 1: Khởi tạo danh sách (có thể nhập từ người dùng hoặc định nghĩa sẵn)
dlist = [10, 20, 30, 40, 50]  # danh sách sẵn

# Nếu muốn nhập từ người dùng:
# n = int(input("Nhập số phần tử của danh sách: "))
# dlist = []
# for i in range(n):
#     dlist.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

# Bước 2: Định nghĩa đường dẫn tệp
file_path = r"c:\Users\HH\Downloads\dlist.txt"

# Bước 3: Mở tệp ở chế độ ghi ('w') và ghi từng phần tử
with open(file_path, "w", encoding="utf-8") as f:
    for item in dlist:
        f.write(str(item) + "\n")  # ghi mỗi phần tử trên 1 dòng

# Bước 4: Thông báo hoàn tất
print(f"Đã ghi danh sách vào tệp {file_path}")

# Bước 5: (Tùy chọn) Đọc lại và hiển thị nội dung tệp
print("\nNội dung tệp vừa ghi:")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
