# Nguyễn Bá Chung, mssv 245752021610143 
# Nhập n, in n dòng đầu tiên của tam giác pascal

n = int(input('nhập vào số vòng của tam giác: '))
# tạo danh sách rỗng đựng từng hàng
pascal = []
for i in range(n): # duyệt qua từng dòng
    number_one = [1] #mỗi dòng đều bắt đầu bằng 1
    if i > 0:
        for j in range (1,i):
            # Mỗi phần tử = tổng 2 phần tử phía trên nó
            number_one.append(pascal[i-1][j-1] + pascal[i-1][j]) 
        # Dòng nào cũng kết thúc bằng 1
        number_one.append(1)
    # thêm dòng vừa tạo vào danh sách
    pascal.append(number_one)
# In ra tam giác Pascal
for number_one in pascal:
    print(number_one)
