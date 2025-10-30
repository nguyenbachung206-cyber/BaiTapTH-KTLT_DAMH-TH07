# Nguyễn Bá Chung, mssv 245752021610143
# bài 11: Thêm phần tử vào list

#đầu vào
chuoi = input('nhap tu ban phim:  ').split() #kèm tách chuỗi
print('chuỗi ban đầu là: ', chuoi)

a = input('nhap thứ cần thêm vào: ')
chuoi.append(a)
print('sau khi thêm chuỗi là: ',chuoi)
# nếu muốn thêm phần tử ở vị trí bất kì
      # dùng chuoi.insert(vi tri , giá trị)
print('còn đây là khi cho chúng thành 1 hàng dọc')
for i in chuoi:
    print (i)
