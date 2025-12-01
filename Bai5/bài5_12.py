# Nguyễn Bá Chung, mssv 245752021610143
"""12.Viết chương trình sử dụng thư viện NumPy để sắp xếp id sinh viên với chiều cao
tăng dần của sinh viên từ id sinh viên và chiều cao đã cho. In các chỉ số nguyên
mô tả thứ tự sắp xếp theo nhiều cột và dữ liệu được sắp xếp (sử dụng hàm
lexsort())
"""

import numpy as np
# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])
# Sử dụng lexsort: sắp xếp theo chiều cao trước, rồi theo id
indices = np.lexsort((student_id, student_height))
# In ra chỉ số sắp xếp
print("Chỉ số:")
print(indices)
# In dữ liệu đã sắp xếp
print("\nDữ liệu sắp xếp:")
for i in indices:
    print(student_id[i], student_height[i])