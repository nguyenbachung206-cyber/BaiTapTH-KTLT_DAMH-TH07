# Nguyễn Bá Chung, MSSV: 245752021610143
"""
Xây dựng hàm “binary_search(list, value)” (giải thuật tìm kiếm nhị phân) dưới
dạng module. Viết chương trình nhập một list n phần tử từ bàn phím và tìm kiếm
phần tử value bất kỳ.
Ví dụ:
binary_search([1,2,3,5,8], 6) -> False
binary_search([1,2,3,5,8], 5) -> True
"""

import mymath5_9   # Gọi module vừa tạo ở cùng thư mục
def input_int(prompt):
    """Nhập một số nguyên hợp lệ."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" Vui lòng nhập số nguyên hợp lệ!")

#  Hàm nhập danh sách
def input_list(n):
    """Nhập danh sách n phần tử nguyên từ bàn phím."""
    lst = []
    for i in range(n):
        x = input_int(f"Nhập phần tử thứ {i+1}: ")
        lst.append(x)
    return lst
# Chương trình chính 
def main():
    n = input_int("Nhập số phần tử của danh sách (n ≥ 0): ")

    if n < 0:
        print(" Số phần tử phải ≥ 0. Thoát chương trình.")
        return
    # Nhập và sắp xếp danh sách
    lst = input_list(n) if n > 0 else []
    lst.sort()
    print("Danh sách sau khi sắp xếp (tăng dần):", lst)
    # Nhập giá trị cần tìm
    value = input_int("Nhập giá trị cần tìm: ")
    # Gọi hàm binary_search từ module mymath5_9
    found = mymath5_9.mymath5_9(lst, value)
    # In kết quả
    if found:
        print(f" Phần tử {value} có trong danh sách.")
    else:
        print(f" Phần tử {value} KHÔNG có trong danh sách.")
# điểm bđ chương trình
if __name__ == "__main__":
    main()
