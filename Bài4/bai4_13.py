# Nguyễn Bá Chung, mssv 245752021610143
# bài 13. tìm vị trí của phần tử

# đầu vào và kèm tách chuỗi
chuoi = input('nhap chuoi tu ban phim(cách nhau = cách): ').split()
print('chuoi ban đầu: ', chuoi)

a = input('phần tử ta cần biết vị trí: ')
#kiểm tra vị trí ".index"
if a in chuoi: #xét xem thứ cần tìm vị trí có trong chuỗi ko
    vi_tri = chuoi.index(a) 
    print('vị trí của chuỗi là: ', vi_tri)
else:
    print('ko có tronh danh sách')

