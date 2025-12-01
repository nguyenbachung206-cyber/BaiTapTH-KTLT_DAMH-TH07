# Nguyễn Bá Chung, mssv 245752021610143
"""8.Xây dựng hàm “Sequential_Search(dlist, item)” (giải thuật tìm kiếm tuyến tính)
dưới dạng module. Viết chương trình nhập một dlist n phần tử từ bàn phím và tìm
kiếm phần tử item bất kỳ"""

# Sử dụng module tìm kiếm tuyến tính

def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return True, i
    return False, -1

# phần nhập/xuất
n = int(input("Nhập số phần tử của danh sách: "))
dlist = []   # tạo 1 từ điển trống
for i in range(n):
    dlist.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
    
# gọi hàm tuyến tính và in ra màn hình
item = int(input("Nhập phần tử cần tìm: "))
found, index = Sequential_Search(dlist, item)
print((found, index))
