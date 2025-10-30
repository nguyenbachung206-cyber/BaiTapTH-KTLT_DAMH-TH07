# Nguyễn Bá Chung, mssv 245752021610143 
#Bài 15.Người dùng nhập từ bàn phím liên tiếp các từ tiếng Anh viết tách nhau bởi dấu
# cách. Hãy nhập chuỗi đầu vào và tách thành các từ sau đó in ra màn hình các từ đó
# theo thứ tự từ điển.

# Nhập chuỗi từ bàn phím và tách chuỗi
chuoi = input("Nhập các từ tiếng Anh, cách nhau bằng dấu cách: ").split()
# Sắp xếp các từ theo thứ tự từ điển (alphabet)
chuoi.sort()
# In ra kết quả
print("Các từ sau khi sắp xếp theo thứ tự từ điển là:")

for tu in chuoi:
    print(tu)
