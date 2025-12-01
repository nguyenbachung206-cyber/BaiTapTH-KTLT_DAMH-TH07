# Nguyễn Bá Chung, mssv 245752021610143
"""6. Viết một class Python có hai phương thức get_String và print_String. get_String
chấp nhận một chuỗi từ người dùng và print_String in chuỗi đó bằng chữ in"""

class XuLyChuoi:
    def __init__(self):
        self.str = ""

    def get_String(self):
        # Nhập chuỗi từ người dùng
        self.str = input("Nhập chuỗi: ")

    def print_String(self):
        # In chuỗi đó bằng chữ in hoa
        print(self.str.upper())

# Sử dụng class
chuoi = XuLyChuoi()     # Tạo đối tượng
chuoi.get_String()       # Gọi hàm nhập chuỗi
chuoi.print_String()     # In chuỗi in hoa
