# Nguyễn Bá Chung, mssv 245752021610143 
# bài 24
# Nhập câu từ bàn phím
s = input("Nhập câu: ")
# Khởi tạo biến đếm
chu_hoa = 0
chu_thuong = 0
# Duyệt qua từng ký tự trong chuỗi
for ch in s:
    if ch.isupper():       # Nếu ký tự là chữ hoa (A–Z)
        chu_hoa += 1
    elif ch.islower():     # Nếu ký tự là chữ thường (a–z)
        chu_thuong += 1
# In kết quả
print("Chữ hoa:", chu_hoa)
print("Chữ thường:", chu_thuong)
