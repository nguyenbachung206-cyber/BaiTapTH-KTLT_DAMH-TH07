# Nguyễn Bá Chung, mssv 245752021610143
"""9. Viết chương trình Python để sao chép nội dung của tệp này sang tệp khác."""

# Chương trình sao chép nội dung từ tệp nguồn sang tệp đích

source_file = r"c:\Users\HH\Downloads\chung.txt"      # tệp nguồn
target_file = r"c:\Users\HH\Downloads\chung_copyy.txt"  # tệp đích

try:
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()       # đọc toàn bộ nội dung

    with open(target_file, "w", encoding="utf-8") as dst:
        dst.write(content)         # ghi sang tệp mới

    print("Đã sao chép nội dung sang tệp mới thành công!")

except FileNotFoundError:
    print("Không tìm thấy tệp nguồn, hãy kiểm tra lại đường dẫn!")
except Exception as e:
    print("Lỗi:", e)
