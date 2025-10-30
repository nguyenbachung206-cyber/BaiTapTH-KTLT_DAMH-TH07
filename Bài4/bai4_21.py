# Nguyễn Bá Chung, mssv 245752021610143 
# Bài 21: 
# Nhập chuỗi nhị phân, ví dụ: 0100,0011,1010,1001
chuoi = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
# Tách chuỗi thành danh sách
ds = chuoi.split(',')
# Tạo danh sách để chứa các số chia hết cho 5
chia_het_5 = []
# Duyệt từng phần tử trong danh sách
for so_nhi_phan in ds:
    # Chuyển nhị phân sang thập phân
    gia_tri = int(so_nhi_phan, 2)
    
    # Kiểm tra chia hết cho 5
    if gia_tri % 5 == 0:
        chia_het_5.append(so_nhi_phan)

# In ra kết quả (nối bằng dấu phẩy)
print(','.join(chia_het_5))
