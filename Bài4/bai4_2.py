# Nguyễn Bá Chung, mssv 245752021610143
# Bài 2: Chỉnh sửa ví dụ trên: hãy bỏ qua không in ra những kí tự “không nhìn thấy” (dấu space và dấu tab).

S = input('nhập chuỗi từ bàn phím:  ')
# duyệt hết các kí tự trong chuỗi
for ch in S:
    # ta xét điều kiện khi ko có tab và space
    if ch not in[' ' , '\t']:
        print (ch) #in ra kết quả