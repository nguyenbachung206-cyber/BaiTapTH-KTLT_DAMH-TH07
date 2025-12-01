# Nguyễn Bá Chung, mssv 245752021610143
"""3. Định nghĩa class Nguoi và 2 class con của nó: Nam, Nu. Tất cả các class có
method "getGender" có thể in "Nam" cho class Nam và "Nữ" cho class Nu.
"""
class Nguoi(object):
    def getGender(self):
        return "Unknown"

class Nam(Nguoi):
    def getGender(self):
        return "Nam"

class Nu(Nguoi):
    def getGender(self):
        return "Nữ"

# Tạo đối tượng 
aNam = Nam()
aNu = Nu()

# Gọi phương thức 
print(aNam.getGender())   # In ra: Nam
print(aNu.getGender())    # In ra: Nữ
