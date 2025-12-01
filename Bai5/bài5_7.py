# Nguyễn Bá Chung, mssv 245752021610143
"""Viết chương trình sử dụng thư viện NumPy để tạo một mảng có cấu trúc từ tên
sinh viên, chiều cao, lớp và các kiểu dữ liệu của họ. Bây giờ sắp xếp các mảng
theo chiều cao."""

import numpy as np  # gọi thư viện NumPy
# Định nghĩa kiểu dữ liệu (tên, chiều cao, lớp)
dtype_sv = [('ten', 'U30'), ('chieucao', 'f4'), ('lop', 'U10')]
# Tạo mảng dữ liệu sinh viên
sinhvien = np.array([
    ('Nguyễn Bá Chung', 1.68, 'K65'),
    ('Dương Phúc Hợp', 1.65, 'k65'),
    ('Trần Văn Minh', 1.80, 'K63'),
    ('Lê Thị Hoa', 1.58, 'K62'),
    ('Phạm Anh Tuấn', 1.75, 'K66')
], dtype=dtype_sv)
# In ra mảng ban đầu
print(" DANH SÁCH SINH VIÊN BAN ĐẦU ")
print(sinhvien)

# Sắp xếp mảng theo chiều cao (tăng dần)
sinhvien_sorted = np.sort(sinhvien, order='chieucao')

# In ra kết quả sau khi sắp xếp
print("\n DANH SÁCH SAU KHI SẮP XẾP THEO CHIỀU CAO ")
print(sinhvien_sorted)
