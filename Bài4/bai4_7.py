# Nguyễn Bá Chung, mssv 245752021610143
# bai 7:Nhập một chuỗi từ bàn phím, hãy loại bỏ tất cả các chữ số khỏi chuỗi và in lại nội dung chuỗi mới ra màn hình.

chuoi = input('nhap chuoi tu ban phim: ')
# tạo chuỗi mới
chuoi_moi = ""
# duyệt từng kí tự trong chuỗi
for ch in chuoi:
    if not ch.isdigit(): # isdigit ko lấy số
        chuoi_moi += ch  # chuỗi mới 

# in kết quả
print('chuoi mới là: ',chuoi_moi)