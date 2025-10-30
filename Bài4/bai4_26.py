# Nguyễn Bá Chung, mssv 245752021610143 
# bài 26
tong_tien = 0 #khởi tạo biến tổng
while True:
    dong = input("Nhập nhật ký giao dịch (D/W + số tiền), hoặc Enter để kết thúc: ")
    if not dong:   # Nếu người dùng nhấn Enter (chuỗi rỗng) → thoát vòng lặp
        break

    # Tách dòng nhập thành 2 phần: ký tự (D hoặc W) và số tiền
    hanh_dong, so_tien = dong.split()
    so_tien = int(so_tien)  # đổi sang số nguyên

    # Xử lý theo loại giao dịch
    if hanh_dong.upper() == 'D':  # nạp tiền (Deposit)
        tong_tien += so_tien
    elif hanh_dong.upper() == 'W':  # rút tiền (Withdraw)
        tong_tien -= so_tien
    else:
        print("Lệnh không hợp lệ, vui lòng nhập lại!")

print("Số tiền thực trong tài khoản là:", tong_tien)
