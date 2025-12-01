# Nguyễn Bá Chung, mssv 245752021610143
"""6. In ra vị trí phần tử lớn nhất và nhỏ nhất tìm được ở bài tập trên"""

# gọi module 5_5 sau khi thêm phần 5_6
import mymath5_5
n = int(input("Nhập số lượng phần tử của danh sách: "))
# Nhập các giá trị vào list
lst = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(x)

# Hiển thị danh sách ban đầu
print("\nDanh sách ban đầu:", lst)

# Gọi các hàm từ module
sorted_lst = mymath5_5.sap_xep(lst)
print("Danh sách sau khi sắp xếp:", sorted_lst)

max_val = mymath5_5.lon_nhat(lst)
min_val = mymath5_5.nho_nhat(lst)
vitri_max = mymath5_5.vitri_lon_nhat(lst)
vitri_min = mymath5_5.vitri_nho_nhat(lst)

# In kết quả
print(f"\nPhần tử lớn nhất: {max_val} ở vị trí {vitri_max}")
print(f"Phần tử nhỏ nhất: {min_val} ở vị trí {vitri_min}")