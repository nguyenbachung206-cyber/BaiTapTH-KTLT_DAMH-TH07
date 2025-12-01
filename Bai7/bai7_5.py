# Nguyễn Bá Chung, mssv 245752021610143
"""5. Chương trình Python để nối văn bản vào tệp và hiển thị văn bản"""

file_path = r"c:\Users\HH\Downloads\chung.txt"

# Nhập nội dung cần nối
text = input("Nhập nội dung cần thêm vào tệp: ")

# Bước 1: Mở tệp ở chế độ append để nối thêm nội dung
with open(file_path, "a", encoding="utf-8") as f:
    f.write(text + "\n")     # thêm dòng mới

# Bước 2: Đọc và hiển thị lại toàn bộ nội dung tệp
print("\n Nội dung tệp sau khi thêm ")
with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
