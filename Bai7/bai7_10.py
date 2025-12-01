# Nguyễn Bá Chung, mssv 245752021610143
"""10.Viết chương trình python để tìm những từ dài nhất trong văn bản"""
# Tìm những từ dài nhất trong một tệp văn bản

file_path = r"c:\Users\HH\Downloads\chung.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()

    max_len = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_len]

    print("Chiều dài lớn nhất:", max_len)
    print("Các từ dài nhất trong tệp:")
    for w in longest_words:
        print(w)

except FileNotFoundError:
    print("Không tìm thấy tệp!")
except Exception as e:
    print("Lỗi:", e)
