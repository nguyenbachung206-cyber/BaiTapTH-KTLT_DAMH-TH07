# Nguyễn Bá Chung, mssv 245752021610143 
# bài 16: Người dùng nhập từ bàn phím chuỗi các số nhị phân viết liên tiếp được nối nhau
#           bởi dấu phẩy. Hãy nhập chuỗi đầu vào sau đó in ra những giá trị được nhập.

# Nhập chuỗi các số nhị phân, cách nhau bằng dấu phẩy
chuoi = input("Nhập các số nhị phân, cách nhau bằng dấu phẩy: ")

# Tách chuỗi thành danh sách
ds = chuoi.split(',')

# In ra danh sách các giá trị
print("Các số nhị phân đã nhập là:")
for so in ds:
    print(so.strip())  # .strip() để xóa khoảng trắng thừa (nếu có)
