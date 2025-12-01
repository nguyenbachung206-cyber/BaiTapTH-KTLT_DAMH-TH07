# Nguyễn Bá Chung, mssv 245752021610143
"""BÀi 5: Viết chương trình tìm phần tử lớn nhất và nhỏ nhất của một danh sách
- Số lượng và giá trị của list được nhập từ bàn phím
- Phương thức sắp xếp và tìm phần tử lớn nhất được viết thành module"""
import mymath5_5 #gọi module của 5_5 ra

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị vào list
lst = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

# Hiển thị danh sách ban đầu
print("Danh sách ban đầu:", lst)

# Gọi hàm sắp xếp từ module
sorted_lst = mymath5_5.sap_xep(lst)
print("Danh sách sau khi sắp xếp: ", sorted_lst)

# Tìm phần tử lớn nhất và nhỏ nhất
print("Phần tử lớn nhất:", mymath5_5.lon_nhat(lst))
print("Phần tử nhỏ nhất:", mymath5_5.nho_nhat(lst))
