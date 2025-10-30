# Nguyễn Bá Chung , msv 245752021610143

#khai báo result-danh sách rỗng để chứa
result = []

for n in range(2000 , 3201):
    #do range chạy từ start đến end-1 nên ta lấy thêm +1 để lấy hết từ 2000 đến 3200
    if n % 7 == 0 and n %5 != 0: # sử dụng if để sét 2 điều kiện đề bài để Thỏa mãn
        result.append(str(n)) #lưu số vào danh sách (chuyển sang chuỗi để join).
print(','.join(result))

