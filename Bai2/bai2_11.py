# Nguyễn Bá Chung , msv 245752021610143
# Viết chương trình kết nối các danh sách vào từ điển

# bước 1 khởi tạo 2 danh sách l và k
l = [1, 'python', 4, 7]
k = ['cse', 2, 'guntur', 8]

m = [] #khởi tạo 1 danh sách rỗng
# .apend dùng để thêm phần tử vào cuối danh sách
m.append(l) 
m.append(k)
print(m)
# Tạo một từ điển d
d = {1:1, 2:k, 'combine_line':m} #có 3 key : value
print(d)