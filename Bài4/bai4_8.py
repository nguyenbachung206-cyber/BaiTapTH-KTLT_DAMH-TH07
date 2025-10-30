# Nguyễn Bá Chung, mssv 245752021610143
# bai8. Nhập một dãy các từ từ bàn phím, hãy in ra từ dài nhất trong dãy vừa nhập, in ra mọi từ có cùng độ dài nhất.

# Nhập dãy từ từ bàn phím
chuoi = input("Nhập dãy các từ: ")

# Tách chuỗi thành danh sách các từ
ds_tu = chuoi.split()

# Tìm độ dài lớn nhất trong các từ
do_dai_max = max(len(tu) for tu in ds_tu)

# In ra tất cả các từ có độ dài bằng độ dài lớn nhất
print("Các từ dài nhất là:")
for tu in ds_tu:
    if len(tu) == do_dai_max:
        print(tu)
