# Nguyễn Bá Chung, mssv 245752021610143
"""Viết chương trình Python dưới dạng class để chuyển đổi một số La Mã thành một
số nguyên"""
class py_solution:
    def roman_to_int(self, s):
        """
        Hàm chuyển đổi số La Mã (string) thành số nguyên (int)
        """
        # 1. Tạo từ điển ánh xạ giá trị
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        int_val = 0
        
        # 2. Duyệt qua từng ký tự trong chuỗi (theo lưu đồ)
        for i in range(len(s)):
            
            # Kiểm tra logic đặc biệt (IV, IX, XL...):
            # Nếu ký tự hiện tại lớn hơn ký tự đứng trước nó
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                # Công thức trong lưu đồ:
                # Cộng giá trị hiện tại VÀ trừ đi 2 lần giá trị trước đó
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                # Trường hợp bình thường: Cộng dồn giá trị
                int_val += rom_val[s[i]]
                
        return int_val

# --- CHẠY THỬ NGHIỆM (Giống trong hình) ---
# Tạo đối tượng và gọi hàm
print(py_solution().roman_to_int('MMMCMLXXXVI')) # Kết quả mong đợi: 3986
print(py_solution().roman_to_int('MMMM'))        # Kết quả mong đợi: 4000
print(py_solution().roman_to_int('C'))           # Kết quả mong đợi: 100