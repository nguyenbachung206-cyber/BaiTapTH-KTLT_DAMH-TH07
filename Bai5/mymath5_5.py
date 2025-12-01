# my module.py của bài 5_5
# Nguyễn Bá Chung, MSSV: 245752021610143
"Phương thức sắp xếp và tìm phần tử lớn nhất"
def sap_xep(lst):
    """Hàm sắp xếp danh sách tăng dần"""
    return sorted(lst)

def lon_nhat(lst):
    """Hàm tìm phần tử lớn nhất"""
    return max(lst)

def nho_nhat(lst):
    """Hàm tìm phần tử nhỏ nhất"""
    return min(lst)

# thêm 2 phần tử mới để làm 5_6
def vitri_lon_nhat(lst):
    """Hàm tìm vị trí phần tử lớn nhất"""
    max_value = max(lst)
    return lst.index(max_value)  # trả về vị trí đầu tiên của max

def vitri_nho_nhat(lst):
    """Hàm tìm vị trí phần tử nhỏ nhất"""
    min_value = min(lst)
    return lst.index(min_value)  # trả về vị trí đầu tiên của min