# Nguyễn Bá Chung, mssv 245752021610143 
#Bài 23:Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó

s = input("Nhập câu: ")
# Khởi tạo biến đếm
chu_cai = 0
chu_so = 0
# Duyệt qua từng ký tự trong chuỗi
for ch in s:
    if ch.isalpha(): # Nếu là chữ cái (a-z, A-Z)
        chu_cai += 1
    elif ch.isdigit(): # Nếu là chữ số (0-9)
        chu_so += 1
# In kết quả
print("Số chữ cái là:", chu_cai)
print("Số chữ số là:", chu_so)
