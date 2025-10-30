# Nguyễn Bá Chung, mssv 245752021610143 
# bài 22
# tạo 1 chuỗi kết quả rỗng để đưngj kết quả
ket_qua = []
# duyệt qua all số từ 1000 đến 3000
for i in range(1000, 3001):
    s = str(i) #Chuyển số i sang chuỗi để có thể duyệt từng chữ số.

    #Duyệt qua từng ký tự ch trong chuỗi s.
    #int(ch) % 2 == 0: kiểm tra xem chữ số đó có chẵn không.
    #Hàm all(...) trả về True nếu tất cả các chữ số đều chẵn.
    if all(int(ch) % 2 == 0 for ch in s):
        ket_qua.append(s) #Thêm số đó vào danh sách kết quả.
print(','.join(ket_qua))# in các ptu cách nhau bởi dấu phẩy