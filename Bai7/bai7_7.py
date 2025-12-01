# Nguyễn Bá Chung, mssv 245752021610143
"""7. Viết chương trình Python để đếm số dòng trong tệp văn bản"""
# Chương trình đếm số dòng trong tệp

file_path = r"c:\Users\HH\Downloads\chungg.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        count = 0
        for _ in f:
            count += 1

    print("Số dòng trong tệp là:", count)

except FileNotFoundError:
    print("Không tìm thấy tệp. Hãy kiểm tra lại đường dẫn!")
except Exception as e:
    print("Lỗi:", e)
