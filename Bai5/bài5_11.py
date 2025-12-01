# Nguyễn Bá Chung, mssv 245752021610143
"""11.Viết chương trình sử dụng thư viện NumPy để tạo một mảng có cấu trúc từ tên
sinh viên, chiều cao, lớp và các kiểu dữ liệu của họ. Bây giờ sắp xếp theo lớp, sau
đó chiều cao nếu lớp bằng nhau."""

import numpy as np # gọi hàm xử lý mảng
# tạo biến data đựng: Tên, Lớp, Cân nặng
data = [
    ('Chung', 7, 60),
    ('Nam', 6, 40),
    ('Hợp', 9, 42),
    ('Trường', 5, 99)
]
# Định nghĩa kiểu dữ liệu cho mảng có cấu trúc
dtype = [('name', 'U10'), ('class', 'i4'), ('height', 'f4')]
# Tạo mảng NumPy có cấu trúc
students = np.array(data, dtype=dtype)
# Sắp xếp theo lớp (class) và sau đó theo cân nặng (height)
sorted_students = np.sort(students, order=['class', 'height'])
# In kế1 quả
print(sorted_students)
