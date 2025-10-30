# Nguyễn Bá Chung, mssv 245752021610143 
# Bài 19: Hãy tạo ra tuple P gồm các số nguyên tố nhỏ hơn 1 triệu.
import math
# Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# Tạo list các số nguyên tố nhỏ hơn 1 triệu
ds_nt = []
for i in range(2, 1_000_000):
    if la_so_nguyen_to(i):
        ds_nt.append(i)
# Chuyển sang tuple
P = tuple(ds_nt)
print("Có tất cả", len(P), "số nguyên tố nhỏ hơn 1 triệu.")
print("10 số đầu tiên:", P[:10])
