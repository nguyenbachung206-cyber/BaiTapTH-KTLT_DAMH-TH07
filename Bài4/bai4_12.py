# Nguyễn Bá Chung, mssv 245752021610143
#bai12.Bỏ phần tử khỏi list

# đầu vào và kèm tách chuỗi
chuoi = input('nhap chuoi tu ban phim: ').split()
print('chuỗi ban đầu : ',chuoi)

#xóa ptu bất kì
a = int(input('vị trí cần xóa trong chuỗi: '))
# chuyển a sang int để dùng với pop sô nguyên
chuoi.pop(a) # xóa ở vị trí bất kì mà bạn chọn
#in kết quả
print(chuoi)