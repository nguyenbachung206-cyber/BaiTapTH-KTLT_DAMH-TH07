# Nguyễn Bá Chung , msv 245752021610143
# Viết chương trình đếm số ký tự trong 1 xâu ký tự nhập vào từ bàn phím,
#  lưu các ký tự vào cấu trúc từ điển

str = input('enter a string: ')
dict = {} #tạo 1 từ điển rỗng để chưa
for n in str: #Duyệt từng ký tự n trong chuỗi vừa nhập.
    keys = dict.keys()#lấy danh sách tất cả các khóa hiện có trong từ điển.
    if n in keys:#Kiểm tra xem ký tự n đã xuất hiện trước đó chưa.
        dict[n] += 1# nếu hiện r Tăng giá trị đếm lên 1.
    else:
        dict[n] = 1 # ngược lại Thêm ký tự mới vào từ điển, với giá trị ban đầu là 1.
print (dict)