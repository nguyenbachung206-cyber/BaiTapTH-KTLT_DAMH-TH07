# Nguyễn Bá Chung, mssv 245752021610143
"""1. Chương trình đọc file và in đảo ngược kết quả"""
# mở tệp
input_file = open(r'c:\Users\HH\Downloads\chungg.txt','r')

# duyêt qua từng dòng cs trong tệp
for line in input_file:      
    line = line.strip()        # loại bỏ ký tự xuống dòng
    l = len(line)              # lấy độ dài của dòng
    s = ''                     # dùng để lưu chuỗi đảo ngược

    # dùng vòng lặp while để đảo chuỗi
    while l > 0:
        s = s + line[l - 1] # thêm ký tự cuối vào chuỗi mới
        l = l - 1           # giảm chỉ số
    print(s)
    
input_file.close() # Đóng tệp
