# Nguyễn Bá Chung , msv 245752021610143
import re # gọi thư viện có sắn trong python dùng để xử lý biểu thức chính quy
# tạo hàm vs tham số đầu vào là pass down
def kiem_tra_mat_khau(password): 
    # Mật khẩu phải dài từ 6 đến 12 ký tự.
    if len(password) < 6 or len(password) > 12:
        return False
    #re.search() trả về None nếu không tìm thấy mẫu → khi đó not làm điều kiện đúng → trả về False.
    if not re.search("[a-z]", password):#ít nhất 1 chữ thường
        return False
    if not re.search("[A-Z]", password):#ít nhất 1 in hoa
        return False
    if not re.search("[0-9]", password):# ít nhất 1 số từ 0-9
        return False
    if not re.search("[$#@]", password):#ít nhất 1 kí tự đắc biệt
        return False
    return True # qua đc các điều khiện trên -> mk hợp lệ
chuoi = input('nhập mật khẩu( cách nhau bằng dấu phẩy): ').split(",") 
                   #mk nhập vào và tách nhau bởi dấu phẩy và đc tách chuỗi bằng split
hop_le = [] #tạo 1 danh sách rỗng để đựng các mk hợp lệ 
for mk in chuoi:
    if kiem_tra_mat_khau(mk.strip()): #.strip() loại bỏ khoảng trắng dư thừa ở đầu/cuối.
        hop_le.append(mk.strip()) #Gọi hàm kiem_tra_mat_khau(mk.strip()) để kiểm tra.
                                #Nếu trả về True → thêm mật khẩu đó vào danh sách hop_le.
print("mật khẩu hợp lệ:", ", ".join(hop_le))