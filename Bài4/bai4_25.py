# Nguyễn Bá Chung, mssv 245752021610143 
#bài 25: Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
# Nhập danh sách số, tách bằng dấu phẩy
ds = input("Nhập các số, cách nhau bằng dấu phẩy: ").split(',')
# Chuyển từng phần tử trong danh sách thành số nguyên
ds = [int(x) for x in ds]
# Lọc ra các số lẻ (số chia 2 dư 1)
so_le = [x for x in ds if x % 2 != 0]
# In kết quả ra màn hình, ngăn cách bằng dấu phẩy
print("Các số lẻ là:", ",".join(str(x) for x in so_le))
