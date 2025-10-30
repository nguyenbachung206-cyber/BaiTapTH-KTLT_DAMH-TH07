# Nguyễn Bá Chung, mssv 245752021610143 
# bài 14: Sắp xếp các phần tử trong list
# đầu vào của chương trình 
ds = input('nhập danh sách: ').split()
# Hàm .sort()dùng để sắp xếp trực tiếp các phần tử trong list theo thứ tự tăng dần
ds.sort()
for kc in ds:
    print(kc)